from handlers.handler import Handler
from config.config import KEYBOARD, CURRENT_WEATHER_URL, FIVE_DAYS_FORECAST_URL
from config.messages import MESSAGES
from temp.temp_data import UserCoordinates, Weather
import requests

class HandlerDataCollecting(Handler):
    """
    This handler response for data collecting from user and api end points
    Like example - user gps location or json data from weather api
    """

    def __init__(self, bot):
        super().__init__(bot)


    def send_current_weather_forecast(self, message) -> None:
        """
        get gps location from user
        """
        # Получить данные о gps
        # get_weather
        # _get_openweather
        # _parse_openweather_json
        # отправить сообщение пользователю с данными о погоде
        self.bot.send_message(message.chat.id, MESSAGES['current_weather'],
                              parse_mode="HTML",
                              reply_markup=self.keyboard.start_menu(),)
        return UserCoordinates(longitude=message.location.longitude, latitude=message.location.latitude)


    def get_weather(self, coordinates: UserCoordinates) -> Weather:
        weather_data = self._get_openweather_response(coordinates.latitude, coordinates.longitude)
        return Weather(weather_data['main']['temp'], 'Moscow')
    

    def _get_openweather_response(self, latitude: float, longitude: float) -> str:
        api_url = CURRENT_WEATHER_URL.format(latitude=latitude, 
                                            longitude=longitude)
        # json object
        response = requests.get(api_url).json()
        return response


    def handle(self) -> None:

        @self.bot.message_handler(content_types=["location"])
        def handle(message) -> None:
            self.send_current_weather_forecast(message)