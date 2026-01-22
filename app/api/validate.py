from fastapi import APIRouter
from app.core.constraint_parser import parse_constraints
from app.core.validator import validate
from app.core.prooftrace import generate_prooftrace
import uuid

router = APIRouter()

@router.post("/validate")
def validate_text(payload: dict):
    text = payload["text"]
    constraints = parse_constraints(payload["rules"])
    results = validate(text, constraints)
    return generate_prooftrace(str(uuid.uuid4()), results)
