"""
Main file for bot app running
"""

from telebot import TeleBot
from handlers.main_handler import HandlerMain
from os import environ
from dotenv import load_dotenv

class Telebot:

    def __init__(self) -> None:
        self.token = environ.get('API_KEY')
        self.bot = TeleBot(self.token)

        # if we dont get api key from evn
        if self.token is None:
            load_dotenv()
            self.token = environ.get('API_KEY')
            self.bot = TeleBot(self.token)

        self.handler = HandlerMain(self.bot)

    
    def start(self):
        self.handler.handle()

    
    def run(self):
        self.start()
        self.bot.polling(none_stop=True)


if __name__ == '__main__':
    bot = Telebot()
    bot.run()