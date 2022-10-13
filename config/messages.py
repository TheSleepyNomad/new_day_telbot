from config.config import APP_VERSION, CREATE_BY, AUTHOR_GITHUB_LINK

"""
This file storage messages template for user
"""

# show if user write /start first time
start_message = """

"""

# show if user already have in data base 
welcome_message = """

"""

# show if user press button 'about app'
about_app = """
<b>Бот <i>Weather Today =)</i></b>
<i>Подсказываю погоду на сегодня и прогнозирую на неделю</i>

<b>Общая информация:</b>
Данный бот разработан для практики и попробовать
типизированный python и dataclass, а также освоить
библиотеку requests

<b>Дополнительная информация:</b>

<b>Версия бота: - </b><i>({})</i>
<b>Разработчик: - </b><i>({})</i>
<b>GITHUB: - </b><i>({})</i>
""".format(APP_VERSION, CREATE_BY, AUTHOR_GITHUB_LINK)

MESSAGES = {
    'start_message': start_message,
    'welcome_message': welcome_message,
    'about_app': about_app,
}