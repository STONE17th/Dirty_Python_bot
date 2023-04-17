from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from .cancel_fsm import btn_cancel
from loader import db


def create_kb_task_type() -> ReplyKeyboardMarkup:
    kb_task_type = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    type_list = [task_type[0] for task_type in db.collect_tasks('task_type')]
    btn_list = []
    for task_type in set(type_list):
        btn_list.append(KeyboardButton(text=task_type))
    kb_task_type.add(*btn_list)
    kb_task_type.add(btn_cancel)

    return kb_task_type
