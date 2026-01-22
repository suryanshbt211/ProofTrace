from dataclasses import dataclass
from typing import List

@dataclass
class RuleResult:
    rule_id: str
    status: str
    evidence: str
    confidence: float

@dataclass
class ProofTrace:
    decision_id: str
    rules: List[RuleResult]
    compliance_score: float
