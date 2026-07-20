from pydantic import BaseModel

class PatientRiskRequest(BaseModel):

    age: int
    gender: str

    glucose: float
    cholesterol: float
    bmi: float

    systolic_bp: float
    diastolic_bp: float
    heart_rate: float

    smoking: str
    alcohol: str

    clinical_notes: str