import streamlit as st
import requests

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

API_URL = "http://localhost:8000/predict-risk"

st.set_page_config(
    page_title="Patient Risk Prediction",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 AI Patient Risk Prediction System")
st.markdown("---")

# ---------------------------------------------------------
# Patient Information
# ---------------------------------------------------------

st.header("Patient Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=62
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"],
        index=0
    )

    glucose = st.number_input(
        "Glucose",
        min_value=0,
        value=240
    )

    cholesterol = st.number_input(
        "Cholesterol",
        min_value=0,
        value=280
    )

    bmi = st.number_input(
        "BMI",
        min_value=0.0,
        value=34.0
    )

with col2:

    systolic_bp = st.number_input(
        "Systolic BP",
        min_value=0,
        value=180
    )

    diastolic_bp = st.number_input(
        "Diastolic BP",
        min_value=0,
        value=110
    )

    heart_rate = st.number_input(
        "Heart Rate",
        min_value=0,
        value=98
    )

    smoking = st.selectbox(
        "Smoking",
        ["No", "Yes"],
        index=1
    )

    alcohol = st.selectbox(
        "Alcohol",
        ["No", "Yes"],
        index=0
    )

clinical_notes = st.text_area(
    "Clinical Notes",
    value="Patient has severe hypertension and uncontrolled diabetes",
    height=150
)

st.markdown("---")

# ---------------------------------------------------------
# Prediction Button
# ---------------------------------------------------------

if st.button("🔍 Predict Risk", use_container_width=True):

    payload = {
        "age": age,
        "gender": gender,
        "glucose": glucose,
        "cholesterol": cholesterol,
        "bmi": bmi,
        "systolic_bp": systolic_bp,
        "diastolic_bp": diastolic_bp,
        "heart_rate": heart_rate,
        "smoking": smoking,
        "alcohol": alcohol,
        "clinical_notes": clinical_notes
    }

    with st.spinner("Predicting Patient Risk..."):

        try:

            response = requests.post(
                API_URL,
                json=payload,
                timeout=60
            )

            if response.status_code == 200:

                result = response.json()

                st.subheader("Prediction Result")

                # -----------------------------------------------------
                # Display based on response type
                # -----------------------------------------------------

                if isinstance(result, dict):

                    # Display each field as Metric if numeric
                    for key, value in result.items():

                        if isinstance(value, (int, float, str)):
                            st.metric(
                                label=key.replace("_", " ").title(),
                                value=value
                            )

                    
                    
                else:
                    st.write(result)

            else:
                st.error(f"API Error : {response.status_code}")
                st.write(response.text)

        except requests.exceptions.ConnectionError:
            st.error("Unable to connect to FastAPI server.")

        except Exception as ex:
            st.exception(ex)