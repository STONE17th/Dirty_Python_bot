from loader import *
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from Keyboards import ikb_start
import config
from data import counter
from Keyboards.Callback import main_menu


@dp.message_handler(commands=['my'])
async def start_command(message: Message):
    db.user_courses(message.from_user.id)
    name = message.from_user.first_name
    poster = config.start_poster
    cur_chat = message.from_user.id
    cur_message = message.message_id
    if not db.check_user(cur_chat):
        db.new_user((cur_chat, name))
    description = f'Привет, {name}!'
    await bot.send_photo(chat_id=cur_chat, photo=poster,
                         caption=description, reply_markup=ikb_start)