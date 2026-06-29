import streamlit as st
import numpy as np
import pandas as pd

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="AI Disease Predictor",
    page_icon="🩺",
    layout="wide"
)

# ----------------------------------
# CUSTOM CSS
# ----------------------------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
    135deg,
    #0f172a,
    #1e3a8a,
    #7c3aed
    );
}

.main-title{
    font-size:60px;
    font-weight:bold;
    text-align:center;
    color:white;
}

.card{
    background:rgba(255,255,255,0.12);
    padding:20px;
    border-radius:20px;
    backdrop-filter:blur(10px);
    text-align:center;
    box-shadow:0px 8px 25px rgba(0,0,0,0.3);
}

.result-card{
    background:rgba(0,255,200,0.15);
    padding:30px;
    border-radius:20px;
    text-align:center;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# TITLE
# ----------------------------------

st.markdown(
"""
<h1 class="main-title">
🩺 AI Disease Prediction System
</h1>
""",
unsafe_allow_html=True
)

st.write("")

# ----------------------------------
# SIDEBAR
# ----------------------------------

st.sidebar.title("⚙️ Patient Information")

age = st.sidebar.slider(
    "👤 Age",
    1,
    100,
    25
)

gender = st.sidebar.selectbox(
    "🚻 Gender",
    ["Male", "Female"]
)

fever = st.sidebar.selectbox(
    "🌡 Fever",
    ["No", "Yes"]
)

cough = st.sidebar.selectbox(
    "🤧 Cough",
    ["No", "Yes"]
)

fatigue = st.sidebar.selectbox(
    "😴 Fatigue",
    ["No", "Yes"]
)

blood_pressure = st.sidebar.slider(
    "🩸 Blood Pressure (mmHg)",
    50,
    250,
    120
)

cholesterol = st.sidebar.slider(
    "🧪 Cholesterol Level (mg/dL)",
    50,
    400,
    180
)

difficulty_breathing = st.sidebar.selectbox(
    "😮‍💨 Difficulty Breathing",
    ["No", "Yes"]
)

# ----------------------------------
# DASHBOARD
# ----------------------------------

st.subheader("📋 Patient Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Age", age)

with col2:
    st.metric("Blood Pressure", blood_pressure)

with col3:
    st.metric("Cholesterol", cholesterol)

with col4:
    st.metric("Gender", gender)

col5, col6, col7, col8 = st.columns(4)

with col5:
    st.metric("Fever", fever)

with col6:
    st.metric("Cough", cough)

with col7:
    st.metric("Fatigue", fatigue)

with col8:
    st.metric("Breathing", difficulty_breathing)

# ----------------------------------
# ENCODING
# ----------------------------------

gender_val = 1 if gender == "Male" else 0
fever_val = 1 if fever == "Yes" else 0
cough_val = 1 if cough == "Yes" else 0
fatigue_val = 1 if fatigue == "Yes" else 0
difficulty_breathing_val = 1 if difficulty_breathing == "Yes" else 0

# ----------------------------------
# PREDICT BUTTON
# ----------------------------------

if st.button("🚀 Predict Disease"):

    features = np.array([
        [
            age,
            gender_val,
            fever_val,
            cough_val,
            fatigue_val,
            blood_pressure,
            cholesterol,
            difficulty_breathing_val
        ]
    ])

    # ----------------------------------
    # CONNECT YOUR MODEL HERE
    # ----------------------------------

    # prediction = model.predict(features)[0]

    # Demo Output
    prediction = np.random.choice(
        [
            "Flu",
            "Common Cold",
            "Viral Fever",
            "Asthma",
            "Pneumonia",
            "Healthy"
        ]
    )

    probability = np.random.randint(80, 99)

    st.markdown(
        f"""
        <div class="result-card">
        <h2>🧬 Predicted Disease</h2>
        <h1>{prediction}</h1>
        <h3>Confidence: {probability}%</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success("Prediction Completed Successfully")

# ----------------------------------
# FOOTER
# ----------------------------------

st.write("")
st.write("")

st.markdown(
"""
<center>
<h4 style='color:white'>
Made with ❤️ using Machine Learning & Streamlit
</h4>
</center>
""",
unsafe_allow_html=True
)