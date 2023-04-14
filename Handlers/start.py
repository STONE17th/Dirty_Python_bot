from loader import *
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from Keyboards import ikb_start
import config
from data import counter
from Keyboards.Callback import main_menu


@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    name = message.from_user.first_name
    poster = config.start_poster
    cur_chat = message.from_user.id
    cur_message = message.message_id
    if not db.check_user(cur_chat):
        db.new_user((cur_chat, name))
    description = f'Привет, {name}!'
    await bot.send_photo(chat_id=cur_chat, photo=poster,
                         caption=description, reply_markup=ikb_start)


@dp.callback_query_handler(main_menu.filter(button='back'))
async def start_command(call: CallbackQuery):
    name = call.from_user.first_name
    poster = config.start_poster
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    if not db.check_user(cur_chat):
        db.new_user((cur_chat, name))
    description = f'Привет, {name}!'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=description),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=ikb_start)

@dp.message_handler(content_types='photo')
async def start_command(message: Message):
    print(message.photo[0].file_id)
