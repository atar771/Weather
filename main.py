from http.client import responses

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import requests

st.markdown("""
# Weather All Over The World
""")

API_KEY = st.secrets["My_Secret"]

def get_weather(city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # Use 'metric' for Celsius, 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return None

def display_weather(data):
    if data:
        city = data.get("name")
        country = data["sys"].get("country")
        temp = data["main"].get("temp")
        temp_min = data["main"].get("temp_min")
        temp_max = data["main"].get("temp_max")
        weather = data["weather"][0].get("description")

        st.markdown(f"### Weather in {city}, {country}")
        st.write(f"**Temperature:** {temp}°C")
        st.write(f"**Minimum Temperature:** {temp_min}°C")
        st.write(f"**Maximum Temperature:** {temp_max}°C")
        st.write(f"**Condition:** {weather.capitalize()}")
    else:
        st.error("Could not fetch weather data. Please try again.")

def main():
    city_name = st.text_input("Enter the name of the city: ")
    if city_name:
        weather_data = get_weather(city_name)
        display_weather(weather_data)

if __name__ == "__main__":
    main()
