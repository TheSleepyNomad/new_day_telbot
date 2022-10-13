from dataclasses import dataclass
from datetime import datetime
from enum import Enum



class WeatherType(str, Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"

@dataclass(frozen=True)
class UserCoordinates:
    """
    temporary dataclass for storaging user location
    """
    longitude: float
    latitude: float


@dataclass(frozen=True)
class Weather:
    """
    temporary dataclass for storaging weather data
    """
    temperature: float
    # weather_type: WeatherType
    # sunrise: datetime
    # sunset: datetime
    city: str

