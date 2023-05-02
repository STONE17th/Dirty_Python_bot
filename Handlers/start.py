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


@dp.message_handler(commands=['add_course'])
async def start_command(message: Message, msg: MsgToDict):
    user_db.check(msg.my_id, msg.name)
    user_db.add_course(message.from_user.id)


@dp.message_handler(commands=['all_users'])
async def show_users(_, admin: bool):
    if admin:
        for row in user_db.print_table():
            tg_id, name, course, lectures = row
            print(f'{tg_id:.<13} ! {name:.<20} ! {course if course else "":.<15} ! {lectures if lectures else "":.<25}')


@dp.message_handler(commands=['add_me'])
async def show_users(message: Message, admin: bool, msg: MsgToDict):
    if admin:
        match message.chat.id:
            case -1001609984559:
                user_db.add_course(msg.my_id, 'botboys_2')
            case -807558507:
                user_db.add_course(msg.my_id, 'botboys_3')
            case -1001972599000:
                user_db.add_course(msg.my_id, 'botboys_4')
            case -644165245:
                user_db.add_course(msg.my_id, 'dp_basic_01')
            case -945231125:
                user_db.add_course(msg.my_id, 'dp_basic_2')


#
#
# @dp.message_handler(content_types='photo')
# async def request_to_admin(message: Message):
#     await message.answer(message.photo[0].file_id)
