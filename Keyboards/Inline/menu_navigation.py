from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as InKB

from Keyboards.Callback import main_menu, list_navigation


def crt_cb(menu: str, task_type: str, task_level: str = '', current_id: int = 0) -> str:
    return list_navigation.new(menu=menu,
                               task_type=task_type,
                               task_level=task_level,
                               current_id=current_id)


def ikb_select_task(select: str, admin: bool, btn_list: list[str],
                    task_type: str = '') -> InlineKeyboardMarkup:
    keyboard_task_type = InlineKeyboardMarkup(row_width=3)
    if select == 'type':
        btn_list = [InKB(text=text, callback_data=crt_cb(select, text)) for text in btn_list]
        btn_back = InKB(text='Назад', callback_data=main_menu.new(menu='', button='back'))
    else:
        btn_list = [InKB(text=text, callback_data=crt_cb(select, task_type, text)) for text in btn_list]
        btn_back = InKB(text='Назад', callback_data=main_menu.new(menu='', button='tasks'))
    btn_add_task = InKB(text='Добавить задачу', callback_data=main_menu.new(menu='', button='add_task'))
    for button in btn_list:
        keyboard_task_type.insert(button)
    if admin:
        keyboard_task_type.row(btn_add_task, btn_back)
    else:
        keyboard_task_type.row(btn_back)
    return keyboard_task_type


def ikb_navigation(menu: str, admin: bool, task_type: str, task_level: str, curr_id: int,
                   list_size: int) -> InlineKeyboardMarkup:
    keyboard_navigation = InlineKeyboardMarkup(row_width=2)
    prev_id = int(curr_id - 1) if curr_id != 0 else int(list_size - 1)
    next_id = int(curr_id + 1) if curr_id != (list_size - 1) else 0
    btn_prev = InKB(text='<<<', callback_data=crt_cb(menu, task_type, task_level, prev_id))
    btn_next = InKB(text='>>>', callback_data=crt_cb(menu, task_type, task_level, next_id))
    btn_back = InKB(text='Назад', callback_data=crt_cb('type', task_type))
    btn_task_delete = InKB(text='Удалить задачу',
                           callback_data=crt_cb('task_delete', task_type, task_level, curr_id))
    if list_size > 1:
        keyboard_navigation.add(btn_prev, btn_next)
    if admin:
        keyboard_navigation.add(btn_task_delete, btn_back)
    else:
        keyboard_navigation.add(btn_back)
    return keyboard_navigation
