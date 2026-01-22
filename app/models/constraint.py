from pydantic import BaseModel
from typing import Optional

class Constraint(BaseModel):
    id: str
    description: str
    enforceable: bool
    assumption: Optional[str] = None
