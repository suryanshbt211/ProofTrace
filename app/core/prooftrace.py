from app.models.prooftrace import ProofTrace

def generate_prooftrace(decision_id, rule_results):
    passed = sum(1 for r in rule_results if r.status == "PASS")
    score = passed / len(rule_results)
    return ProofTrace(
        decision_id=decision_id,
        rules=rule_results,
        compliance_score=score
    )
