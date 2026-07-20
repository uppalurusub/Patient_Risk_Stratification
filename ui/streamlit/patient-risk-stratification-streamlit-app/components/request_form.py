import streamlit as st
def render():
    st.header("Patient Information")
    c1,c2=st.columns(2)
    with c1:
        age=st.number_input("Age",1,120,62)
        gender=st.selectbox("Gender",["Male","Female"])
        glucose=st.number_input("Glucose",0,240)
        cholesterol=st.number_input("Cholesterol",0,280)
        bmi=st.number_input("BMI",0.0,100.0,34.0)
    with c2:
        systolic_bp=st.number_input("Systolic BP",0,180)
        diastolic_bp=st.number_input("Diastolic BP",0,110)
        heart_rate=st.number_input("Heart Rate",0,98)
        smoking=st.selectbox("Smoking",["No","Yes"],1)
        alcohol=st.selectbox("Alcohol",["No","Yes"],0)
    notes=st.text_area("Clinical Notes","Patient has severe hypertension and uncontrolled diabetes",height=150)
    return {"age":age,"gender":gender,"glucose":glucose,"cholesterol":cholesterol,"bmi":bmi,"systolic_bp":systolic_bp,"diastolic_bp":diastolic_bp,"heart_rate":heart_rate,"smoking":smoking,"alcohol":alcohol,"clinical_notes":notes}
