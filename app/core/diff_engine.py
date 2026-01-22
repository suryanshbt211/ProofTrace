def diff_prooftraces(pt_a, pt_b):
    diffs = []

    rules_a = {r.rule_id: r for r in pt_a.rules}
    rules_b = {r.rule_id: r for r in pt_b.rules}

    all_ids = set(rules_a) | set(rules_b)

    for rid in all_ids:
        ra = rules_a.get(rid)
        rb = rules_b.get(rid)

        if ra and not rb:
            diffs.append({"rule_id": rid, "change": "REMOVED", "before": ra})
            continue

        if rb and not ra:
            diffs.append({"rule_id": rid, "change": "ADDED", "after": rb})
            continue

        if (
            ra.status != rb.status
            or ra.evidence != rb.evidence
            or ra.confidence != rb.confidence
        ):
            diffs.append({
                "rule_id": rid,
                "change": "MODIFIED",
                "before": ra,
                "after": rb,
            })

    return diffs
