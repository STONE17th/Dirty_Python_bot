from aiogram.types import InputMediaPhoto

from Keyboards import create_ikb_my_courses, create_ikb_my_course_navigation, create_ikb_notification
from Keyboards.Callback import main_menu, course_navigation
from Misc import MsgToDict, Course, PICTURES
from loader import dp, bot, course_db, user_db


@dp.callback_query_handler(main_menu.filter(button='notification'))
async def notification_menu(_, admin: bool, msg: MsgToDict):
    poster = PICTURES.get('no_lecture')
    caption = 'Выбери тип оповещения: Новость или стрим'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=msg.chat_id,
                                 message_id=msg.message_id,
                                 reply_markup=create_ikb_notification())


@dp.callback_query_handler(main_menu.filter(button='stream'))
async def create_stream(_, msg: MsgToDict):
    poster = PICTURES.get('no_lecture')
    caption = 'Выбери тип оповещения: Новость или стрим'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=msg.chat_id,
                                 message_id=msg.message_id,
                                 reply_markup=create_ikb_notification())


@dp.callback_query_handler(main_menu.filter(button='news'))
async def create_news(_, msg: MsgToDict):
    poster = PICTURES.get('no_lecture')
    caption = 'Выбери тип оповещения: Новость или стрим'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=msg.chat_id,
                                 message_id=msg.message_id,
                                 reply_markup=create_ikb_notification())