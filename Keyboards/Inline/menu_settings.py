from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Keyboards.Callback import main_menu, settings_option


def create_ikb_settings(my_set: tuple) -> InlineKeyboardMarkup:
    _, stream, courses, news = my_set
    ikb_settings = InlineKeyboardMarkup(row_width=1)

    btn_stream = InlineKeyboardButton(text=f'Оповещения о стримах DP: {"ON" if stream == "True" else "OFF"}',
                                      callback_data=settings_option.new(menu='settings',
                                                                        button='stream'))
    btn_courses = InlineKeyboardButton(text=f'Оповещения о моих курсах DP: {"ON" if courses == "True" else "OFF"}',
                                       callback_data=settings_option.new(menu='settings',
                                                                         button='courses'))
    btn_news = InlineKeyboardButton(text=f'Оповещения о новостях и акциях DP: {"ON" if news == "True" else "OFF"}',
                                    callback_data=settings_option.new(menu='settings',
                                                                      button='news'))
    btn_back = InlineKeyboardButton(text='Назад',
                                    callback_data=main_menu.new(menu='main',
                                                                      button='back'))

    ikb_settings.add(btn_stream)
    ikb_settings.add(btn_courses)
    ikb_settings.add(btn_news)
    ikb_settings.add(btn_back)
    return ikb_settings
