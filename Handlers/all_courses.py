# from loader import *
# from aiogram.types import Message, CallbackQuery, InputMediaPhoto
# from Keyboards import create_ikb_my_courses, create_ikb_all_courses, create_ikb_all_classes
# import config
# from Keyboards.Callback import main_menu
# from Misc import MsgToDict, Course
#
#
# @dp.callback_query_handler(main_menu.filter(button='all_courses'))
# async def start_command(call: CallbackQuery, admin: bool):
#     msg = MsgToDict(call)
#     poster = config.all_courses
#     desc = f'{msg.name}, это все актуальные курсы на данный момент!' if None not in db.user_courses(
#         msg.my_id) else f'{msg.name}, заходи позже. Пока у нас нечего тебе предложить'
#     await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=desc),
#                                  chat_id=msg.chat_id, message_id=msg.message_id,
#                                  reply_markup=create_ikb_all_courses(admin))
#
#
# # reply_markup
# @dp.callback_query_handler(main_menu.filter(menu='target_course'))
# async def start_command(call: CallbackQuery):
#     course = Course(db.whole_course(call.data.split(':')[-1]))
#     msg = MsgToDict(call)
#     poster = config.all_courses
#     desc = f'{msg.name}, это твои курсы!' if None not in db.user_courses(
#         msg.chat_id) else f'{msg.name}, у тебя нет активных курсов!'
#     await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=desc),
#                                  chat_id=msg.chat_id, message_id=msg.message_id,
#                                  reply_markup=create_ikb_all_classes(msg.data[-1]))
