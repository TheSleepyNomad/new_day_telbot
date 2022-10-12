from abc import ABCMeta, abstractmethod
from config.markup import Keyboards

"""
Класс родитель - следит за обязательным изменением метода handle
"""

class Handler(metaclass=ABCMeta):

    def __init__(self, bot):
        self.bot = bot
        self.keyboard = Keyboards()
    
    @abstractmethod
    def handle(self):
        pass