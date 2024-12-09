import streamlit as st
import requests

st.title("Weather Prediction Application")

temperature = st.number_input("Temperature (°C)", min_value=-50.0, max_value=50.0)
wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=150.0)

if st.button("Predict"):
    data = {"temperature": temperature, "wind_speed": wind_speed}
    # Change the URL to the new port (5001)
    response = requests.post("http://localhost:5001/predict", json=data)
    
    if response.status_code == 200:
        prediction = response.json()["predicted_humidity"]
        st.write(f"Predicted Humidity: {prediction:.2f}%")
    else:
        st.error("Error in prediction")
