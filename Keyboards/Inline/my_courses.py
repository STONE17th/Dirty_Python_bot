from aiogram.types import InlineKeyboardButton as InKB, InlineKeyboardMarkup
from Keyboards.Callback import main_menu, course_navigation


def ikb_my_courses(courses) -> InlineKeyboardMarkup:
    keyboard_my_courses = InlineKeyboardMarkup(row_width=2)
    if courses and courses != (None,):
        btn_courses = [InKB(text=course.name,
                           callback_data=course_navigation.new(menu='my_courses',
                                                               table=course.table,
                                                               current_id=0)) for course in courses if course.lectures]
        [keyboard_my_courses.add(btn) for btn in btn_courses]
    btn_back = InKB(text='Назад',
                   callback_data=main_menu.new(menu='',
                                               button='back'))
    keyboard_my_courses.add(btn_back)
    return keyboard_my_courses



def ikb_my_course_navigation(menu: str, buttons: tuple[str,str], curr_id: int, list_size: int, table: str = '') -> InlineKeyboardMarkup:
    keyboard_my_navigation = InlineKeyboardMarkup(row_width=2)
    prev_id = int(curr_id - 1) if curr_id != 0 else int(list_size - 1)
    next_id = int(curr_id + 1) if curr_id != (list_size - 1) else 0
    btn_prev = InKB(text='<<<',
                   callback_data=course_navigation.new(menu=menu,
                                                       table=table,
                                                       current_id=prev_id))
    btn_next = InKB(text='>>>',
                   callback_data=course_navigation.new(menu=menu,
                                                       table=table,
                                                       current_id=next_id))
    btn_video = InKB(text='Лекция', url=buttons[0])
    btn_compendium = InKB(text='Конспект', url=buttons[1])
    btn_back = InKB(text='Назад', callback_data=main_menu.new(menu='', button='my_courses'))
    keyboard_my_navigation.row(btn_video, btn_compendium)
    if list_size > 1:
        keyboard_my_navigation.add(btn_prev, btn_next)
    keyboard_my_navigation.add(btn_back)
    return keyboard_my_navigation
