from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from .cancel_fsm import btn_cancel

kb_task_level = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn_easy = KeyboardButton(text='easy')
btn_normal = KeyboardButton(text='normal')
btn_hard = KeyboardButton(text='hard')

kb_task_level.add(btn_easy, btn_normal, btn_hard)
kb_task_level.add(btn_cancel)
