# service/risk_service.py

from implementations.risk_implementation import predict_risk

class RiskService:

    @staticmethod
    def evaluate_patient_risk(data):
        return predict_risk(data)
    