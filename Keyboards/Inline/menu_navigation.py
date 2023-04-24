from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as IKB

from Keyboards.Callback import main_menu, tasks, list_navigation


def create_ikb_select_option(select: str, admin: bool, btn_list: list[str],
                             task_type: str = '') -> InlineKeyboardMarkup:
    ikb_navigation = InlineKeyboardMarkup(row_width=3)
    if select == 'type':
        btn_list = [
            IKB(text=text,
                callback_data=list_navigation.new(menu=select,
                                                  task_type=text,
                                                  task_level='',
                                                  current_id=0))
            for text in
            btn_list]
        btn_back = IKB(text='Назад',
                       callback_data=main_menu.new(menu='',
                                                   button='back'))
    else:
        btn_list = [IKB(text=text,
                        callback_data=list_navigation.new(menu=select,
                                                          task_type=task_type,
                                                          task_level=text,
                                                          current_id=0)) for
                    text in btn_list]
        btn_back = IKB(text='Назад',
                       callback_data=main_menu.new(menu='',
                                                   button='tasks'))
    btn_add_task = IKB(text='Добавить задачу',
                       callback_data=main_menu.new(menu='',
                                                   button='add_task'))
    ikb_navigation.add(*btn_list)
    if admin:
        ikb_navigation.add(btn_add_task, btn_back)
    else:
        ikb_navigation.add(btn_back)

    return ikb_navigation


def create_ikb_list_navigation(menu: str, admin: bool, task_type: str, task_level: str, curr_id: int,
                               list_size: int) -> InlineKeyboardMarkup:
    ikb_navigation = InlineKeyboardMarkup(row_width=3)
    prev_id = int(curr_id - 1) if curr_id != 0 else int(list_size - 1)
    next_id = int(curr_id + 1) if curr_id != (list_size - 1) else 0
    btn_prev = IKB(text='<<<',
                   callback_data=list_navigation.new(menu=menu,
                                                     task_type=task_type,
                                                     task_level=task_level,
                                                     current_id=prev_id))
    btn_next = IKB(text='>>>',
                   callback_data=list_navigation.new(menu=menu,
                                                     task_type=task_type,
                                                     task_level=task_level,
                                                     current_id=next_id))
    btn_back = IKB(text='Назад',
                   callback_data=list_navigation.new(menu='type',
                                                     task_type=task_type,
                                                     task_level='',
                                                     current_id=0))
    btn_task_delete = IKB(text='Удалить задачу',
                          callback_data=list_navigation.new(menu='task_delete',
                                                            task_type=task_type,
                                                            task_level=task_level,
                                                            current_id=curr_id))
    if list_size > 1:
        ikb_navigation.add(btn_prev, btn_next)
    if admin:
        ikb_navigation.add(btn_task_delete, btn_back)
    else:
        ikb_navigation.add(btn_back)
    return ikb_navigation
