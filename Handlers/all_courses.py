from aiogram.types import CallbackQuery, InputMediaPhoto

from Keyboards import create_ikb_all_courses, create_ikb_class_navigation, create_ikb_online_course, create_ikb_individual
from Keyboards.Callback import main_menu, course_navigation
from Misc import MsgToDict, Course, pictures
from loader import dp, bot, course_db


@dp.callback_query_handler(main_menu.filter(button='all_courses'))
async def user_courses(_, admin: bool, msg: MsgToDict):
    poster = pictures.all_courses
    course_list = course_db.all()
    course_list = [Course(course) for course in course_list]
    desc = f'{msg.name}, заходи позже. Пока у нас нечего тебе предложить'
    if course_list:
        desc = f'{msg.name}, это все актуальные курсы на данный момент!'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=desc),
                                 chat_id=msg.chat_id, message_id=msg.message_id,
                                 reply_markup=create_ikb_all_courses(course_list, admin))


@dp.callback_query_handler(course_navigation.filter(menu='online'))
async def online_courses(_, msg: MsgToDict):
    course = Course(course_db.select(msg.table))
    desc = course.info()
    keyboard = create_ikb_online_course(msg, msg.table)
    await bot.edit_message_media(media=InputMediaPhoto(media=course.lectures[msg.id].poster, caption=desc),
                                 chat_id=msg.chat_id, message_id=msg.message_id, reply_markup=keyboard)


@dp.callback_query_handler(course_navigation.filter(menu='offline'))
async def offline_courses(_, admin: bool, msg: MsgToDict):
    course = Course(course_db.select(msg.table))
    desc = f'{msg.id + 1}/{len(course)}\n{course.lecture(msg.id, admin)}'
    await bot.edit_message_media(media=InputMediaPhoto(media=course.lectures[msg.id].poster, caption=desc),
                                 chat_id=msg.chat_id, message_id=msg.message_id,
                                 reply_markup=create_ikb_class_navigation('offline', len(course), msg.table, msg.id,
                                                                          admin, msg))


@dp.callback_query_handler(course_navigation.filter(menu='finalize_course'))
async def offline_courses(call: CallbackQuery, msg: MsgToDict):
    course_db.finalize(msg.table)
    await call.answer(f'Курс завершен!', show_alert=True)
    await bot.send_message(msg.my_id, text='Вернуться в главное меню /start')


@dp.callback_query_handler(course_navigation.filter(menu='individual'))
async def individual_courses(_, msg: MsgToDict):
    desc = f'{msg.name}, если ты здесь, то видимо тебе нужны индивидуальные курсы\nи , да,  мы можем с тобой поработать' \
           f'\nСамый главный вопрос который интересует всех - СКОЛЬКО? ту тнет однозначного ответа, зависит от того, чем будем заниматься :)\n' \
           f'Так что давай решим этот вопрос при личном общении. Жми кнопку "Оставить заявку" и я с тобой свяжусь. Гуд ЛАК!'
    await bot.edit_message_media(media=InputMediaPhoto(media=pictures.individual_courses, caption=desc),
                                 chat_id=msg.chat_id, message_id=msg.message_id,
                                 reply_markup=create_ikb_individual())


@dp.callback_query_handler(course_navigation.filter(menu='want'))
async def want_button(call: CallbackQuery, msg: MsgToDict):
    mention = "[" + msg.name + "](tg://user?id=" + str(msg.my_id) + ")"
    await bot.send_message(chat_id=409205647, text=f'{mention} хочет индивидулочку! Отпишись ему!',
                           parse_mode='markdown')
    await call.answer(text='Заявка отправлена!\nСкоро ответит... Но это не точно :)', show_alert=True)
