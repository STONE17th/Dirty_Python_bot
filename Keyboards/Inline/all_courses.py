from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Keyboards.Callback import main_menu, tasks
from loader import db


def create_ikb_all_courses(btn_list: list[str], admin: bool) -> InlineKeyboardMarkup:
    ikb_all_courses = InlineKeyboardMarkup(row_width=3)
    button_names = db.all_active_courses()
    ibtn_list = []
    if None not in button_names:
        ibtn_list = [
            InlineKeyboardButton(text=course_name[0],
                                 callback_data=main_menu.new(menu='target_course', button=course_name[1]))
            for course_name in button_names]
    ibtn_create_new_course = InlineKeyboardButton(text='Создать новый курс', callback_data=main_menu.new(menu='', button='new_course'))
    ibtn_back = InlineKeyboardButton(text='Назад', callback_data=main_menu.new(menu='', button='back'))
    ikb_all_courses.add(*ibtn_list)
    if admin:
        ikb_all_courses.add(ibtn_create_new_course)
    ikb_all_courses.add(ibtn_back)

    return ikb_all_courses


def create_ikb_all_classes(table_name: str) -> InlineKeyboardMarkup:
    ikb_all_classes = InlineKeyboardMarkup(row_width=3)
    button_names = db.all_classes(table_name)
    ibtn_list = []
    if None not in button_names:
        ibtn_list = [
            InlineKeyboardButton(text=course_name[0],
                                 callback_data=main_menu.new(menu='target_course', button=course_name[1]))
            for course_name in button_names]
    ibtn_create_new_course = InlineKeyboardButton(text='Создать новый курс', callback_data=main_menu.new(menu='', button='new_course'))
    ibtn_back = InlineKeyboardButton(text='Назад', callback_data=main_menu.new(menu='', button='back'))
    ikb_all_classes.add(*ibtn_list)
    ikb_all_classes.add(ibtn_create_new_course)
    ikb_all_classes.add(ibtn_back)

    return ikb_all_classes