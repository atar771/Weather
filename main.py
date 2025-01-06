from http.client import responses

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import requests
import pytz
import pandas as pd



##st.markdown("""
# Weather All Over The World
##""")

st.markdown(
    """
    <style>
    /* Background styling */
    .main {
        background-color: #f5f5f5; /* Light gray background */
        padding: 20px;
    }

    /* Header styling */
    h1 {
        color: #333333;
        text-align: left;
        font-family: 'Arial', sans-serif;
    }

    /* Weather card styling */
    .weather-card {
        background-color: #ffffff; /* White card */
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
        font-family: 'Arial', sans-serif;
        color: #444444;
        text-align: center;
    }

    /* Button and input styling */
    div.stButton > button {
        background-color: #007BFF; /* Bootstrap blue */
        color: white;
        border-radius: 5px;
        font-size: 12px;
        padding: 5px 15px;
        cursor: pointer;
    }

    div.stButton > button:hover {
        background-color: #0056b3; /* Darker blue on hover */
    }

    div.stTextInput > div > input {
        border-radius: 5px;
        padding: 5px 10px;  
        font-size: 16px;
        border: 1px solid #cccccc;
        
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page Title
st.markdown("<h1>🌤 Weather Around the World</h1>", unsafe_allow_html=True)



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
    # Use columns to position the input box and button side by side
    col1, col2 = st.columns([3, 1])  # Adjust the width ratios if needed

    with col1:
        city_name = st.text_input("Enter the name of the city:", label_visibility="collapsed")

    with col2:
        get_weather_btn = st.button("Get Weather")

    if get_weather_btn:
      if city_name:
        weather_data = get_weather(city_name)
        display_weather(weather_data)

if __name__ == "__main__":
    main()
