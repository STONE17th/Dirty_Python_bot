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
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_settings(my_set))


@dp.callback_query_handler(main_menu.filter(menu='settings'))
async def select_settings(call: CallbackQuery):
    cur_button = call.data.split(':')[-1]
    poster = config.start_poster
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = 'Это твои настройки'
    db.change_option(cur_chat, cur_button)
    my_set = db.user_settings(cur_chat)
    match cur_button:
        case 'stream':
            caption = f'Оповещения на все стримы {"ВКЛЮЧЕНЫ" if my_set[1] == "True" else "ОТКЛЮЧЕНЫ"}'
        case 'courses':
            caption = f'Оповещения о курсах {"ВКЛЮЧЕНЫ" if my_set[1] == "True" else "ОТКЛЮЧЕНЫ"}'
        case 'news':
            caption = f'Оповещения о новостях {"ВКЛЮЧЕНЫ" if my_set[1] == "True" else "ОТКЛЮЧЕНЫ"}'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_settings(my_set))

