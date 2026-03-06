import requests
import json
from config import API_KEY, CITY, UNITS

def extract_weather_data():
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY}&appid={API_KEY}&units={UNITS}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"API request failed: {response.status_code}")

    data = response.json()

    with open("data/raw_weather.json", "w") as f:
        json.dump(data, f, indent=4)

    print("✅ Weather data extracted successfully")
    return data


if __name__ == "__main__":
    extract_weather_data()