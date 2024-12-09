import requests
import pandas as pd
from datetime import datetime

# WeatherStack API details
API_KEY = "10f7a24f80f05c791af281bfa9d4aa91"
BASE_URL = "http://api.weatherstack.com/current"

def fetch_weather(cities=["London", "Singapore", "Shanghai"]):
    data_list = []
    for city in cities:
        params = {
            "access_key": API_KEY,
            "query": city
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            if "current" in data:
                weather = {
                    "City": city,
                    "Temperature": data["current"]["temperature"],
                    "Humidity": data["current"]["humidity"],
                    "Wind Speed": data["current"]["wind_speed"],
                    "Weather Condition": data["current"]["weather_descriptions"][0],
                    "Date": datetime.now().strftime("%Y-%m-%d"),
                    "Time": datetime.now().strftime("%H:%M:%S")
                }
                data_list.append(weather)
            else:
                print(f"Error: No weather data for {city}")
        else:
            print(f"Error: {response.status_code} for city {city}")
    return data_list

def save_weather_data(filename="raw_data.csv"):
    cities = ["London", "Singapore", "Shanghai"]
    weather_data = fetch_weather(cities)
    if weather_data:
        df = pd.DataFrame(weather_data)
        df.to_csv(filename, index=False, mode='a', header=not pd.io.common.file_exists(filename))
        print(f"Weather data saved to {filename}")

# Example Usage
if __name__ == "__main__":
    save_weather_data()
