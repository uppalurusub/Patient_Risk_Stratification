# ml/model_loader.py

import joblib

model = joblib.load(
    "ml/saved_models/risk_model.pkl"
)

def get_model():
    return model