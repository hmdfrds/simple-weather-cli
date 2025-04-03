import requests
from dotenv import load_dotenv
import os

load_dotenv(".env")
API_KEY = os.environ.get("OPENWEATHER_API_KEY")
if not API_KEY:
    print("Error: OPENWEATHER_API_KEY not set. Please set it in your environment.")
    exit(1)

BASE_URL = f"http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&unites=metric"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            city = data.get("name")
            temp = data.get("main", {}).get("temp")
            feels_like = data.get("main",{}).get("feels_like")
            description = data.get("weather",[{}])[0].get("description")
            humidity = data.get("main", {}).get("humidity")
            wind_speed = data.get("wind", {}).get("speed")

            print(f"Weather in {city}:")
            print("-" *25)
            print(f"Temperature:    {temp}C")
            print(f"Feels Like: {feels_like}")
            print(f"Description:    {description}")
            print(f"Humidity:   {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s)")

        elif response.status_code== 404:
            print("Error: City not found. Please check the spelling.")
        elif response.status_code == 401:
            print("Error: Authentication failed. Please check your API key.")
        else:
            print("Error: Could not retrieve weather data. Check your connection or the API service.")
    except requests.exceptions.RequestException:
        print("Error: Could not retrieve weather data. Check your connection or the API service.")


if __name__ == "__main__":
    print("--- Simple Weather Reporter ---")
    city = input("Enter city name: ")
    if not city.strip():
        print("Error: No city name provided.")
    else:
        get_weather(city)

        