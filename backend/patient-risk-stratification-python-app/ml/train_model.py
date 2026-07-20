# app/ml/train_model.py

import os
import joblib
import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

# -----------------------------------
# Load Dataset
# -----------------------------------

df = pd.read_csv("../data/patient_data.csv")

# -----------------------------------
# Drop unnecessary columns
# -----------------------------------

df = df.drop(columns=[
    "patient_id",
    "name"
])

# -----------------------------------
# Encode categorical columns
# -----------------------------------

categorical_cols = [
    "gender",
    "smoking",
    "alcohol"
]

label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# -----------------------------------
# Process clinical notes using TF-IDF
# -----------------------------------

tfidf = TfidfVectorizer(max_features=20)

text_features = tfidf.fit_transform(
    df["clinical_notes"]
).toarray()

text_df = pd.DataFrame(
    text_features,
    columns=tfidf.get_feature_names_out()
)

# Remove original text column
df = df.drop(columns=["clinical_notes"])

# Merge TF-IDF features
df = pd.concat(
    [df.reset_index(drop=True),
     text_df.reset_index(drop=True)],
    axis=1
)

# -----------------------------------
# Features and Target
# -----------------------------------

X = df.drop("risk_label", axis=1)
y = df["risk_label"]

# -----------------------------------
# Train Test Split
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------------
# MLflow Setup
# -----------------------------------

mlflow.set_experiment(
    "Patient_Risk_Stratification"
)

# -----------------------------------
# Train Model
# -----------------------------------

with mlflow.start_run():

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print(f"Accuracy: {accuracy}")

    # Log params
    mlflow.log_param(
        "model",
        "RandomForestClassifier"
    )

    mlflow.log_metric(
        "accuracy",
        accuracy
    )

    # Save model
    os.makedirs(
        "app/ml/saved_models",
        exist_ok=True
    )

    joblib.dump(
        model,
        "app/ml/saved_models/risk_model.pkl"
    )

    # Save vectorizer
    joblib.dump(
        tfidf,
        "app/ml/saved_models/tfidf.pkl"
    )

    # Save encoders
    joblib.dump(
        label_encoders,
        "app/ml/saved_models/encoders.pkl"
    )

    # MLflow model logging
    mlflow.sklearn.log_model(
        model,
        "risk_model"
    )

print("Model training completed.")