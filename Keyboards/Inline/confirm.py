from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Keyboards.Callback import main_menu


def create_ikb_confirm(target: str) -> InlineKeyboardMarkup:
    ikb_confirm = InlineKeyboardMarkup(row_width=2)

    ibtn_yes = InlineKeyboardButton(text='Да', callback_data=main_menu.new(menu=f'{target}_confirm', button='yes'))
    ibtn_no = InlineKeyboardButton(text='Нет', callback_data=main_menu.new(menu=f'{target}_confirm', button='no'))

    ikb_confirm.add(ibtn_yes, ibtn_no)

    return ikb_confirm