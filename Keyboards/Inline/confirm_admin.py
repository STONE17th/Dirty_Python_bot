from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Keyboards.Callback import new_admin


def create_new_admin_confirm(user_id: int) -> InlineKeyboardMarkup:
    ikb_confirm = InlineKeyboardMarkup(row_width=2)

    ibtn_yes = InlineKeyboardButton(text='Да', callback_data=new_admin.new(menu='new_admin', user_id=user_id, button='yes'))
    ibtn_no = InlineKeyboardButton(text='Нет', callback_data=new_admin.new(menu='new_admin', user_id=user_id, button='no'))

    ikb_confirm.add(ibtn_yes, ibtn_no)

    return ikb_confirm