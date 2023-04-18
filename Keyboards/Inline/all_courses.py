from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Keyboards.Callback import main_menu, select_task
from loader import db


def create_ikb_all_courses() -> InlineKeyboardMarkup:
    kb_all_courses = InlineKeyboardMarkup(row_width=3)
    button_names = []
    ibtn_list = []
    if None not in button_names:
        ibtn_list = [
            InlineKeyboardButton(text=course_name[0],
                                 callback_data=main_menu.new(menu='my_courses', button=course_name[1]))
            for course_name in button_names]
    ibtn_create_new_course = InlineKeyboardButton(text='Создать новый курс', callback_data=main_menu.new(menu='', button='new_course'))
    ibtn_back = InlineKeyboardButton(text='Назад', callback_data=main_menu.new(menu='', button='all_courses'))
    kb_all_courses.add(*ibtn_list)
    kb_all_courses.add(ibtn_create_new_course)
    kb_all_courses.add(ibtn_back)

    return kb_all_courses