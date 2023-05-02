from aiogram.types import Message, InputMediaPhoto
from aiogram.utils.exceptions import MessageCantBeEdited, MessageCantBeDeleted

from Keyboards import ikb_start
from Keyboards.Callback import main_menu
from Misc import MsgToDict, PICTURES
from loader import dp, bot, user_db


@dp.callback_query_handler(main_menu.filter(button='back'))
@dp.message_handler(commands=['start'])
async def start_command(_, admin: bool, msg: MsgToDict):
    poster = PICTURES.get('start_poster')
    user_db.check(msg.my_id, msg.name)
    desc = f'Привет, уважаемый {msg.name}!'
    try:
        await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=desc),
                                     chat_id=msg.chat_id, message_id=msg.message_id,
                                     reply_markup=ikb_start(admin))
    except MessageCantBeEdited:
        await bot.send_photo(chat_id=msg.chat_id, photo=poster, caption=desc,
                             reply_markup=ikb_start(admin))


@dp.callback_query_handler(main_menu.filter(button='message_delete'))
async def start_command(_, msg: MsgToDict):
    try:
        await bot.delete_message(chat_id=msg.chat_id, message_id=msg.message_id)
    except MessageCantBeDeleted:
        pass


# @dp.message_handler(commands=['add_course'])
# async def start_command(message: Message, msg: MsgToDict):
#     user_db.check(msg.my_id, msg.name)
#     user_db.add_course(message.from_user.id)
#
#
# @dp.message_handler(content_types='photo')
# async def request_to_admin(message: Message):
#     await message.answer(message.photo[0].file_id)
