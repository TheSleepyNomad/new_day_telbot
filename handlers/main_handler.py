from handlers.handler_commands import HandlerCommands

class HandlerMain:
    """
    Collect another handlers and run them
    """
    
    def __init__(self, bot) -> None:
        self.bot = bot
        self.handler_commands = HandlerCommands(self.bot)

    
    def handle(self):
        self.handler_commands.handle()