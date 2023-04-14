from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Keyboards.Callback import main_menu, select_task
from loader import db


def create_ikb_task_type() -> InlineKeyboardMarkup:
    kb_task_type = InlineKeyboardMarkup(row_width=3)
    type_list = [task_type[0] for task_type in db.collect_tasks_types()]
    ibtn_list = []
    for task_type in set(type_list):
        ibtn_list.append(InlineKeyboardButton(text=task_type,
                                              callback_data=select_task.new(menu='select_task_type', task_type=task_type,
                                                                            task_level='')))
    ibtn_back = InlineKeyboardButton(text='Назад',
                                     callback_data=main_menu.new(menu='main',
                                                                 button='back'))
    kb_task_type.add(*ibtn_list)
    kb_task_type.add(ibtn_back)

    return kb_task_type