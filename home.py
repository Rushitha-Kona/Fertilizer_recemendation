import streamlit as st
import base64

import os
import pickle

# Base directory = root of your repo
BASE_DIR = os.path.dirname(__file__)  # home.py is in root

def load_pickle(filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "rb") as f:
        return pickle.load(f)

# Function to encode image
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Convert your image
img_base64 = get_base64("f_rec.jpg")
# Page Config
st.set_page_config(page_title="Fertilizer Recommendation System", layout="wide", initial_sidebar_state="collapsed")

# Hide sidebar completely
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

# --- TOP RIGHT BUTTON ---
st.markdown(
    """
    <div style="display: flex; justify-content: flex-end; margin-top: -40px;">
        <a href="/prediction" target="_self">
            <button style="background-color: #4CAF50; color: white; padding: 10px 20px; 
                           border: none; border-radius: 5px; cursor: pointer; font-size: 16px;">
                🚀 Predict
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="
        background: linear-gradient(rgba(0,128,0,0.3), rgba(0,128,0,0.3)),
        url('data:image/jpg;base64,{img_base64}') center/cover no-repeat;
        padding: 60px;
        height: 300px;
        border-radius: 10px;
        text-align: center;">
        <h1 style="color:white; text-align:center;">🌾 Fertilizer Recommendation System</h1>
        <p style="color:white;font-size:18px; text-align:center;">
            Harness the power of machine learning to get precise fertilizer recommendations tailored to your soil conditions, crop type, and environmental factors.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# --- FEATURES SECTION ---
st.markdown(
    """
    <h2 style='text-align: center; color: #1b4332;'>Why Choose Our System?</h2>
    <p style='text-align: center; font-size: 18px; color: #4a4a4a;'>
        Our AI-powered system considers multiple factors to provide accurate, science-based fertilizer recommendations
    </p>
    """,
    unsafe_allow_html=True
)

# Three Columns with equal height boxes
col1, col2, col3 = st.columns(3)
feature_box_style = """
    background-color:white; border: 1px solid #e0e0e0; border-radius:12px; 
    padding:20px; text-align:center; box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    min-height: 250px; height: 250px; display: flex; flex-direction: column; justify-content: center;
"""

with col1:
    st.markdown(
        f"""
        <div style="{feature_box_style}">
            <div style="font-size: 35px; color: #4CAF50;">🎯</div>
            <h4 style="color:#1b4332;">Precision Agriculture</h4>
            <p style="color:#4a4a4a; font-size:15px;">
                Get fertilizer recommendations tailored to your specific soil type, crop requirements, and environmental conditions.
            </p>
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div style="{feature_box_style}">
            <div style="font-size: 35px; color: #4CAF50;">📊</div>
            <h4 style="color:#1b4332;">Data-Driven Insights</h4>
            <p style="color:#4a4a4a; font-size:15px;">
                Powered by machine learning algorithms trained on extensive agricultural data for reliable and accurate predictions.
            </p>
        </div>
        """, unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div style="{feature_box_style}">
            <div style="font-size: 35px; color: #4CAF50;">⚡</div>
            <h4 style="color:#1b4332;">Quick Results</h4>
            <p style="color:#4a4a4a; font-size:15px;">
                Get instant fertilizer recommendations with just a few clicks. No waiting, no complex calculations required.
            </p>
        </div>
        """, unsafe_allow_html=True
    )

# Divider
st.write("---")

# --- HOW TO USE THE SYSTEM SECTION ---
st.markdown('<h2 style="text-align:center;">📝 How to Use the System</h2>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center;">Follow these simple steps to get your personalized fertilizer recommendation</div>', unsafe_allow_html=True)

step1, step2, step3, step4 = st.columns(4)
howto_box_style = """
    background-color:white; border: 1px solid #e0e0e0; border-radius:12px; 
    padding:20px; text-align:center; box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    min-height: 200px; height: 200px; display: flex; flex-direction: column; justify-content: center;
"""

with step1:
    st.markdown(
        f"""
        <div style="{howto_box_style}">
            <div style="font-size: 30px; color: #4CAF50;">1</div>
            <h4 style="color:#1b4332;">Environment Data</h4>
            <p style="color:#4a4a4a; font-size:15px;">
                🌡️ Enter temperature, humidity, and soil moisture levels
            </p>
        </div>
        """, unsafe_allow_html=True
    )

with step2:
    st.markdown(
        f"""
        <div style="{howto_box_style}">
            <div style="font-size: 30px; color: #4CAF50;">2</div>
            <h4 style="color:#1b4332;">Soil & Crop</h4>
            <p style="color:#4a4a4a; font-size:15px;">
                🪨 Select your soil type and the crop you want to grow
            </p>
        </div>
        """, unsafe_allow_html=True
    )

with step3:
    st.markdown(
        f"""
        <div style="{howto_box_style}">
            <div style="font-size: 30px; color: #4CAF50;">3</div>
            <h4 style="color:#1b4332;">NPK Levels</h4>
            <p style="color:#4a4a4a; font-size:15px;">
                🧪 Input current nitrogen, phosphorous, and potassium levels
            </p>
        </div>
        """, unsafe_allow_html=True
    )

with step4:
    st.markdown(
        f"""
        <div style="{howto_box_style}">
            <div style="font-size: 30px; color: #4CAF50;">4</div>
            <h4 style="color:#1b4332;">Get Results</h4>
            <p style="color:#4a4a4a; font-size:15px;">
                📄 Receive your personalized fertilizer recommendation instantly
            </p>
        </div>
        """, unsafe_allow_html=True
    )

st.write("---")

# --- BOTTOM BUTTON ---
st.markdown(
    """
    <div style="text-align: center; margin-top: 20px;">
        <a href="/prediction" target="_self">
            <button style="background-color: #4CAF50; color: white; padding: 12px 25px; 
                           border: none; border-radius: 8px; cursor: pointer; font-size: 18px;">
                🌿 Try It Now
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
