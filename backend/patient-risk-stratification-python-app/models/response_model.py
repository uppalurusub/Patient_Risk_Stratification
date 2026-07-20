# models/response_model.py

from pydantic import BaseModel

class PatientRiskResponse(BaseModel):
    risk_score: float
    risk_category: str
    cluster: int