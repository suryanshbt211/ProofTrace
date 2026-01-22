import os
import json
from app.models.prooftrace import RuleResult
from app.gemini.client import get_gemini_model


def validate(text: str, constraints):
    """
    Rule-by-rule validation using Gemini.

    STEP 13–15 FEATURES:
    - Rule-level PASS / FAIL / UNVERIFIABLE
    - Explicit evidence quoting
    - Anti-hallucination verification
    - Confidence surfacing

    TEST SAFETY:
    - Deterministic behavior when PROOFTRACE_TEST_MODE=1
    """

    results = []

    # ==========================================================
    # 🔒 TEST MODE (NO GEMINI — DETERMINISTIC)
    # ==========================================================
    if os.getenv("PROOFTRACE_TEST_MODE") == "1":
        for c in constraints:
            # Very simple deterministic logic for tests
            if "email" in c.description.lower() and "@" in text:
                results.append(
                    RuleResult(
                        rule_id=c.id,
                        status="FAIL",
                        evidence="Detected email address",
                        confidence=0.9,
                    )
                )
            else:
                results.append(
                    RuleResult(
                        rule_id=c.id,
                        status="PASS",
                        evidence="No violation detected",
                        confidence=0.9,
                    )
                )
        return results

    # ==========================================================
    # 🤖 PRODUCTION MODE (GEMINI)
    # ==========================================================
    model = get_gemini_model()

    for c in constraints:
        prompt = f"""
You are auditing text against a rule.

Rule:
{c.description}

Text:
{text}

Return STRICT JSON ONLY:
{{
  "status": "PASS | FAIL | UNVERIFIABLE",
  "evidence": "EXACT quote from text or empty string",
  "confidence": 0.0-1.0
}}
"""

        response = model.generate_content(prompt)
        raw = response.text.strip()

        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            results.append(
                RuleResult(
                    rule_id=c.id,
                    status="ERROR",
                    evidence="Gemini returned invalid JSON",
                    confidence=0.0,
                )
            )
            continue

        evidence = data.get("evidence", "").strip()

        # ======================================================
        # 🔒 ANTI-HALLUCINATION VERIFIER (KILL SHOT)
        # ======================================================
        if evidence and evidence not in text:
            results.append(
                RuleResult(
                    rule_id=c.id,
                    status="ERROR",
                    evidence="Hallucination detected: evidence not found in source text",
                    confidence=0.0,
                )
            )
            continue

        results.append(
            RuleResult(
                rule_id=c.id,
                status=data.get("status", "UNVERIFIABLE"),
                evidence=evidence or "No concrete evidence cited",
                confidence=float(data.get("confidence", 0.5)),
            )
        )

    return results
