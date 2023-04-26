from aiogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup
from Keyboards.Callback import main_menu, course_navigation


def create_ikb_my_courses(courses) -> InlineKeyboardMarkup:
    kb_my_courses = InlineKeyboardMarkup(row_width=2)
    if courses and courses != (None,):
        btn_courses = [IKB(text=course.name,
                           callback_data=course_navigation.new(menu='my_courses',
                                                               table=course.table,
                                                               current_id=0)) for course in courses if course.lectures]
        [kb_my_courses.add(btn) for btn in btn_courses]
    btn_back = IKB(text='Назад',
                   callback_data=main_menu.new(menu='',
                                               button='back'))
    kb_my_courses.add(btn_back)
    return kb_my_courses



def create_ikb_my_course_navigation(menu: str, curr_id: int, list_size: int, table: str = '') -> InlineKeyboardMarkup:
    ikb_navigation = InlineKeyboardMarkup(row_width=2)
    prev_id = int(curr_id - 1) if curr_id != 0 else int(list_size - 1)
    next_id = int(curr_id + 1) if curr_id != (list_size - 1) else 0
    btn_prev = IKB(text='<<<',
                   callback_data=course_navigation.new(menu=menu,
                                                       table=table,
                                                       current_id=prev_id))
    btn_next = IKB(text='>>>',
                   callback_data=course_navigation.new(menu=menu,
                                                       table=table,
                                                       current_id=next_id))
    btn_back = IKB(text='Назад',
                   callback_data=main_menu.new(menu='',
                                               button='my_courses'))
    if list_size > 1:
        ikb_navigation.add(btn_prev, btn_next)
    ikb_navigation.add(btn_back)
    return ikb_navigation
