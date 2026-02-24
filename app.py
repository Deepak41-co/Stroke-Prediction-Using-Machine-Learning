import streamlit as st
import joblib
import pandas as pd

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Stroke Risk Predictor",
    page_icon="🧠",
    layout="centered"
)

# ---------------- Load Model ----------------
model = joblib.load("stroke_prediction_model.pkl")

# ---------------- Title ----------------
st.title("🧠 Stroke Risk Prediction App")
st.write("Enter patient details below:")
st.markdown("---")

# ---------------- Input Fields ----------------

gender = st.selectbox(
    "Gender",
    ["Select Gender", "Male", "Female"]
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120
)

hypertension = st.selectbox(
    "Hypertension",
    ["Select Yes or No", "Yes", "No"]
)

heart_disease = st.selectbox(
    "Heart Disease",
    ["Select Yes or No", "Yes", "No"]
)

avg_glucose_level = st.number_input(
    "Average Glucose Level",
    min_value=0.0
)

bmi = st.number_input(
    "BMI",
    min_value=0.0
)

st.markdown("---")

# ---------------- Predict Button ----------------
predict = st.button("🔍 Predict Stroke Risk", use_container_width=True)

if predict:

    # ---------------- Validation ----------------
    if gender == "Select Gender":
        st.warning("⚠ Please select Gender before predicting.")
    elif hypertension == "Select Yes or No":
        st.warning("⚠ Please select Hypertension before predicting.")
    elif heart_disease == "Select Yes or No":
        st.warning("⚠ Please select Heart Disease before predicting.")
    else:

        # Convert categorical inputs
        hypertension_value = 1 if hypertension == "Yes" else 0
        heart_disease_value = 1 if heart_disease == "Yes" else 0

        input_data = pd.DataFrame([{
            "gender": gender,
            "age": age,
            "hypertension": hypertension_value,
            "heart_disease": heart_disease_value,
            "avg_glucose_level": avg_glucose_level,
            "bmi": bmi
        }])

        # ---------------- Prediction ----------------
        with st.spinner("Analyzing patient data..."):
            prediction = model.predict(input_data)[0]

            # Safe probability extraction
            stroke_index = list(model.classes_).index(1)
            probability = model.predict_proba(input_data)[0][stroke_index]

        # ---------------- Result Section ----------------
        st.markdown("## 📊 Prediction Result")

        st.progress(float(probability))
        st.markdown(f"### Stroke Probability: {round(probability * 100, 2)}%")

        if prediction == 1:
            st.error("⚠ High Stroke Risk Detected")
        else:
            st.success("✅ Low Stroke Risk")

        

        st.markdown("---")
