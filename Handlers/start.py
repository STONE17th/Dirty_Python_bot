from aiogram.types import Message, InputMediaPhoto
from aiogram.utils.exceptions import MessageCantBeEdited
from Keyboards import ikb_start
from Keyboards.Callback import main_menu, settings
from Misc import MsgToDict, PICTURES
from loader import dp, bot, user_db, course_db


@dp.callback_query_handler(main_menu.filter(button='back'))
@dp.message_handler(commands=['start'])
async def start_command(_, admin: bool, msg: MsgToDict):
    poster = PICTURES.get('start_poster')
    user_db.check(msg.my_id, msg.name)
    desc = f'Привет, {msg.name}!'
    try:
        await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=desc),
                                     chat_id=msg.chat_id, message_id=msg.message_id,
                                     reply_markup=ikb_start(admin))
    except MessageCantBeEdited:
        await bot.send_photo(chat_id=msg.chat_id, photo=poster, caption=desc,
                             reply_markup=ikb_start(admin))


@dp.message_handler(commands=['check'])
async def start_command(message: Message):
    print(course_db.done('botboys_2'))
    print(course_db.done('botboys_3'))
    print(course_db.done('botboys_4'))
    # def crt_cb(button: str):
    #     return settings.new(menu='settings', button=button)
    # print(type(crt_cb('button')))


@dp.message_handler(content_types='photo')
async def request_to_admin(message: Message):
    await message.answer(message.photo[0].file_id)

# Этот коммит с ПК
