import joblib
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler

# **Set Page Config (Placed at Start)**
st.set_page_config(page_title="Calorie Prediction App", page_icon="🔥", layout="wide")

# **Sidebar for About & Social Links**
st.sidebar.image("logo.png", width=150)
st.sidebar.title("📌 About the Project")
st.sidebar.write("This app predicts calorie expenditure based on activity data using an AI-powered Random Forest model. 🚀")

# **Add Creator's Name**
st.sidebar.markdown("**👤 Created by:** Rupak C. Jogi")  

# **Social Links (Smaller LinkedIn & GitHub Icons)**
st.sidebar.markdown("""
<a href="https://www.linkedin.com/in/rupak-jogi-py-aiml">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="30">
</a>
<a href="https://github.com/RCJ360">
    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="30">
</a>
""", unsafe_allow_html=True)

# **Load Model & Scaler with Corrected Paths**
rf_model = joblib.load("model.pkl", mmap_mode="r")
scaler = joblib.load("scaler.pkl")

# **App Title & Description**
st.image("logo.png", width=150)  
st.title("🔥 AI-Powered Calorie Prediction App")
st.write("Enter your details below to estimate your calorie expenditure based on activity and heart rate!")

# **User Input Section**
name = st.text_input("Your Name")
age = st.slider("Age", min_value=18, max_value=80, value=25)
gender = st.selectbox("Gender", ["Male", "Female"])
height = st.slider("Height (cm)", min_value=140, max_value=220, value=170)
weight = st.slider("Weight (kg)", min_value=40, max_value=150, value=70)
duration = st.slider("Exercise Duration (minutes)", min_value=5, max_value=120, value=30)
heart_rate = st.slider("Heart Rate (bpm)", min_value=50, max_value=180, value=100)
body_temp = st.slider("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=37.5)

# **Convert Gender to Numeric**
Sex_Male = 1 if gender == "Male" else 0

# **Feature Engineering**
sex_duration = duration * Sex_Male
weight_heart_rate = weight * heart_rate

# **Create input DataFrame (Excluding Sex_Male for Scaling)**
user_input = pd.DataFrame([[age, height, weight, duration, heart_rate, body_temp, sex_duration, weight_heart_rate]],
                          columns=["Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp", "Sex_Duration", "Weight_HeartRate"])

# **Apply Scaling**
user_input_scaled = scaler.transform(user_input)

# **Convert back to DataFrame & Add Sex_Male**
user_input_scaled = pd.DataFrame(user_input_scaled, columns=user_input.columns)
user_input_scaled["Sex_Male"] = Sex_Male  

# **Reorder Columns to Match Training Features**
user_input_scaled = user_input_scaled[["Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp", "Sex_Male", "Sex_Duration", "Weight_HeartRate"]]

# **Prediction**
if st.button("Predict Calories 🔥"):
    calories_pred = rf_model.predict(user_input_scaled)[0]
    calories_pred = max(calories_pred, 0)  

    # **Display Output with Motivation**
    st.success(f"🔥 {name}, based on your details, your estimated calorie expenditure is **{calories_pred:.2f} Calories!**")
    
    # **Motivation Based on Activity Level**
    if calories_pred < 150:
        st.write("🔹 Keep pushing! A little more activity could enhance your fitness.")
    elif 150 <= calories_pred <= 500:
        st.write("💪 Great job! Your workout is burning calories efficiently!")
    else:
        st.write("🔥 Incredible effort! You are truly maximizing your workouts!")

# **Footer with Background Image (Correct Path)**
st.image("background.jpg", width=800)  
st.write("🚀 Powered by AI | Developed for Fitness & Health Enthusiasts")
