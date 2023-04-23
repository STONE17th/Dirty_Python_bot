from loader import dp, bot, user_db
from aiogram.types import CallbackQuery, InputMediaPhoto
from Keyboards import create_ikb_settings
from Keyboards.Callback import main_menu,settings_option
from Misc import MsgToDict, pictures


@dp.callback_query_handler(main_menu.filter(button='settings'))
async def my_settings(call: CallbackQuery, msg: MsgToDict):
    poster = pictures.start_poster
    user_settings = user_db.settings(msg.my_id)
    desc = 'Это твои настройки'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=desc),
                                 chat_id=msg.chat_id, message_id=msg.message_id,
                                 reply_markup=create_ikb_settings(user_settings))


@dp.callback_query_handler(settings_option.filter(menu='settings'))
async def select_settings(call: CallbackQuery, msg: MsgToDict):
    poster = pictures.start_poster
    caption = 'Это твои настройки'
    user_db.switcher(msg.my_id, msg.button)
    user_settings = user_db.settings(msg.my_id)
    match msg.button:
        case 'stream':
            caption = f'Оповещения на все стримы {"ВКЛЮЧЕНЫ" if user_settings[1] == "True" else "ОТКЛЮЧЕНЫ"}'
        case 'courses':
            caption = f'Оповещения о курсах {"ВКЛЮЧЕНЫ" if user_settings[1] == "True" else "ОТКЛЮЧЕНЫ"}'
        case 'news':
            caption = f'Оповещения о новостях {"ВКЛЮЧЕНЫ" if user_settings[1] == "True" else "ОТКЛЮЧЕНЫ"}'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=msg.chat_id, message_id=msg.message_id,
                                 reply_markup=create_ikb_settings(user_settings))

