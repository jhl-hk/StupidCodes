import os 
import dotenv
import requests

dotenv.load_dotenv()

# Environmnetal Values
URL = "http://api.weatherapi.com/v1"
API_KEY = os.getenv("WEATHER_API_KEY")

# Get Current Weather through City
def get_weather(city):
    try:
        response = requests.get(f"{URL}/current.json?key={API_KEY}&q={city}")
        response.raise_for_status()
        original_data = response.json()
        data = {
            "location": original_data["location"]["name"],
            "temperature": original_data["current"]["temp_c"],
            "condition": original_data["current"]["condition"]["text"],
            "humidity": original_data["current"]["humidity"],
            "wind_speed": original_data["current"]["wind_kph"],
            "feels_like": original_data["current"]["feelslike_c"],
        }
        print(f"Weather in {data['location']}: {data['temperature']}°C, {data['condition']}, {data['humidity']}% humidity, {data['wind_speed']} km/h wind speed, feels like {data['feels_like']}°C")
        return
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

city = input("Enter the name of the city: ")
get_weather(city)