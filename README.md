# 🏥 Patient Risk Stratification System

An end-to-end AI-powered **Patient Risk Stratification System** that predicts patient risk levels using demographic information, clinical measurements, medical history, and clinical notes. The project consists of:

- **Backend:** FastAPI-based Machine Learning REST API
- **Frontend:** React + TypeScript (Vite + Material UI)
- **Machine Learning:** Scikit-learn risk prediction model with TF-IDF text processing
- **Experiment Tracking:** MLflow
- **Visualization/UI:** React Dashboard and optional Streamlit interface

---

# Project Architecture

```
                    +----------------------+
                    |   React Frontend     |
                    |  (Material UI + TS)  |
                    +----------+-----------+
                               |
                               |
                      REST API Calls
                               |
                               ▼
                  +------------------------+
                  |      FastAPI API       |
                  |   Risk Prediction API  |
                  +-----------+------------+
                              |
          ------------------------------------------
          |                    |                   |
          ▼                    ▼                   ▼
   Risk Prediction      ML Models           MLflow Tracking
      Service          TF-IDF + ML          Experiment Logs
          |
          ▼
  Trained Risk Model
```

---

# Repository Structure

```
Patient_Risk_Stratification/

│
├── backend/
│   │
│   ├── data/
│   │      patient_data.csv
│   │      clinical_notes.csv
│   │
│   ├── patient-risk-stratification-python-app/
│   │
│   │      main.py
│   │      mlflow.db
│   │
│   ├── routers/
│   ├── services/
│   ├── implementations/
│   ├── models/
│   ├── utils/
│   ├── ml/
│   │      train_model.py
│   │      clustering.py
│   │      model_loader.py
│   │      saved_models/
│   │
│   └── README.md
│
├── ui/
│   │
│   ├── app.py                (Streamlit UI)
│   │
│   └── reactjs/
│         patient-risk-stratification-react-app/
│
├── requirements.txt
│
└── README.md
```

---

# Features

## Backend

- FastAPI REST APIs
- Modular Architecture
- Request & Response Models
- Clinical Text Processing
- Patient Risk Prediction
- Risk Score Calculation
- MLflow Experiment Tracking
- Pre-trained ML Models
- CORS Enabled
- Structured Logging

---

## Frontend

- React 19
- TypeScript
- Material UI
- Axios Integration
- Responsive UI
- Risk Prediction Form
- Prediction Results Dashboard
- API Integration
- Form Validation

---

## Machine Learning

The project includes a trained machine learning pipeline capable of predicting patient risk categories.

### Components

- Feature Encoding
- TF-IDF Vectorizer
- Clinical Note Processing
- Risk Prediction Model
- Model Serialization
- Model Loader
- MLflow Integration

Saved models include:

```
risk_model.pkl
encoders.pkl
tfidf.pkl
```

---

# Technology Stack

## Backend

- Python
- FastAPI
- Scikit-Learn
- Pandas
- NumPy
- MLflow
- Joblib
- TF-IDF
- Uvicorn

---

## Frontend

- React 19
- TypeScript
- Vite
- Material UI
- Axios
- React Hook Form

---

# Backend Architecture

```
Client
   │
   ▼
FastAPI Router
   │
   ▼
Risk Service
   │
   ▼
Implementation Layer
   │
   ├── Risk Scoring
   ├── Text Processing
   ├── Model Loader
   ├── ML Prediction
   │
   ▼
Response
```

---

# API Endpoint

## Predict Patient Risk

```
POST /predict-risk
```

---

### Sample Request

```json
{
  "age": 65,
  "gender": "Male",
  "blood_pressure": 145,
  "heart_rate": 88,
  "diabetes": true,
  "hypertension": true,
  "clinical_note": "Patient has chest pain and uncontrolled hypertension."
}
```

---

### Sample Response

```json
{
  "risk_level": "High",
  "risk_score": 0.91,
  "recommendation": "Immediate physician consultation recommended."
}
```

---

# Backend Setup

## Clone Repository

```bash
git clone <repository-url>
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start FastAPI

```bash
cd backend/patient-risk-stratification-python-app

uvicorn main:app --reload
```

Application

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# MLflow

Start MLflow

```bash
mlflow ui
```

or

```bash
mlflow server \
--backend-store-uri sqlite:///mlflow.db \
--default-artifact-root ./mlruns \
--host 0.0.0.0 \
--port 5000
```

MLflow UI

```
http://localhost:5000
```

---

# Model Training

Train the model

```bash
python ml/train_model.py
```

Generated artifacts

```
risk_model.pkl

encoders.pkl

tfidf.pkl
```

---

# Frontend Setup

Navigate to React project

```bash
cd ui/reactjs/patient-risk-stratification-react-app
```

Install packages

```bash
npm install
```

Run application

```bash
npm run dev
```

Frontend URL

```
http://localhost:5173
```

Build

```bash
npm run build
```

Preview

```bash
npm run preview
```

---

# Streamlit UI (Optional)

The repository also includes a Streamlit application.

Run

```bash
cd ui

streamlit run app.py
```

---

# Project Workflow

```
Patient Data
      │
      ▼
Feature Engineering
      │
      ▼
Clinical Note Processing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Risk Prediction Model
      │
      ▼
Risk Score
      │
      ▼
Risk Category
      │
      ▼
REST API Response
      │
      ▼
React Dashboard
```

---

# Major Modules

### Backend

- FastAPI Application
- Risk Router
- Risk Service
- ML Implementation
- Model Loader
- Text Processing
- Risk Scoring
- MLflow Manager
- Logging Utilities

---

### Frontend

- React Components
- API Services
- Form Validation
- Prediction Dashboard
- Material UI Components

---

# Machine Learning Pipeline

```
Patient Data
      │
      ▼
Data Cleaning
      │
      ▼
Categorical Encoding
      │
      ▼
Clinical Text Processing
      │
      ▼
TF-IDF Features
      │
      ▼
Model Prediction
      │
      ▼
Risk Score
```

---

# Future Enhancements

- Explainable AI (SHAP/LIME)
- Patient Risk Dashboard
- Risk Trend Analytics
- Model Versioning
- Docker Support
- Kubernetes Deployment
- Authentication & Authorization
- Role-Based Access Control
- Cloud Deployment (Azure/AWS/GCP)
- CI/CD Pipeline
- Real-time Monitoring
- Model Drift Detection

---

# License

This project is intended for educational, research, and healthcare analytics purposes. Ensure compliance with applicable healthcare privacy regulations (such as HIPAA or GDPR) before using it with real patient data.

---

# Author

**Patient Risk Stratification System**

AI-powered Healthcare Risk Prediction Platform built using **FastAPI**, **React**, **Machine Learning**, **MLflow**, and **Scikit-learn**.