# Fetches weather data using OpenWeatherMap API
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    return f"{city}: {response['main']['temp']}°C, {response['weather'][0]['description']}"

if __name__ == "__main__":
    city = input("Enter city: ")
    api_key = "your_api_key_here"  # Replace with your API key
    print(get_weather(city, api_key))