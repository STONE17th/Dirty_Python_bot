from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

kb_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_start = KeyboardButton(text='/start')
btn_help = KeyboardButton(text='/help')
btn_mother = KeyboardButton(text='мама')
btn_location = KeyboardButton(text='Локация', request_location=True)
btn_phone = KeyboardButton(text='Телефон', request_contact=True)
btn_phone = KeyboardButton(text='Телефон')

kb_main.add(btn_start, btn_help)
kb_main.add(btn_mother)
kb_main.add(btn_location, btn_phone)

remover = ReplyKeyboardRemove()