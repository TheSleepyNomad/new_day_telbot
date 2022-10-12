from emoji import emojize
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# telegram bot config
TELEGRAM_BOT_API_KEY = getenv('API_KEY')

# buttons for keyboard
KEYBOARD = {
    'ADMIN_PANEL': emojize('⚙️ Админ панель'),
    'LOCATION': emojize(':globe_with_meridians: Задать координаты'),
    }

# https://openweathermap.org/ API
OPEN_WEATHER_API_KEY = getenv('OPENWEATHER_API_KEY')
# url template for current weather request
CURRENT_WEATHER_URL = (
    'https://api.openweathermap.org/data/2.5/weather?'
    'lat={latitude}&lon={longitude}&lang=ru&'
    '&appid='+ OPEN_WEATHER_API_KEY + '&units=metric'
)
# url template for 5 days weather request
FIVE_DAYS_FORECAST_URL = (
    'https://api.openweathermap.org/data/2.5/forecast?'
    'lat={latitude}&lon={longitude}&lang=ru&'
    '&appid='+ OPEN_WEATHER_API_KEY + '&units=metric'
)

# other
APP_VERSION = '0.0.1'
CREATE_BY = 'Ilya "TheSleepyNomad" Pankov'