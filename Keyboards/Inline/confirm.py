from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Keyboards.Callback import main_menu, confirm_request


def create_ikb_confirm(target: str, args: str) -> InlineKeyboardMarkup:
    ikb_confirm = InlineKeyboardMarkup(row_width=2)

    btn_yes = InlineKeyboardButton(text='Да', callback_data=confirm_request.new(menu=target, args=args, button='yes'))
    btn_no = InlineKeyboardButton(text='Нет', callback_data=confirm_request.new(menu=target, args=args, button='no'))

    ikb_confirm.add(btn_yes, btn_no)

    return ikb_confirm