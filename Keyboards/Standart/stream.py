from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from .cancel_fsm import btn_cancel

kb_stream = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn_list = [KeyboardButton(text=name) for name in ['YouTube', 'ZOOM']]

kb_stream.add(*btn_list)
kb_stream.add(btn_cancel)
