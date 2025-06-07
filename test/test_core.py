import pytest
from weather_analyzer.core import analyze_weather

def test_analyze_weather_valid_city():
    result = analyze_weather("New York")
    assert result["average_temperature"] == pytest.approx(68.75)

def test_analyze_weather_invalid_city():
    with pytest.raises(ValueError):
        analyze_weather("Unknown City")
