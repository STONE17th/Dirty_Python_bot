from aiogram.types import Message, InputMediaPhoto
from Keyboards import create_start_menu
from Keyboards.Callback import main_menu
from Misc import MsgToDict, PICTURES, user_distribution
from loader import dp, bot, user_db, settings_db


@dp.callback_query_handler(main_menu.filter(button='back'))
@dp.message_handler(commands=['start'])
async def start_command(_, admin: bool, msg: MsgToDict):
    poster = PICTURES.get('start_poster')
    user_db.check(msg.my_id, msg.name)
    desc = f'Привет, {msg.name}!'
    try:
        await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=desc),
                                     chat_id=msg.chat_id,
                                     message_id=msg.message_id,
                                     reply_markup=create_start_menu(admin))
    except:
        await bot.send_photo(chat_id=msg.chat_id,
                             photo=poster,
                             caption=desc,
                             reply_markup=create_start_menu(admin))


@dp.message_handler(commands=['check'])
async def start_command(message: Message):
    # print(user_db.at_course(alert='alerts_stream', table='dp_basic_01'))
    # user_distribution('stream', 'message')
    # await user_distribution('courses', 'Новый курс')
    # await user_distribution('courses', 'В курсе Бэйсик новая лекция', 'dp_basic_01')
    # user_distribution('news', 'message')
    link_list = [link[3] for link in settings_db.load(type_set='link')]
    print(link_list)


@dp.message_handler(content_types='photo')
async def request_to_admin(message: Message):
    await message.answer(message.photo[0].file_id)

# Этот коммит с ПК
