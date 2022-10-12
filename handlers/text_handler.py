from handlers.handler import Handler


class HandlerText(Handler):
    """
    Handler HandlerText response for work with buttons and text from user
    """

    def __init__(self, bot):
        super().__init__(bot)


    def handle(self):

        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            pass