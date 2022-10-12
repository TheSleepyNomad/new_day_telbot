from abc import ABCMeta, abstractmethod
from config.markup import Keyboards


class Handler(metaclass=ABCMeta):
    """
    abstract class
    """

    def __init__(self, bot):
        self.bot = bot
        self.keyboard = Keyboards()
    
    
    @abstractmethod
    def handle(self):
        pass