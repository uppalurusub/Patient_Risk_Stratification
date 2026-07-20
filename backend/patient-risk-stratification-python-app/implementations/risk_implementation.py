# app/implementations/risk_implementation.py

import numpy as np
import pandas as pd
import joblib

# -----------------------------------
# Load Saved Objects
# -----------------------------------

model = joblib.load(
    "ml/saved_models/risk_model.pkl"
)

tfidf = joblib.load(
    "ml/saved_models/tfidf.pkl"
)

encoders = joblib.load(
    "ml/saved_models/encoders.pkl"
)

# -----------------------------------
# Prediction Function
# -----------------------------------

def predict_risk(data):

    # Encode categorical columns
    gender = encoders["gender"].transform(
        [data.gender]
    )[0]

    smoking = encoders["smoking"].transform(
        [data.smoking]
    )[0]

    alcohol = encoders["alcohol"].transform(
        [data.alcohol]
    )[0]

    # TF-IDF transformation
    text_features = tfidf.transform(
        [data.clinical_notes]
    ).toarray()

    # Base numeric features
    base_features = np.array([[
        data.age,
        data.glucose,
        data.cholesterol,
        data.bmi,
        data.systolic_bp,
        data.diastolic_bp,
        data.heart_rate,
        gender,
        smoking,
        alcohol
    ]])

    # Merge all features
    final_features = np.hstack([
        base_features,
        text_features
    ])

    # Prediction
    prediction = model.predict(
        final_features
    )[0]

    probability = model.predict_proba(
        final_features
    ).max()

    return {
        "risk_category": prediction,
        "confidence": round(
            float(probability) * 100,
            2
        )
    }