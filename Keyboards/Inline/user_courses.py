from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Keyboards.Callback import main_menu, select_task
from loader import db


def create_ikb_my_courses(tg_id: int) -> InlineKeyboardMarkup:
    kb_my_courses = InlineKeyboardMarkup(row_width=3)
    button_names = db.user_courses(tg_id)
    ibtn_list = []
    if None not in button_names:
        ibtn_list = [
            InlineKeyboardButton(text=course_name[0],
                                 callback_data=main_menu.new(menu='my_courses', button=course_name[1]))
            for course_name in button_names]
    ibtn_back = InlineKeyboardButton(text='Назад', callback_data=main_menu.new(menu='', button='back'))
    kb_my_courses.add(*ibtn_list)
    kb_my_courses.add(ibtn_back)

    return kb_my_courses
