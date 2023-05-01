from aiogram.types import InputMediaPhoto

from Keyboards import ikb_settings, ikb_links
from Keyboards.Callback import main_menu, settings
from Misc import MsgToDict, PICTURES
from loader import dp, bot, user_db


@dp.callback_query_handler(main_menu.filter(button='settings'))
async def my_settings(_, msg: MsgToDict):
    poster = PICTURES.get('settings')
    desc = 'Это твои настройки'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=desc),
                                 chat_id=msg.chat_id,
                                 message_id=msg.message_id,
                                 reply_markup=ikb_settings(msg))


@dp.callback_query_handler(settings.filter(menu='settings'))
async def select_settings(_, msg: MsgToDict):
    poster = PICTURES.get('settings')
    if msg.button != 'admin':
        active = user_db.switch_alert(msg.my_id, msg.button)
    else:
        active = user_db.switch_admin(msg.my_id)
    status = "ВКЛЮЧЕНЫ" if active[0] == 1 else "ОТКЛЮЧЕНЫ"
    match msg.button:
        case 'stream':
            caption = f'Оповещения на все стримы {status}'
        case 'courses':
            caption = f'Оповещения о курсах {status}'
        case 'news':
            caption = f'Оповещения о новостях {status}'
        case _:
            caption = f'Права администратора: {status}'

    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=msg.chat_id,
                                 message_id=msg.message_id,
                                 reply_markup=ikb_settings(msg))


@dp.callback_query_handler(main_menu.filter(button='links'))
async def links_list(_, msg: MsgToDict):
    poster = PICTURES.get('links')
    caption = 'Полезные ссылки проекта Dirty Python'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=msg.chat_id,
                                 message_id=msg.message_id,
                                 reply_markup=ikb_links())
