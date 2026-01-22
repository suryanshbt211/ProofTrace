def run_pql(prooftrace, query: str):
    if query == "FAILED_RULES":
        return [r for r in prooftrace.rules if r.status != "PASS"]

    if query == "LOW_CONFIDENCE":
        return [r for r in prooftrace.rules if r.confidence < 0.7]

    if query.startswith("RULE:"):
        rule_id = query.split(":", 1)[1]
        return [r for r in prooftrace.rules if r.rule_id == rule_id]

    raise ValueError(f"Unknown PQL query: {query}")
