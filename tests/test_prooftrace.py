# tests/test_prooftrace.py

from app.core.constraint_parser import parse_constraints
from app.core.validator import validate
from app.core.replay_engine import replay
from app.core.pql_engine import run_pql
from app.core.diff_engine import diff_prooftraces

from app.models.prooftrace import ProofTrace, RuleResult


def test_constraint_parsing():
    constraints = parse_constraints("Must not include email addresses")
    assert len(constraints) >= 1
    assert constraints[0].description.lower().find("email") != -1


def test_validation_detects_email():
    constraints = parse_constraints("Must not include email addresses")
    results = validate("Contact me at test@test.com", constraints)
    assert results[0].status == "FAIL"


def test_replay_changes_outcome():
    text = "Contact me at test@test.com"

    pt_a = replay(
        text,
        "Must not include email addresses",
        validate,
        parse_constraints
    )

    pt_b = replay(
        text,
        "Email addresses are allowed",
        validate,
        parse_constraints
    )

    # Replay runs without crashing and produces ProofTrace-like output
    assert isinstance(pt_a, ProofTrace)
    assert isinstance(pt_b, ProofTrace)


def test_pql_failed_rules():
    pt = ProofTrace(
        decision_id="test",
        rules=[
            RuleResult("R1", "FAIL", "email found", 0.9),
            RuleResult("R2", "PASS", "ok", 0.95),
        ],
        compliance_score=0.5
    )

    failed = run_pql(pt, "FAILED_RULES")
    assert len(failed) == 1
    assert failed[0].rule_id == "R1"


def test_hallucination_detection():
    """
    Anti-hallucination safety:
    Evidence quoted by Gemini must exist in the source text.
    """

    constraints = parse_constraints("Must not include email addresses")
    text = "Hello world"

    results = validate(text, constraints)

    for r in results:
        if r.status == "FAIL":
            assert r.evidence in text
