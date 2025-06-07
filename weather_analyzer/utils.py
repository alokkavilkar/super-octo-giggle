def fetch_weather_data(city: str) -> dict:
    # Simulated response from a weather API
    dummy_data = {
        "New York": {"temperatures": [70, 72, 68, 65]},
        "London": {"temperatures": [60, 62, 59, 58]}
    }
    return dummy_data.get(city)

