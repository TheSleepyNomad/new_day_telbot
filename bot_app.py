"""
Main file for bot app running
"""

from telebot import TeleBot
from handlers.main_handler import HandlerMain
from os import environ
from dotenv import load_dotenv
from config.config import TELEGRAM_BOT_API_KEY


class Telebot:

    def __init__(self) -> None:
        self.token = TELEGRAM_BOT_API_KEY
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