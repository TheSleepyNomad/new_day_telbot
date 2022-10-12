from telebot.types import KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
# from config.config import KEYBOARD

class Keyboards:
    """
    Класс Keyboards предназначен для создания разметки интерфейса
    """

    def __init__(self) -> None:
        self.markup = None

    def set_btn(self, name: int) -> KeyboardButton:
        """
        Create and return button
        """
    
    @staticmethod
    def remove_menu() -> None:
        """
        Delete buttons
        """
        return ReplyKeyboardRemove()