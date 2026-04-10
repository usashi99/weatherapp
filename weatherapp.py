import streamlit as st
import requests

st.title("🌦 Weather App (Live API)")

api_key = "3c3234c96f01354258cdac85aac6a32b"   # paste your API key here

city = st.text_input("Enter City Name:")

if st.button("Get Weather"):
    if city == "":
        st.warning("Please enter a city name!")
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]

            st.success(f"Weather in {city}")
            st.write("🌡 Temperature:", temp, "°C")
            st.write("💧 Humidity:", humidity, "%")
            st.write("🌥 Condition:", condition)

        else:
            st.error("City not found! Please enter a valid city name.")