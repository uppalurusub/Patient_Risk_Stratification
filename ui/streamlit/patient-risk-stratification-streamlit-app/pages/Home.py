import streamlit as st
from components.sidebar import render as sidebar
from components.request_form import render
from components.response_view import show
from api.client import predict
st.set_page_config(page_title="Patient Risk Prediction",page_icon="🏥",layout="wide")
sidebar()
st.title("🏥 AI Patient Risk Prediction System")
payload=render()
if st.button("🔍 Predict Risk",use_container_width=True):
    with st.spinner("Predicting..."):
        try:
            r=predict(payload)
            if r.status_code==200:
                show(r.json())
            else:
                st.error(r.text)
        except Exception as e:
            st.exception(e)
