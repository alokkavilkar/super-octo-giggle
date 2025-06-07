from .utils import fetch_weather_data

def analyze_weather(city: str) -> dict:
    data = fetch_weather_data(city)
    if not data:
        raise ValueError("No data received")
    avg_temp = sum(data['temperatures']) / len(data['temperatures'])
    return {"city": city, "average_temperature": avg_temp}

