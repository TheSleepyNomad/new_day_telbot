from handlers.handler import Handler


class HandlerText(Handler):
    """
    Class work with commands /start, /help, /menu
    """

    def __init__(self, bot):
        super().__init__(bot)


    def handle(self):

        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            pass