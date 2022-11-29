import time
import requests
import os

from dotenv import load_dotenv 
load_dotenv()

api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')
city_name = "Inhumas"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name


def get_weather_openweathermap():
    time.sleep(2)
    return {'temperature_kelvin': '295', 'atmospheric_pressure': '1006', 'humidity': '61', 'description': 'clear sky'}

    response = requests.get(complete_url)
    response = response.json()

    if response["cod"] != "404":
        current_temperature = response["main"]["temp"]
        current_pressure = response["main"]["pressure"]
        current_humidiy = response["main"]["humidity"]
        weather_description = response["weather"][0]["description"]

        return {
            "temperature_kelvin": str(current_temperature),
            "atmospheric_pressure": str(current_pressure),
            "humidity": str(current_humidiy),
            "description": str(weather_description)
        }

    else:
        return "City Not Found"

