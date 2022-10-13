from handlers.handler import Handler
from config.config import KEYBOARD
from config.messages import MESSAGES


class HandlerText(Handler):
    """
    Handler HandlerText response for work with buttons and text from user
    """

    def __init__(self, bot):
        super().__init__(bot)


    def pressed_btn_about_app(self, message):
        """
        user press btn about app
        """
        self.bot.send_message(message.chat.id, MESSAGES['about_app'],
                              parse_mode="HTML",)


    def handle(self):

        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            if message.text == KEYBOARD['ABOUT_APP']:
                self.pressed_btn_about_app(message)