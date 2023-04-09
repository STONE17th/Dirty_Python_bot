from loader import *
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from Keyboards import ikb_start, create_ikb_settings
from Keyboards.Callback import main_menu
import config


@dp.callback_query_handler(main_menu.filter(button='settings'))
async def my_settings(call: CallbackQuery):
    name = call.from_user.first_name
    poster = config.start_poster
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    my_set = db.user_settings(cur_chat)
    caption = 'Это твои настройки'
    print(my_set)
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_settings(my_set))


@dp.callback_query_handler(main_menu.filter(menu='settings'))
async def select_settings(call: CallbackQuery):
    cur_button = call.data.split(':')[-1]
    name = call.from_user.first_name
    poster = config.start_poster
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    my_set = db.user_settings(cur_chat)
    caption = 'Это твои настройки'
    match cur_button:
        case 'all_courses':
            db.change_option_stream(cur_chat)

            print('Выбран ВСЕ СТРИМЫ')
            caption = 'ВСЕ СТРИМЫ ОТКЛЮЧЕНЫ'
        case 'my_courses':
            print(bool(my_set[2]))
            print(type(my_set[2]))
            print('Выбран МОИ КУРСЫ')
            caption = 'ВСЕ КУРСЫ ОТКЛЮЧЕНЫ'
        case 'news':
            print(my_set[3])
            print(type(my_set[3]))
            print('Выбран НОВОСТИ')
            caption = 'ВСЕ НОВОСТИ ОТКЛЮЧЕНЫ'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_settings(my_set))

