from aiogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup

from Keyboards.Callback import main_menu, course_navigation
from Misc import MsgToDict, Course
from loader import course_db, user_db


def crt_callback(menu: str = '', table: str = '', current_id: int = 0):
    return course_navigation.new(menu=menu, table=table, current_id=current_id)


def create_ikb_all_courses(course_list: list[Course], admin: bool = False) -> InlineKeyboardMarkup:
    ikb_all_courses = InlineKeyboardMarkup(row_width=2)
    btn_online = []
    btn_offline = []
    for course in course_list:
        if admin:
            btn = IKB(text=f'{course.name} (Идет)' if course.is_active() else f'{course.name} (Завершен)',
                      callback_data=crt_callback('offline', course.table))
            btn_online.append(btn)
        elif course.is_active():
            btn = IKB(text=f'{course.name} (Онлайн)', callback_data=crt_callback('online', course.table))
            btn_online.append(btn)
        else:
            btn = IKB(text=f'{course.name} (Лекции)', callback_data=crt_callback('offline', course.table))
            btn_offline.append(btn)
    btn_create_new_course = IKB(text='Создать новый курс', callback_data=main_menu.new(menu='', button='new_course'))
    btn_individual = IKB(text='Индивидуальные занятия',
                         callback_data=crt_callback('individual'))
    btn_back = IKB(text='Назад', callback_data=main_menu.new(menu='', button='back'))
    ikb_all_courses.add(*btn_online)
    ikb_all_courses.add(*btn_offline)
    if admin:
        ikb_all_courses.row(btn_create_new_course, btn_back)
    else:
        ikb_all_courses.row(btn_individual)
        ikb_all_courses.row(btn_back)
    return ikb_all_courses


def create_ikb_class_navigation(menu: str, size: int, table: str, current_id: int, admin: bool,
                                msg: MsgToDict) -> InlineKeyboardMarkup:
    ikb_class_navigation = InlineKeyboardMarkup(row_width=3)
    prev_id = int(current_id - 1) if current_id != 0 else int(size - 1)
    next_id = int(current_id + 1) if current_id != (size - 1) else 0
    btn_prev = IKB(text='<<<',
                   callback_data=crt_callback(menu, table, prev_id))
    btn_next = IKB(text='>>>',
                   callback_data=crt_callback(menu, table, next_id))
    btn_back = IKB(text='Назад',
                   callback_data=main_menu.new(menu='', button='all_courses'))
    btn_lecture_edit = IKB(text='Изменить',
                           callback_data=crt_callback('edit_class', table, current_id))
    btn_finalize_course = IKB(text='Завершить',
                              callback_data=crt_callback('finalize_course', table, current_id))
    btn_purchase = IKB(text='Купить',
                       callback_data=crt_callback('purchase', table, current_id))

    if size > 1:
        ikb_class_navigation.row(btn_prev, btn_next)
    if admin:
        if all(map(lambda x: x != (None,), course_db.is_completed(table))):
            ikb_class_navigation.row(btn_finalize_course, btn_lecture_edit, btn_back)
        else:
            ikb_class_navigation.row(btn_lecture_edit, btn_back)
    else:
        user_courses, user_lectures = user_db.course_and_lectures(msg.my_id)
        if not ((user_lectures and f'{table}:{current_id}' in user_lectures) or (
                user_courses and table in user_courses)):
            ikb_class_navigation.row(btn_purchase, btn_back)
        else:
            ikb_class_navigation.row(btn_back)
    return ikb_class_navigation


def create_ikb_online_course(msg: MsgToDict, table: str) -> InlineKeyboardMarkup:
    ikb_online_course = InlineKeyboardMarkup(row_width=3)
    btn_purchase = IKB(text='Купить',
                       callback_data=crt_callback('purchase', table, -1))
    btn_back = IKB(text='Назад',
                   callback_data=main_menu.new(menu='', button='all_courses'))
    print(f'{user_db.course_and_lectures(msg.my_id)} лекции')
    user_courses, user_lectures = user_db.course_and_lectures(msg.my_id) if user_db.course_and_lectures(
        msg.my_id) else (None, None)
    if not user_courses or table not in user_courses:
        ikb_online_course.row(btn_purchase, btn_back)
    else:
        ikb_online_course.row(btn_back)
    return ikb_online_course


def create_ikb_individual() -> InlineKeyboardMarkup:
    ikb_individual = InlineKeyboardMarkup(row_width=2)
    btn_want = IKB(text='Оставить заявку',
                   callback_data=crt_callback('want'))
    btn_back = IKB(text='Назад',
                   callback_data=main_menu.new(menu='', button='all_courses'))

    ikb_individual.add(btn_want, btn_back)
    return ikb_individual
