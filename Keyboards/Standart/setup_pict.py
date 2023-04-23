from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from .cancel_fsm import btn_cancel

kb_next_pict = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_next = KeyboardButton(text='Дальше')

kb_next_pict.add(btn_next, btn_cancel)
