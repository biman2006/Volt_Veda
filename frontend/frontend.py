import streamlit as st
import requests 

st.set_page_config(page_title="VoltVeda AI", page_icon="🔋", layout="centered")
st.title("🔋Battery Health Predictor")
st.write("Enter your smartphone usage & charging details to predict battery health percentage.")
FASTAPI_URL="https://voltveda-production.up.railway.app/predict"




with st.form("battery_form"):

    st.subheader("📱 Device Information")
    device_age_month=st.number_input("Device Age(months)", min_value=0, max_value=1000, value=18)
    battery_capacity_mah=st.number_input("Battery Capacity (mAh)", min_value=1000,max_value=100000, value=5000)


    st.subheader("⚡ Usage & Charging Habits")
    avg_screen_on_hours_per_day=st.number_input("Avg Screen time (hours/day)", min_value=0.0,max_value=24.0,value=6.0)
    avg_charging_cycles_per_week=st.number_input("Avg Charging Cycles (per week)", min_value=0.0,max_value=50.0, value=10.0)
    avg_battery_temp_celsius=st.number_input("Avg Battery Temperature (°C)", min_value=0.0, max_value=60.0, value=34.0)
    fast_charging_usage_percent = st.slider("Fast Charging Usage (%)", min_value=0, max_value=100, value=60)
    overnight_charging_freq_per_week = st.number_input("Overnight Charging Frequency (per week)", min_value=0.0, max_value=14.0, value=4.0)

    gaming_hours_per_week = st.number_input("Gaming Hours (per week)", min_value=0.0, max_value=100.0, value=12.0)
    video_streaming_hours_per_week = st.number_input("Video Streaming Hours (per week)", min_value=0.0, max_value=100.0, value=8.0)

    charging_habit_score = st.slider("Charging Habit Score (0-10)", min_value=0.0, max_value=10.0, value=7.5)
    usage_intensity_score = st.slider("Usage Intensity Score (0-10)", min_value=0.0, max_value=10.0, value=8.2)
    thermal_stress_index = st.slider("Thermal Stress Index (0-10)", min_value=0.0, max_value=10.0, value=6.8)

    st.subheader("📶 Categorical Features")
    background_app_usage_level = st.selectbox("Background App Usage Level", ["Low", "Medium", "High"])
    signal_strength_avg = st.selectbox("Signal Strength Average", ['Medium', 'High', 'Low'])

    submit = st.form_submit_button("🔍 Predict Battery Health")





if submit: 
    input_data={
        "device_age_months": device_age_month,
        "battery_capacity_mah": battery_capacity_mah,
        "avg_screen_on_hours_per_day": avg_screen_on_hours_per_day,
        "avg_charging_cycles_per_week": avg_charging_cycles_per_week,
        "avg_battery_temp_celsius": avg_battery_temp_celsius,
        "fast_charging_usage_percent": fast_charging_usage_percent,
        "overnight_charging_freq_per_week": overnight_charging_freq_per_week,
        "gaming_hours_per_week": gaming_hours_per_week,
        "video_streaming_hours_per_week": video_streaming_hours_per_week,
        "charging_habit_score": charging_habit_score,
        "usage_intensity_score": usage_intensity_score,
        "thermal_stress_index": thermal_stress_index,
        "background_app_usage_level": background_app_usage_level,
        "signal_strength_avg": signal_strength_avg

    }
    try:
        response=requests.post(FASTAPI_URL, json=input_data)
        if response.status_code==200:
            result=response.json()


            st.success("✅ Prediction Successful!")

            st.metric("Predicted Battery Health (%)", result["predicted_battery_health_percent"])
            st.write("### 🟢 Health Status:", result["health_status"])
            st.info(result["message"])

            prediction=result["predicted_battery_health_percent"]

            st.write(f"🔋 Battery Health: **{prediction:.2f}%**")

            progress_value=max(0,min(100,int(prediction)))
            st.progress(progress_value)


        else:
            st.error(f"❌ API Error: {response.status_code}")
            st.write(response.text)



    except Exception as e:
        st.error("❌ Could not connect to FastAPI server.")
        st.write("Make sure FastAPI is running at: http://127.0.0.1:8000")
        st.write("Error:", str(e))





