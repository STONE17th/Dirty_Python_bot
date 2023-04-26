from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as IKB

from Keyboards.Callback import main_menu


def crt_callback(menu: str, button: str):
    return main_menu.new(menu=menu, button=button)


def create_start_menu(admin) -> InlineKeyboardMarkup:
    ikb_start = InlineKeyboardMarkup(row_width=3)

    btn_tasks = IKB(text='Задачи',
                    callback_data=crt_callback('main', 'tasks'))
    btn_all_courses = IKB(text='Курсы DP',
                          callback_data=crt_callback('main', 'all_courses'))
    btn_my_courses = IKB(text='Мои курсы',
                         callback_data=crt_callback('main', 'my_courses'))
    btn_my_settings = IKB(text='Настройки',
                          callback_data=crt_callback('main', 'settings'))
    btn_create_activity = IKB(text='Создать...',
                              callback_data=crt_callback('main', 'notification'))
    btn_links = IKB(text='Ссылки',
                              callback_data=crt_callback('main', 'links'))

    ikb_start.add(btn_tasks, btn_all_courses, btn_create_activity if admin else btn_my_courses)
    ikb_start.add(btn_my_settings, btn_links)

    return ikb_start
