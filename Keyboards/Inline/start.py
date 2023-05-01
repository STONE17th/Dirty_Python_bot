from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as InKB

from Keyboards.Callback import main_menu


def crt_callback(button: str):
    return main_menu.new(menu='main', button=button)


def ikb_start(admin) -> InlineKeyboardMarkup:
    keyboard_start = InlineKeyboardMarkup(row_width=3)

    btn_tasks = InKB(text='Задачи', callback_data=crt_callback('tasks'))
    btn_all_courses = InKB(text='Курсы DP', callback_data=crt_callback('all_courses'))
    btn_my_courses = InKB(text='Мои курсы', callback_data=crt_callback('my_courses'))
    btn_my_settings = InKB(text='Настройки', callback_data=crt_callback('settings'))
    btn_create_activity = InKB(text='Создать...', callback_data=crt_callback('notification'))
    btn_links = InKB(text='Ссылки', callback_data=crt_callback('links'))

    keyboard_start.add(btn_tasks, btn_all_courses, btn_create_activity if admin else btn_my_courses)
    keyboard_start.add(btn_my_settings, btn_links)

    return keyboard_start
