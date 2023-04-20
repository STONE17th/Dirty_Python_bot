from aiogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup
from Keyboards.Callback import main_menu, course_navigation


def create_ikb_all_courses(course_list: list[str] = [], admin: bool=False) -> InlineKeyboardMarkup:
    ikb_all_courses = InlineKeyboardMarkup(row_width=2)
    btn_online = []
    btn_offline = []
    for course in course_list:
        if course[2] == 'True':
            btn = IKB(text=f'{course[0]} (Онлайн)', callback_data=course_navigation.new(menu='online', table=course[1], current_id=0))
            btn_online.append(btn)
        else:
            btn = IKB(text=f'{course[0]} (Лекции)', callback_data=course_navigation.new(menu='offline', table=course[1], current_id=0))
            btn_online.append(btn)
    btn_create_new_course = IKB(text='Создать новый курс', callback_data=main_menu.new(menu='', button='new_course'))
    btn_back = IKB(text='Назад', callback_data=main_menu.new(menu='', button='back'))
    ikb_all_courses.row(*btn_online)
    ikb_all_courses.row(*btn_offline)
    if admin:
        ikb_all_courses.row(btn_create_new_course, btn_back)
    else:
        ikb_all_courses.row(btn_back)
    return ikb_all_courses


def create_ikb_class_navigation(menu: str, size: int, table: str, current_id: int, admin: bool) -> InlineKeyboardMarkup:
    ikb_class_navigation = InlineKeyboardMarkup(row_width=3)
    prev_id = int(current_id - 1) if current_id != 0 else int(size - 1)
    next_id = int(current_id + 1) if current_id != (size - 1) else 0
    btn_prev = IKB(text='<<<', callback_data=course_navigation.new(menu=menu, table=table, current_id=prev_id))
    btn_next = IKB(text='>>>', callback_data=course_navigation.new(menu=menu, table=table, current_id=next_id))
    btn_back = IKB(text='Назад', callback_data=main_menu.new(menu='', button='all_courses'))
    btn_class_edit = IKB(text='Изменить', callback_data=course_navigation.new(menu='edit_class', table=table, current_id=current_id))
    btn_purchase = IKB(text='Купить', callback_data=course_navigation.new(menu='purchase', table=table, current_id=current_id))
    if size > 1:
        ikb_class_navigation.row(btn_prev, btn_next)
    if admin:
        ikb_class_navigation.row(btn_class_edit, btn_back)
    else:
        ikb_class_navigation.row(btn_purchase, btn_back)
    return ikb_class_navigation
