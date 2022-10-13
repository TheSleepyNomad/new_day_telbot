from handlers.handler import Handler
from config.config import KEYBOARD
from config.messages import MESSAGES


class HandlerText(Handler):
    """
    Handler HandlerText response for work with buttons and text from user
    """

    def __init__(self, bot):
        super().__init__(bot)


    def pressed_about_app_btn(self, message):
        """
        user press btn about app
        """
        self.bot.send_message(message.chat.id, MESSAGES['about_app'],
                              parse_mode="HTML",
                              reply_markup=self.keyboard.about_app())


    def pressed_back_btn(self, message):
        """
        Обработка события нажатия на кнопку 'Назад'
        """
        self.bot.send_message(message.chat.id, "Вы вернулись назад",
                              reply_markup=self.keyboard.start_menu())


    def handle(self):

        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            if message.text == KEYBOARD['ABOUT_APP']:
                self.pressed_about_app_btn(message)

            if message.text == KEYBOARD['<<']:
                self.pressed_back_btn(message)
