from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Keyboards.Callback import main_menu, navigation_menu, select_task
from loader import db


def create_ikb_navigation(curr_id: int, task_type: str, task_level: str) -> InlineKeyboardMarkup:
    ikb_navigation = InlineKeyboardMarkup(row_width=3)
    list_tasks = db.select_tasks(task_type, task_level)
    prev_id = int(curr_id - 1) if curr_id != 0 else int(len(list_tasks) - 1)
    next_id = int(curr_id + 1) if curr_id != (len(list_tasks) - 1) else 0
    ibtn_prev = InlineKeyboardButton(text='<<<', callback_data=navigation_menu.new(menu='navigation',
                                                                                   curr_id=prev_id,
                                                                                   task_type=task_type,
                                                                                   task_level=task_level))
    ibtn_next = InlineKeyboardButton(text='>>>', callback_data=navigation_menu.new(menu='navigation',
                                                                                   curr_id=next_id,
                                                                                   task_type=task_type,
                                                                                   task_level=task_level))
    ibtn_back = InlineKeyboardButton(text='Назад',
                                     callback_data=select_task.new(menu='select_task_type',
                                                                   task_type=task_type,
                                                                   task_level=''))
    if len(list_tasks) > 1:
        ikb_navigation.add(ibtn_prev, ibtn_next)
    ikb_navigation.add(ibtn_back)
    return ikb_navigation
