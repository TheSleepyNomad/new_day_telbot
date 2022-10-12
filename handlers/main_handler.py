from handlers.handler_commands import HandlerCommands
from handlers.data_collect_handler import HandlerDataCollecting
from handlers.text_handler import HandlerText


class HandlerMain:
    """
    Collect another handlers and run them
    """
    
    def __init__(self, bot) -> None:
        self.bot = bot
        self.handler_commands = HandlerCommands(self.bot)
        self.handler_data_collecting = HandlerDataCollecting(self.bot)
        self.handler_text = HandlerText(self.bot)

    
    def handle(self):
        self.handler_commands.handle()
        self.handler_data_collecting.handle()
        self.handler_text.handle()
