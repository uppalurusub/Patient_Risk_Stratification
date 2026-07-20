# router/risk_router.py

from fastapi import APIRouter

from models.request_model import PatientRiskRequest
from services.risk_service import RiskService

router = APIRouter()

@router.post("/predict-risk")

def predict_risk(request: PatientRiskRequest):

    result = RiskService.evaluate_patient_risk(
        request
    )

    return result