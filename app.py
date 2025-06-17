import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ---------- Custom CSS Styling ----------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Quicksand', sans-serif;
        background: linear-gradient(to right, #D2F1E4, #E3F2FD);  /* Pastel green-blue */
        color: #2F4F4F;
        transition: background 0.6s ease-in-out;
    }

    .main {
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 24px rgba(0,0,0,0.1);
        transition: all 0.5s ease;
        animation: fadeIn 1s ease-in-out;
    }

    h1, h2, h3 {
        color: #3A9D8F;
        transition: color 0.3s ease;
    }

    h1:hover, h2:hover {
        color: #50C2A9;
        transform: scale(1.02);
    }

    input[type="number"] {
        background-color: #ffffff !important;
        border: 1px solid #B5EAD7 !important;
        border-radius: 10px;
        padding: 8px;
        transition: box-shadow 0.3s ease;
    }

    input[type="number"]:focus {
        box-shadow: 0 0 10px #76D7C4;
    }

    button {
        border-radius: 12px !important;
        background: linear-gradient(to right, #57CFB9, #A5DEE4) !important;
        color: black !important;
        font-weight: bold;
        transition: all 0.3s ease-in-out;
    }

    .stButton > button:hover {
        background: #3FB7A7 !important;
        transform: scale(1.05);
    }

    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(15px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# 🏷️ App Title
st.title("🔌 Energy Consumption Predictor")
st.subheader("Smarter Energy | Greener Planet")

st.markdown("""
Welcome to the **Energy Consumption Predictor** app!  
Enter the environmental conditions below to estimate appliance energy consumption.

💡 *Model powered by XGBoost*
""")

# ✅ Load the trained model
try:
    model = joblib.load("xgboost_energy_model.pkl")
except FileNotFoundError:
    st.error("🚫 Model file not found! Make sure 'xgboost_energy_model.pkl' is in the same directory.")
    st.stop()

# 🧮 Input fields using a form
st.markdown("### 🔍 Input Environmental Features")
with st.form("predict_form"):
    T1 = st.number_input("🌡️ Temperature in Kitchen (T1)", value=20.0)
    RH_1 = st.number_input("💧 Humidity in Kitchen (RH_1)", value=40.0)
    T2 = st.number_input("🌡️ Temperature in Living Room (T2)", value=21.0)
    RH_2 = st.number_input("💧 Humidity in Living Room (RH_2)", value=45.0)
    T_out = st.number_input("🌤️ Outside Temperature (T_out)", value=10.0)
    RH_out = st.number_input("💧 Outside Humidity (RH_out)", value=55.0)
    Press_mm_hg = st.number_input("📉 Pressure (Press_mm_hg)", value=760.0)
    Visibility = st.number_input("🌫️ Visibility", value=40.0)
    Windspeed = st.number_input("💨 Windspeed", value=5.0)

    submitted = st.form_submit_button("🔮 Predict")

# 🔮 Predict and show result
if submitted:
    input_data = np.array([[T1, RH_1, T2, RH_2, T_out, RH_out, Press_mm_hg, Visibility, Windspeed]])
    prediction = model.predict(input_data)[0]
    st.success(f"⚡ Predicted Energy Usage: **{prediction:.2f} Wh**")
