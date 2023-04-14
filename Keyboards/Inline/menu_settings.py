from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Keyboards.Callback import main_menu


def create_ikb_settings(my_set: tuple) -> InlineKeyboardMarkup:
    _, stream, courses, news = my_set
    ikb_settings = InlineKeyboardMarkup(row_width=1)

    ibtn_stream = InlineKeyboardButton(text=f'Оповещения о стримах DP: {"ON" if stream == "True" else "OFF"}',
                                       callback_data=main_menu.new(menu='settings',
                                                                   button='stream'))
    ibtn_courses = InlineKeyboardButton(text=f'Оповещения о моих курсах DP: {"ON" if courses == "True" else "OFF"}',
                                        callback_data=main_menu.new(menu='settings',
                                                                    button='courses'))
    ibtn_news = InlineKeyboardButton(text=f'Оповещения о новостях и акциях DP: {"ON" if news == "True" else "OFF"}',
                                     callback_data=main_menu.new(menu='settings',
                                                                 button='news'))
    ibtn_back = InlineKeyboardButton(text='Назад',
                                     callback_data=main_menu.new(menu='main',
                                                                 button='back'))

    ikb_settings.add(ibtn_stream)
    ikb_settings.add(ibtn_courses)
    ikb_settings.add(ibtn_news)
    ikb_settings.add(ibtn_back)
    return ikb_settings