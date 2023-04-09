from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Keyboards.Callback import main_menu


def create_ikb_settings(my_set: tuple):
    _, stream, courses, news = my_set
    ikb_settings = InlineKeyboardMarkup(row_width=1)

    ibtn_stream = InlineKeyboardButton(text=f'Оповещения о стримах DP: {"ON" if stream else "OFF"}',
                                       callback_data=main_menu.new(menu='settings',
                                                                   button='all_courses'))
    ibtn_courses = InlineKeyboardButton(text=f'Оповещения о моих курсах DP: {"ON" if courses else "OFF"}',
                                        callback_data=main_menu.new(menu='settings',
                                                                    button='my_courses'))
    ibtn_news = InlineKeyboardButton(text=f'Оповещения о новостях и акциях DP: {"ON" if news else "OFF"}',
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
