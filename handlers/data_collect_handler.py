from pyexpat.errors import messages
from handlers.handler import Handler
from config.config import KEYBOARD

class HandlerDataCollecting(Handler):
    """
    Class work with commands /start, /help, /menu
    """

    def __init__(self, bot):
        super().__init__(bot)


    def get_user_location(self, message):
        self.bot.send_message(message.chat.id, "В будущем здесь будет функционал проверки записи на урок")

    def handle(self):

        @self.bot.message_handler(content_types=["location"])
        def handle(message):
            print(message.location.longitude, message.location.latitude)
            self.get_user_location(message)