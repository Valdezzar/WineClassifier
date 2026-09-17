import os

import requests
import streamlit as st


API_URL = os.getenv("API_URL", "http://localhost:8000/predict")

st.title("Wine predictor")

alcohol = st.number_input("Alcohol", min_value=0.0, value=13.05, step=0.01)
malic_acid = st.number_input("Malic acid", min_value=0.0, value=1.87, step=0.01)
color_intensity = st.number_input("Color intensity", min_value=0.0, value=4.69, step=0.01)
proline = st.number_input("Proline", min_value=0.0, value=673.5, step=0.1)

if st.button("Predict"):
    response = requests.post(
        API_URL,
        json={
            "alcohol": alcohol,
            "malic_acid": malic_acid,
            "color_intensity": color_intensity,
            "proline": proline,
        },
        timeout=10,
    )
    response.raise_for_status()
    result = response.json()
    st.write(f"{result['class_name']} ({result['class_id']})")
