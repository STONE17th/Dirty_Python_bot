from loader import dp, bot, user_db, settings_db
from aiogram.types import CallbackQuery, InputMediaPhoto
from Keyboards import create_ikb_settings, create_ikb_links
from Keyboards.Callback import main_menu, settings_option
from Misc import MsgToDict, PICTURES


@dp.callback_query_handler(main_menu.filter(button='settings'))
async def my_settings(_, msg: MsgToDict):
    poster = PICTURES.get('settings')
    user_settings = user_db.settings(msg.my_id)
    desc = 'Это твои настройки'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=desc),
                                 chat_id=msg.chat_id,
                                 message_id=msg.message_id,
                                 reply_markup=create_ikb_settings(user_settings))


@dp.callback_query_handler(settings_option.filter(menu='settings'))
async def select_settings(_, msg: MsgToDict):
    poster = PICTURES.get('start_poster')
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
                                 chat_id=msg.chat_id,
                                 message_id=msg.message_id,
                                 reply_markup=create_ikb_settings(user_settings))


@dp.callback_query_handler(main_menu.filter(button='links'))
async def links_list(_, msg: MsgToDict):
    poster = PICTURES.get('start_poster')
    caption = 'Это твои настройки'
    btn_list = [link[3] for link in settings_db.load(type_set='link')]
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=msg.chat_id,
                                 message_id=msg.message_id,
                                 reply_markup=create_ikb_links())