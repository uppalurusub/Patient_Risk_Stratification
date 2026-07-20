# 🏥 Patient Risk Stratification using Machine Learning

## 📌 Project Overview

Patient Risk Stratification is an end-to-end Machine Learning application that predicts the clinical risk category of a patient using demographic information, vital signs, laboratory values, lifestyle factors, and unstructured clinical notes.

The application combines structured healthcare data with Natural Language Processing (NLP) techniques to provide accurate patient risk predictions. It exposes REST APIs using FastAPI and includes a Streamlit web application for interactive predictions.

---

# 🎯 Business Problem

Healthcare providers need to identify high-risk patients early to:

- Reduce hospital readmissions
- Improve patient outcomes
- Prioritize clinical interventions
- Optimize healthcare resources
- Support preventive care initiatives

Traditional rule-based systems often fail to capture complex interactions between clinical variables and physician notes. This project leverages Machine Learning to automate patient risk assessment.

---

# 🚀 Solution

The application predicts patient risk categories by analyzing:

- Demographics
- Vital signs
- Laboratory values
- Lifestyle habits
- Clinical notes (NLP)

The prediction engine combines structured numerical features with TF-IDF vectorized clinical text to generate patient risk predictions with confidence scores.

---

# 🏗 Project Architecture

```
                 Patient Information
                        │
        ┌───────────────┴────────────────┐
        │                                │
 Structured Features              Clinical Notes
        │                                │
 Label Encoding                 TF-IDF Vectorization
        │                                │
        └───────────────┬────────────────┘
                        │
               Feature Engineering
                        │
                 Trained ML Model
                        │
              Risk Stratification
                        │
          FastAPI REST API / Streamlit UI
```



# 📊 Dataset

The project uses structured healthcare information along with clinical notes.

## Structured Features

| Feature | Description |
|----------|-------------|
| age | Patient age |
| gender | Gender |
| glucose | Blood glucose level |
| cholesterol | Cholesterol level |
| bmi | Body Mass Index |
| systolic_bp | Systolic Blood Pressure |
| diastolic_bp | Diastolic Blood Pressure |
| heart_rate | Heart Rate |
| smoking | Smoking status |
| alcohol | Alcohol consumption |

## Unstructured Feature

- Clinical Notes

Example:

```
Patient presents with chest pain and uncontrolled hypertension.
```

---

# 🎯 Target Variable

```
risk_label
```

Example categories:

- Low Risk
- Medium Risk
- High Risk

---

# ⚙ Machine Learning Pipeline

## Data Preprocessing

- Missing value handling
- Feature selection
- Label Encoding
- Text preprocessing
- TF-IDF Vectorization

---

## Feature Engineering

### Numerical Features

- Age
- BMI
- Blood Pressure
- Heart Rate
- Glucose
- Cholesterol

### Encoded Features

- Gender
- Smoking
- Alcohol

### Text Features

Clinical Notes

↓

TF-IDF

↓

Sparse Matrix

↓

Combined with structured data

---

# 🤖 Machine Learning Model

The project loads a trained classification model from:

```
app/ml/saved_models/risk_model.pkl
```

Additional artifacts:

- TF-IDF Vectorizer
- Label Encoders

---

# 🔍 Prediction Flow

```
Input Request

↓

Validate Request

↓

Encode Categorical Variables

↓

Vectorize Clinical Notes

↓

Merge Features

↓

Predict Risk Category

↓

Calculate Confidence

↓

Return JSON Response
```

---

# 📦 API Endpoint

## POST

```
/predict-risk
```

---

## Sample Request

```json
{
  "age": 62,
  "gender": "Male",
  "glucose": 240,
  "cholesterol": 280,
  "bmi": 34,
  "systolic_bp": 180,
  "diastolic_bp": 110,
  "heart_rate": 98,
  "smoking": "Yes",
  "alcohol": "No",
  "clinical_notes": "Patient has uncontrolled diabetes, hypertension, obesity and chest pain."
}
```

---

## Sample Response

```json
{
  "risk_category": "High Risk",
  "confidence": 96.45
}
```

---

# 🖥 Streamlit Application

The Streamlit interface provides:

- Patient Information Form
- Clinical Notes Input
- One-click Prediction
- Confidence Score Display
- Interactive Dashboard

Run:

```bash
streamlit run ui/app.py
```

---

# ⚡ FastAPI Server

Run:

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```
http://localhost:8000/docs
```

ReDoc:

```
http://localhost:8000/redoc
```

---

# 📈 Machine Learning Workflow

```
Dataset

↓

Preprocessing

↓

Feature Engineering

↓

TF-IDF

↓

Encoding

↓

Model Training

↓

Model Validation

↓

Model Saving

↓

REST API

↓

Prediction
```

---

# 📚 Technologies Used

## Backend

- FastAPI
- Python

## Machine Learning

- Scikit-Learn
- XGBoost
- NumPy
- Pandas
- Joblib

## NLP

- TF-IDF Vectorizer

## Frontend

- Streamlit

## Experiment Tracking

- MLflow

---

# 📦 Required Packages

```
fastapi
uvicorn
streamlit
pandas
numpy
scikit-learn
xgboost
joblib
mlflow
loguru
pydantic
python-multipart
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

## Clone Repository

```bash
git clone <repository-url>
```

---

## Install Packages

```bash
pip install -r requirements.txt
```

---

## Start FastAPI

```bash
uvicorn app.main:app --reload
```

---

## Launch Streamlit

```bash
streamlit run ui/app.py
```

---

# 📊 Expected Workflow

```
User

↓

Streamlit UI

↓

FastAPI

↓

Prediction Service

↓

ML Model

↓

Risk Category

↓

Confidence Score
```

---

# 🎯 Use Cases

- Hospital Risk Assessment
- Population Health Management
- Chronic Disease Monitoring
- Clinical Decision Support
- Preventive Care Programs
- Healthcare Analytics
- Remote Patient Monitoring
- Insurance Risk Assessment

---

# 🔮 Future Enhancements

- Deep Learning Models
- Transformer-based Clinical NLP (e.g., ClinicalBERT)
- SHAP Explainability
- LIME Interpretability
- Real-time Risk Monitoring
- Batch Predictions
- Docker Deployment
- Kubernetes Support
- Azure/AWS Deployment
- CI/CD Pipeline
- Patient Risk Dashboard
- Role-based Authentication

---

# 👨‍💻 Author

Machine Learning Project

**Patient Risk Stratification using Structured Clinical Data and Natural Language Processing**

Developed using:

- FastAPI
- Streamlit
- Scikit-Learn
- TF-IDF
- MLflow
- Python