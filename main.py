from http.client import responses

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import requests

##Weather_location_ask=input ("Search City")
##print ()
##import requests
##url =f"https://api.openweathermap.org/data/3.0/onecall?lat"
##print(url)
##response = requests.get("https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}")

##secret = st.secrets["my_secret"]
##st.text(f"my secret is {secret}, dont tell anyone")

##st.markdown("""
# Title   
## Subtitle

##- bullet 1
##- bullet 2
##- bullet 3

##>Amazing Quote
##""")

# Create a radio button widget for selecting the plot type
##plot_type = st.radio("Which plot do you want to see?", ["Seaborn", "Plotly"])

# Load the dataset
##df = sns.load_dataset("penguins")

##if plot_type == "Seaborn":
    # Create a Seaborn scatter plot
##    fig, ax = plt.subplots()
##    sns.scatterplot(data=df, x="flipper_length_mm", y="bill_length_mm", hue="species", ax=ax)
##    st.pyplot(fig)
##elif plot_type == "Plotly":
##    # Create a Plotly scatter plot
##    fig = px.scatter(
##        df,
##        x="flipper_length_mm",
##        y="bill_length_mm",
##        color="species",
##        title="Penguins: Flipper Length vs Bill Length"
##    )
##    st.plotly_chart(fig)



# Replace with your OpenWeatherMap API key
API_KEY = "c22111555d8dbc69c4700a23bfb0eeea"


def get_weather(city_name):
    base_url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric" , # Use 'metric' for Celsius, 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def display_weather(data):
    if data:
        city = data.get("name")
        country = data["sys"].get("country")
        temp = data["main"].get("temp")
        temp_min = data["main"].get("temp_min")
        temp_max = data["main"].get("temp_max")
        humidity = data["main"].get( "humidity")

        weather = data["weather"][0].get("description")

        print(f"\nWeather in {city}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"min Temperature: {temp_min}°C")
        print(f"max Temperature: {temp_max}°C")
        print(f"Condition: {weather.capitalize()}")
        print(f"Humidity: {humidity}")

    else:
        print("Could not fetch weather data. Please try again.")


def main():
    city_name = input("Enter the name of the city: ")
    weather_data = get_weather(city_name)
    display_weather(weather_data)


if __name__ == "__main__":
    main()


