from loader import *
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from Keyboards import ikb_start, create_ikb_my_courses
import config
from data import counter
from Keyboards.Callback import main_menu


@dp.callback_query_handler(main_menu.filter(button='my_courses'))
async def start_command(call: CallbackQuery):
    name = call.from_user.first_name
    poster = config.my_courses
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    description = f'{name}, это твои курсы!' if None not in db.user_courses(
        cur_chat) else f'{name}, у тебя нет активных курсов!'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=description),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_my_courses(call.from_user.id))
