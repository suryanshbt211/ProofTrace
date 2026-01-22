import uuid
from app.models.prooftrace import ProofTrace

def replay(text, rules, validate_fn, parse_fn):
    constraints = parse_fn(rules)
    results = validate_fn(text, constraints)

    compliance = (
        sum(1 for r in results if r.status == "PASS")
        / max(len(results), 1)
    )

    return ProofTrace(
        decision_id=str(uuid.uuid4()),
        rules=results,
        compliance_score=round(compliance, 2),
    )
