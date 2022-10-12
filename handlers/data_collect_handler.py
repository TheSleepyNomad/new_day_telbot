from handlers.handler import Handler


class HandlerCommands(Handler):
    """
    Class work with commands /start, /help, /menu
    """

    def __init__(self, bot):
        super().__init__(bot)


    def handle(self):
        
        @self.bot.message_handler(content_types=["location"])
        def handle(message):
            pass