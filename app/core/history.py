class ProofTraceHistory:
    def __init__(self):
        self.runs = []

    def add(self, prooftrace):
        self.runs.append(prooftrace)

    def timeline(self):
        return [
            {
                "run": i + 1,
                "decision_id": pt.decision_id,
                "compliance_score": pt.compliance_score,
                "rules": pt.rules,
            }
            for i, pt in enumerate(self.runs)
        ]
