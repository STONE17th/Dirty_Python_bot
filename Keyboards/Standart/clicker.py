from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from data import counter
def create_clicker(message: Message):
    print(counter)
    counter.setdefault(message.from_user.id, 0)
    count = counter.get(message.from_user.id)
    clicker = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    btn_clicker = KeyboardButton(text=f'{count}')
    btn_restart = KeyboardButton(text='/restart')
    clicker.add(btn_clicker)
    clicker.add(btn_restart)
    return clicker