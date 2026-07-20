# Patient Risk Prediction React Application

A modern React + TypeScript frontend application for predicting patient health risk using a Machine Learning model exposed through a FastAPI REST API.

The application provides an intuitive clinical data entry form, submits patient information to the prediction API, and displays the predicted risk category along with the confidence score.

---

# Project Overview

This application is designed as the frontend for a Healthcare AI Risk Prediction system.

Users can:

- Enter patient demographic information
- Enter vital signs
- Enter laboratory values
- Provide clinical notes
- Submit the data to the prediction API
- View prediction results in a clean dashboard

The backend performs Machine Learning inference and returns the prediction.

---

# Features

- React 19
- TypeScript
- Vite
- Material UI (MUI)
- React Hook Form
- Axios API Integration
- Responsive UI
- Sample Data Loader
- Form Reset
- Prediction Summary Card
- Confidence Progress Bar
- Loading Indicator

---

# Technology Stack

| Technology | Purpose |
|------------|----------|
| React | UI Development |
| TypeScript | Type Safety |
| Vite | Build Tool |
| Material UI | UI Components |
| React Hook Form | Form Management |
| Axios | REST API Communication |
| FastAPI | Backend API |
| Python | Machine Learning Backend |

---

# Project Structure

```
src/
│
├── api/
│   └── riskApi.ts
│
├── assets/
│
├── components/
│   ├── RiskForm.tsx
│   └── PredictionCard.tsx
│
├── types/
│   └── risk.ts
│
├── App.tsx
├── App.css
├── index.css
└── main.tsx
```

---

# Application Workflow

```
User
   │
   ▼
RiskForm
   │
   ▼
React Hook Form
   │
   ▼
Axios
   │
POST /predict-risk
   │
   ▼
FastAPI Backend
   │
Machine Learning Model
   │
   ▼
Prediction Response
   │
   ▼
PredictionCard
```

---

# Input Parameters

| Field | Type |
|--------|------|
| Age | Number |
| Gender | Male/Female |
| BMI | Number |
| Glucose | Number |
| Cholesterol | Number |
| Heart Rate | Number |
| Systolic BP | Number |
| Diastolic BP | Number |
| Smoking | Yes/No |
| Alcohol | Yes/No |
| Clinical Notes | Text |

---

# Sample Request

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
  "clinical_notes": "Patient has severe hypertension and uncontrolled diabetes"
}
```

---

# Sample Response

```json
{
  "risk_category": "High Risk",
  "confidence": 96.5
}
```

---

# Prediction Output

The application displays

- Risk Category
- Confidence Percentage
- Confidence Progress Bar
- Risk Indicator Color

Example

```
Risk Category

High Risk

Confidence

96.5%
```

---

# API Configuration

Current API endpoint:

```ts
http://127.0.0.1:8000/predict-risk
```

Location:

```
src/api/riskApi.ts
```

```ts
const api = axios.create({
    baseURL: "http://127.0.0.1:8000"
});
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Navigate to project

```bash
cd patient-risk-react
```

Install dependencies

```bash
npm install
```

Run development server

```bash
npm run dev
```

Open browser

```
http://localhost:5173
```

---

# Available Scripts

Start Development

```bash
npm run dev
```

Production Build

```bash
npm run build
```

Preview Production Build

```bash
npm run preview
```

Lint

```bash
npm run lint
```

---

# Dependencies

Main dependencies include:

- React
- React DOM
- TypeScript
- Axios
- Material UI
- React Hook Form
- Emotion

---

# Form Features

- Default Sample Data
- Client-side Form Management
- Controlled Components
- Reset Button
- Load Sample Button
- Loading Spinner
- API Submission

---

# UI Components

## RiskForm

Responsible for:

- Collecting patient information
- Validation
- API submission

---

## PredictionCard

Displays

- Risk Category
- Confidence
- Progress Bar
- Color-coded Risk Status

---

# Data Models

## RiskRequest

```ts
interface RiskRequest {
    age: number;
    gender: string;
    glucose: number;
    cholesterol: number;
    bmi: number;
    systolic_bp: number;
    diastolic_bp: number;
    heart_rate: number;
    smoking: string;
    alcohol: string;
    clinical_notes: string;
}
```

---

## RiskResponse

```ts
interface RiskResponse {
    risk_category: string;
    confidence: number;
}
```

---

# Future Enhancements

- Authentication
- Dark Mode
- Form Validation
- Error Handling
- Prediction History
- Download Prediction Report
- Patient Dashboard
- Charts & Analytics
- API Environment Configuration
- Docker Support
- Unit Testing
- Integration Testing
- CI/CD Pipeline

---

# Backend Requirements

The frontend expects a FastAPI backend exposing

```
POST /predict-risk
```

Response

```json
{
    "risk_category": "High Risk",
    "confidence": 96.5
}
```

---

# Recommended Improvements

- Replace hardcoded API URL with environment variables.
- Add React Router for scalable navigation.
- Implement comprehensive form validation using `react-hook-form`.
- Improve TypeScript typing by avoiding `any` in API responses.
- Introduce centralized error handling and toast notifications.
- Add loading skeletons and empty-state UI.
- Organize components into feature-based folders.
- Use environment-specific configuration files (`.env`).
- Add unit tests with Vitest and React Testing Library.

---

# License

This project is intended for educational and research purposes.

---

# Author

Developed using:

- React
- TypeScript
- Vite
- Material UI
- React Hook Form
- Axios
- FastAPI
- Machine Learning