from handlers.handler import Handler
from config.config import KEYBOARD
from temp.temp_data import UserCoordinates

class HandlerDataCollecting(Handler):
    """
    This handler response for data collecting from user and api end points
    Like example - user gps location or json data from weather api
    """

    def __init__(self, bot):
        super().__init__(bot)


    def get_user_location(self, message) -> UserCoordinates:
        """
        get gps location from user
        """
        self.bot.send_message(message.chat.id, f"{message.location.longitude} and {message.location.latitude}")
        return UserCoordinates(longitude=message.location.longitude, latitude=message.location.latitude)

    def handle(self) -> None:

        @self.bot.message_handler(content_types=["location"])
        def handle(message) -> None:
            coordinates = self.get_user_location(message)
            print(coordinates.longitude, coordinates.latitude)