import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ==============================
# Load Models and Tokenizer
# ==============================
rf = joblib.load("rf_model.pkl")
tokenizer = joblib.load("tokenizer.pkl")
model_lstm = load_model("lstm_model.h5")

# ==============================
# Streamlit Page Config
# ==============================
st.set_page_config(page_title="Fake Job Detection", page_icon="🕵️", layout="wide")

st.title("🕵️ Fake Job Posting Detector")
st.write("Enter job details below to check if the job post is **Fake or Legitimate.**")

# ==============================
# Input Section
# ==============================
col1, col2 = st.columns(2)

with col1:
    title = st.text_input("📄 Job Title", "Environmental Technician I")
    description = st.text_area("📝 Job Description")
    location = st.text_input("📍 Location (e.g., US, TX, Houston)", "US, TX, Houston")
    department = st.text_input("🏢 Department", "")
    employment_type = st.selectbox("💼 Employment Type", ["Full-time", "Part-time", "Contract", "Temporary", "Other"])
    required_experience = st.text_input("🎓 Required Experience", "")
    required_education = st.text_input("🎯 Required Education", "")
    industry = st.text_input("🏭 Industry", "Oil & Energy")
    function = st.text_input("🧩 Job Function", "")

with col2:
    salary_range = st.text_input("💰 Salary Range (e.g., 40000-60000)", "")
    telecommuting = st.selectbox("💻 Remote Job?", ["Yes", "No"])
    has_company_logo = st.selectbox("🏢 Company Logo Present?", ["Yes", "No"])
    has_questions = st.selectbox("❓ Includes Screening Questions?", ["Yes", "No"])
    description_length = st.number_input("🧠 Description Length", value=0)
    requirements_length = st.number_input("📋 Requirements Length", value=0)
    benefits_length = st.number_input("💵 Benefits Length", value=0)
    salary_range_missing = st.selectbox("🚫 Salary Range Missing?", ["Yes", "No"])
    department_missing = st.selectbox("🚫 Department Missing?", ["Yes", "No"])

# ==============================
# Prediction Button
# ==============================
if st.button("🔍 Predict Fake or Legitimate"):
    # ------------------------
    # Preprocess structured data
    # ------------------------
    try:
        salary_min, salary_max = salary_range.split('-')
        salary_min, salary_max = float(salary_min), float(salary_max)
        salary_avg = (salary_min + salary_max) / 2
    except:
        salary_min, salary_max, salary_avg = 0, 0, 0

    # Convert categorical to numeric
    telecommuting_val = 1 if telecommuting == "Yes" else 0
    has_logo_val = 1 if has_company_logo == "Yes" else 0
    has_questions_val = 1 if has_questions == "Yes" else 0
    salary_missing_val = 1 if salary_range_missing == "Yes" else 0
    dept_missing_val = 1 if department_missing == "Yes" else 0

    # Structured feature array (18 features)
    X_struct = np.array([[
        salary_min, salary_max, salary_avg,
        description_length, requirements_length, benefits_length,
        salary_missing_val, dept_missing_val,
        telecommuting_val, has_logo_val, has_questions_val,
        # For categorical values, simple placeholder encoding (since actual encoders aren’t loaded)
        len(location), len(department), len(employment_type),
        len(required_experience), len(required_education),
        len(industry)
    ]])

    # ------------------------
    # Text preprocessing for LSTM
    # ------------------------
    seq = tokenizer.texts_to_sequences([description])
    seq_padded = pad_sequences(seq, maxlen=200)
    lstm_prob = model_lstm.predict(seq_padded).flatten()[0]

    # ------------------------
    # Random Forest Prediction
    # ------------------------
    rf_prob = rf.predict_proba(X_struct)[:, 1][0]

    # ------------------------
    # Hybrid Ensemble Prediction
    # ------------------------
    hybrid_prob = (0.6 * rf_prob) + (0.4 * lstm_prob)
    prediction = "🚨 Fake Job Posting" if hybrid_prob >= 0.5 else "✅ Legitimate Job Posting"

    # ------------------------
    # Display Results
    # ------------------------
    st.subheader(prediction)
    st.write(f"**Prediction Confidence:** {hybrid_prob:.2f}")

    if hybrid_prob >= 0.5:
        st.warning("⚠️ This posting shows signs of fraud. Review carefully before applying.")
    else:
        st.success("✅ This posting appears legitimate — but stay alert for red flags.")
