from email import message
from handlers.handler import Handler


class HandlerCommands(Handler):
    """
    Class work with commands /start, /help, /menu
    """

    def __init__(self, bot):
        super().__init__(bot)


    def pressed_start_btn(self, message):
        """
        if user write /start
        """
        self.bot.send_message(message.chat.id,
                              f'{message.from_user.first_name},'
                              f' здравствуйте! Жду дальнейших задач.',
                              reply_markup=self.keyboard.start_menu())
    

    def pressed_help_btn(self, message):
        """
        if user write /help
        """
        self.bot.send_message(message.chat.id,
                              'Вы попали меню помощи')

    
    def pressed_menu_btn(self, message):
        """
        if user write /help
        """
        self.bot.send_message(message.chat.id,
                              'Вы попали меню')

    def handle(self):

        @self.bot.message_handler(commands=['start', 'help', 'menu'])
        def handle(message):
            if message.text == '/start':
                self.pressed_start_btn(message)
            if message.text == '/help':
                self.pressed_help_btn(message)
            if message.text == '/menu':
                self.pressed_menu_btn(message)
