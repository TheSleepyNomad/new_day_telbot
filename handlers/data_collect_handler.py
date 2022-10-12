from handlers.handler import Handler
from config.config import KEYBOARD


class HandlerDataCollecting(Handler):
    """
    This handler response for data collecting from user and api end points
    Like example - user gps location or json data from weather api
    """

    def __init__(self, bot):
        super().__init__(bot)


    def get_user_location(self, message) -> None:
        """
        get gps location from user
        """
        self.bot.send_message(message.chat.id, "В будущем здесь будет функционал проверки записи на урок")


    def handle(self) -> None:

        @self.bot.message_handler(content_types=["location"])
        def handle(message) -> None:
            print(message.location.longitude, message.location.latitude)
            self.get_user_location(message)