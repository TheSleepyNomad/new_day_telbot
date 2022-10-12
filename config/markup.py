from telebot.types import KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from config.config import KEYBOARD


class Keyboards:
    """
    Класс Keyboards предназначен для создания разметки интерфейса
    """

    def __init__(self) -> None:
        self.markup = None


    def set_btn(self, name: str) -> KeyboardButton:
        """
        Create and return button
        """
        return KeyboardButton(KEYBOARD[name])
    

    @staticmethod
    def remove_menu() -> None:
        """
        Delete buttons
        """
        return ReplyKeyboardRemove()