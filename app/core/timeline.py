class ProofTraceTimeline:
    def __init__(self):
        self.history = []

    def add(self, prooftrace):
        self.history.append(prooftrace)

    def latest(self):
        return self.history[-1] if self.history else None

    def all(self):
        return self.history
