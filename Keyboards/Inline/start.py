from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as IKB

from Keyboards.Callback import main_menu

def create_start_menu(admin) -> InlineKeyboardMarkup:
    ikb_start = InlineKeyboardMarkup(row_width=3)

    btn_tasks = IKB(text='Задачи',
                    callback_data=main_menu.new(menu='main',
                                                button='tasks'))

    btn_all_courses = IKB(text='Курсы DP',
                          callback_data=main_menu.new(menu='main',
                                                      button='all_courses'))
    btn_my_courses = IKB(text='Мои курсы',
                         callback_data=main_menu.new(menu='main',
                                                     button='my_courses'))
    btn_my_settings = IKB(text='Настройки',
                          callback_data=main_menu.new(menu='main',
                                                      button='settings'))
    btn_create_activity = IKB(text='Создать...', callback_data=main_menu.new(menu='main', button='create'))
    ikb_start.add(btn_tasks, btn_all_courses, btn_my_courses)
    ikb_start.add(btn_create_activity if admin else btn_my_settings)

    return ikb_start