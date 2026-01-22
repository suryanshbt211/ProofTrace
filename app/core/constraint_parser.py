import os
import json
from app.models.constraint import Constraint
from app.gemini.client import get_gemini_model


def parse_constraints(text: str):
    """
    Uses Gemini to convert natural-language requirements
    into structured, executable constraints.

    STEP 14 FEATURES:
    - Explicit assumption surfacing
    - Enforceable vs non-enforceable distinction
    - Strict JSON contract
    - Interface preserved

    TEST SAFETY:
    - Deterministic fallback when PROOFTRACE_TEST_MODE=1
    """

    # ==========================================================
    # 🔒 TEST MODE (NO GEMINI CALLS — DETERMINISTIC)
    # ==========================================================
    if os.getenv("PROOFTRACE_TEST_MODE") == "1":
        return [
            Constraint(
                id="R1",
                description=text,
                enforceable=True,
                assumption="Test-mode deterministic constraint (Gemini bypassed)"
            )
        ]

    # ==========================================================
    # 🤖 PRODUCTION MODE (GEMINI)
    # ==========================================================
    model = get_gemini_model()  # Lazy init (correct)

    prompt = f"""
You are a requirements-to-constraints parser for an AI auditing system.

Your job:
- Extract constraints from the requirement
- Detect ambiguity
- Make assumptions EXPLICIT
- Decide whether each constraint is enforceable by a machine

IMPORTANT RULES:
- If a requirement is vague, subjective, or undefined (e.g. "creative", "high quality"),
  you MUST:
    - Set enforceable = false
    - Add an assumption explaining how it was interpreted
- If a requirement is clear and testable, enforceable = true
- NEVER leave assumption empty when ambiguity exists

Return STRICT JSON ONLY.
No markdown. No explanations. No extra text.

The JSON schema MUST be EXACTLY:

{{
  "constraints": [
    {{
      "id": "R1",
      "description": "string",
      "enforceable": true,
      "assumption": "string or null"
    }}
  ]
}}

Requirement:
\"\"\"{text}\"\"\"

Return ONLY the JSON object.
"""

    response = model.generate_content(prompt)
    raw = response.text.strip()

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        # 🔒 Hard fail-safe: model violated contract
        return [
            Constraint(
                id="R1",
                description="Unparseable requirement",
                enforceable=False,
                assumption="Gemini failed to return valid JSON"
            )
        ]

    constraints = []

    for c in data.get("constraints", []):
        try:
            constraints.append(Constraint(**c))
        except Exception:
            constraints.append(
                Constraint(
                    id=c.get("id", "R?"),
                    description="Malformed constraint",
                    enforceable=False,
                    assumption="Constraint fields missing or invalid"
                )
            )

    return constraints
