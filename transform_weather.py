import json
import pandas as pd

def transform_weather_data():
    with open("data/raw_weather.json", "r") as f:
        data = json.load(f)

    weather = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "cloudiness": data["clouds"]["all"],
        "weather": data["weather"][0]["main"]
    }

    df = pd.DataFrame([weather])

    df.to_csv("data/clean_weather.csv", index=False)

    print("✅ Weather data transformed successfully")
    return df


if __name__ == "__main__":
    transform_weather_data()