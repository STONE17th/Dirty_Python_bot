from aiogram.types import InlineKeyboardButton as InKB, InlineKeyboardMarkup

from Keyboards.Callback import main_menu, course_navigation
from Misc import MsgToDict, Course
from loader import course_db, user_db


def crt_callback(menu: str = '', table: str = '', current_id: int = 0):
    return course_navigation.new(menu=menu, table=table, current_id=current_id)


def ikb_all_courses(course_list: list[Course], admin: bool = False) -> InlineKeyboardMarkup:
    keyboard_all_courses = InlineKeyboardMarkup(row_width=2)
    btn_online = []
    btn_offline = []
    for course in course_list:
        if course.is_active() == 1:
            if admin:
                btn = InKB(text=f'{course.name} (Онлайн)', callback_data=crt_callback('offline', course.table))
                btn_offline.append(btn)
            else:
                btn = InKB(text=f'{course.name} (Онлайн)', callback_data=crt_callback('online', course.table))
                btn_online.append(btn)
        elif course.is_active() == 0:
            btn = InKB(text=f'{course.name} (Лекции)', callback_data=crt_callback('offline', course.table))
            btn_offline.append(btn)
    btn_create_new_course = InKB(text='Создать', callback_data=main_menu.new(menu='', button='new_course'))
    btn_individual = InKB(text='Индивидуальные занятия', callback_data=crt_callback('individual'))
    btn_back = InKB(text='Назад', callback_data=main_menu.new(menu='', button='back'))
    keyboard_all_courses.add(*btn_online)
    keyboard_all_courses.add(*btn_offline)
    if admin:
        keyboard_all_courses.row(btn_create_new_course, btn_back)
    else:
        keyboard_all_courses.row(btn_individual, btn_back)
    return keyboard_all_courses


def ikb_offline_course(menu: str, size: int, table: str, current_id: int, admin: bool,
                       msg: MsgToDict) -> InlineKeyboardMarkup:
    keyboard_offline_course = InlineKeyboardMarkup(row_width=3)
    prev_id = int(current_id - 1) if current_id != 0 else int(size - 1)
    next_id = int(current_id + 1) if current_id != (size - 1) else 0
    btn_prev = InKB(text='<<<', callback_data=crt_callback(menu, table, prev_id))
    btn_next = InKB(text='>>>', callback_data=crt_callback(menu, table, next_id))
    btn_back = InKB(text='Назад', callback_data=main_menu.new(menu='', button='all_courses'))
    btn_lecture_edit = InKB(text='Изменить', callback_data=crt_callback('edit_class', table, current_id))
    btn_finalize_course = InKB(text='Завершить', callback_data=crt_callback('finalize_course', table, current_id))
    btn_archive_course = InKB(text='Архивировать', callback_data=crt_callback('finalize_course', table, -1))
    btn_purchase = InKB(text='Купить', callback_data=crt_callback('purchase', table, current_id))

    if size > 1:
        keyboard_offline_course.row(btn_prev, btn_next)
    if admin:
        if course_db.is_completed(table) and course_db.status(msg.table):
            keyboard_offline_course.row(btn_finalize_course)
        elif not course_db.status(table):
            keyboard_offline_course.row(btn_archive_course)
        keyboard_offline_course.add(btn_lecture_edit, btn_back)
    else:
        user_courses, user_lectures = user_db.course_and_lectures(msg.my_id)
        if not ((user_lectures and f'{table}:{current_id}' in user_lectures) or (
                user_courses and table in user_courses)):
            keyboard_offline_course.row(btn_purchase, btn_back)
        else:
            keyboard_offline_course.row(btn_back)
    return keyboard_offline_course


def ikb_online_course(msg: MsgToDict, table: str) -> InlineKeyboardMarkup:
    keyboard_online_course = InlineKeyboardMarkup(row_width=3)
    btn_purchase = InKB(text='Купить', callback_data=crt_callback('purchase', table, -1))
    btn_back = InKB(text='Назад', callback_data=main_menu.new(menu='', button='all_courses'))
    user_courses, user_lectures = user_db.course_and_lectures(msg.my_id) if user_db.course_and_lectures(
        msg.my_id) else (None, None)
    if not user_courses or table not in user_courses:
        keyboard_online_course.row(btn_purchase, btn_back)
    else:
        keyboard_online_course.row(btn_back)
    return keyboard_online_course


def ikb_individual() -> InlineKeyboardMarkup:
    keyboard_individual = InlineKeyboardMarkup(row_width=2)
    btn_want = InKB(text='Оставить заявку', callback_data=crt_callback('want'))
    btn_back = InKB(text='Назад', callback_data=main_menu.new(menu='', button='all_courses'))
    keyboard_individual.add(btn_want, btn_back)
    return keyboard_individual
