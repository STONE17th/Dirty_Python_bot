from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Keyboards.Callback import main_menu

ikb_start = InlineKeyboardMarkup(row_width=3)

ibtn_tasks = InlineKeyboardButton(text='Задачи',
                                  callback_data=main_menu.new(menu='main',
                                                              button='tasks'))

ibtn_all_courses = InlineKeyboardButton(text='Курсы DP',
                                        callback_data=main_menu.new(menu='main',
                                                                    button='all_courses'))
ibtn_my_courses = InlineKeyboardButton(text='Мои курсы',
                                       callback_data=main_menu.new(menu='main',
                                                                   button='my_courses'))
ibtn_my_settings = InlineKeyboardButton(text='Настройки',
                                        callback_data=main_menu.new(menu='main',
                                                                    button='settings'))

ikb_start.add(ibtn_tasks, ibtn_all_courses, ibtn_my_courses)
ikb_start.add(ibtn_my_settings)
