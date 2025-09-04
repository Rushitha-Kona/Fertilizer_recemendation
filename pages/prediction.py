import pickle
import numpy as np
import streamlit as st
import os

# ===== Helper function to load pickle files =====
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # go up from pages/ to root

def load_pickle(filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "rb") as f:
        return pickle.load(f, encoding='latin1')

# ===== Load model and encoders =====
model = load_pickle("rf_file.pkl")
soil_enc = load_pickle("soil.pkl")
crop_enc = load_pickle("crop.pkl")
ferti_enc = load_pickle("fertilizer.pkl")

# ===== Streamlit UI =====
st.title("🌿 Fertilizer Predictor")
st.write("Enter your field conditions to get personalized fertilizer recommendations")

soil_options = ["Clayey", "Loamy", "Red", "Black", "Sandy"]
crop_options = [
    "rice", "Wheat", "Tobacco", "Sugarcane", "Pulses", "pomegranate", "Paddy",
    "Oil seeds", "Millets", "Maize", "Ground Nuts", "Cotton", "coffee",
    "watermelon", "Barley", "kidneybeans", "orange"
]

with st.form("fertilizer_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        temperature = st.number_input("🌡️ Temperature (°C)", 0, 60, 25)
        soil_type = st.selectbox("🪨 Soil Type", sorted(soil_options))
        nitrogen = st.number_input("🟦 Nitrogen (N)", 0, 150, 50)
    with col2:
        humidity = st.number_input("💧 Humidity (%)", 0, 100, 65)
        crop_type = st.selectbox("🌾 Crop Type", sorted(crop_options))
        phosphorus = st.number_input("🟨 Phosphorous (P)", 0, 100, 30)
    with col3:
        moisture = st.number_input("☔ Moisture (%)", 0, 100, 45)
        potassium = st.number_input("🟩 Potassium (K)", 0, 150, 40)

    submitted = st.form_submit_button("Predict Fertilizer")

if submitted:
    # Encode inputs
    soil_encoded = soil_enc.transform([soil_type])[0]
    crop_encoded = crop_enc.transform([crop_type])[0]

    # Prepare input
    input_data = np.array([[temperature, humidity, moisture, soil_encoded,
                            crop_encoded, nitrogen, phosphorus, potassium]])

    # Predict
    prediction = model.predict(input_data)[0]

    # Decode fertilizer
    fertilizer_name = ferti_enc.inverse_transform([prediction])[0]

    st.success(f"Recommended Fertilizer: **{fertilizer_name}** for {crop_type} crop.")
