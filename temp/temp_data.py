from dataclasses import dataclass
from datetime import datetime
from typing import TypeAlias
from enum import Enum


Celsius: TypeAlias = int

class WeatherType(str, Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"

@dataclass(slots=True, frozen=True)
class UserCoordiates:
    """
    temporary dataclass for storaging user location
    """
    longitude: float
    latitude: float


@dataclass(slots=True, frozen=True)
class Weather:
    """
    temporary dataclass for storaging weather data
    """
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str

