from telebot.types import KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from config.config import KEYBOARD


class Keyboards:
    """
    class Keyboards create menu markups and buttons
    """

    def __init__(self) -> None:
        self.markup = None


    def set_btn(self, name: str, request_location: bool = False) -> KeyboardButton:
        """
        Create and return button
        """
        return KeyboardButton(KEYBOARD[name], request_location=request_location)
    

    def start_menu(self) -> ReplyKeyboardMarkup:
        """
        Create markup when user write /start
        """

        # create markup
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.row(self.set_btn('LOCATION', True))
        self.markup.row(self.set_btn('ABOUT_APP'))

        return self.markup


    def about_app(self):
        """
        Create markup when pressed about_app button
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.row(self.set_btn('<<'))

        return self.markup    

    @staticmethod
    def remove_menu() -> None:
        """
        Delete buttons
        """
        return ReplyKeyboardRemove()