from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Keyboards.Callback import main_menu

ikb_start = InlineKeyboardMarkup(row_width=2)

ibtn_hello = InlineKeyboardButton(text='Привет',
                                  callback_data=main_menu.new(menu='main',
                                                              button='hello'))
ibtn_bye = InlineKeyboardButton(text='Пока',
                                  callback_data=main_menu.new(menu='main',
                                                              button='bye'))

ikb_start.add(ibtn_hello, ibtn_bye)