from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Keyboards.Callback import main_menu, select_task
from loader import db


def create_ikb_task_level(task_type: str) -> InlineKeyboardMarkup:
    kb_task_level = InlineKeyboardMarkup(row_width=3)
    ibtn_list = []
    for task_level in ['easy', 'normal', 'hard']:
        ibtn_list.append(InlineKeyboardButton(text=task_level,
                                              callback_data=select_task.new(menu='select_task_level', task_type=task_type,
                                                                            task_level=task_level)))
    ibtn_back = InlineKeyboardButton(text='Назад',
                                     callback_data=main_menu.new(menu='main',
                                                                 button='tasks'))
    kb_task_level.add(*ibtn_list)
    kb_task_level.add(ibtn_back)

    return kb_task_level