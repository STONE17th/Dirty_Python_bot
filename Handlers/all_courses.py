from aiogram.types import CallbackQuery, InputMediaPhoto

from Keyboards import ikb_all_courses, ikb_online_course, ikb_offline_course, ikb_individual
from Keyboards.Callback import main_menu, course_navigation
from Misc import MsgToDict, Course, PICTURES
from loader import dp, bot, course_db


@dp.callback_query_handler(main_menu.filter(button='all_courses'))
async def menu_all_courses(_, admin: bool, msg: MsgToDict):
    poster = PICTURES.get('all_courses')
    course_list = course_db.all()
    desc = f'{msg.name}, заходи позже. Пока у нас нечего тебе предложить'
    if course_list:
        course_list = [Course(course) for course in course_list]
        desc = f'{msg.name}, это все актуальные курсы на данный момент!'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=desc),
                                 chat_id=msg.chat_id, message_id=msg.message_id,
                                 reply_markup=ikb_all_courses(course_list, admin))


@dp.callback_query_handler(course_navigation.filter(menu='online'))
async def online_courses(_, admin, msg: MsgToDict):
    course = Course(course_db.select(msg.table))
    poster = course.poster
    poster = poster if poster else PICTURES.get('no_lecture')
    desc = course.info()
    keyboard = ikb_offline_course('offline', len(course), msg.table, msg.id, admin, msg) if admin else ikb_online_course(msg, msg.table)
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=desc),
                                 chat_id=msg.chat_id, message_id=msg.message_id,
                                 reply_markup=keyboard)


@dp.callback_query_handler(course_navigation.filter(menu='offline'))
async def offline_courses(_, admin: bool, msg: MsgToDict):
    course = Course(course_db.select(msg.table))
    desc = f'{msg.id + 1}/{len(course)}\n{course.lecture(msg.id, admin)}'
    keyboard = ikb_offline_course('offline', len(course), msg.table, msg.id, admin, msg)
    poster = course.lectures[msg.id].poster
    poster = poster if poster else PICTURES.get('no_lecture')
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=desc),
                                 chat_id=msg.chat_id, message_id=msg.message_id,
                                 reply_markup=keyboard)


@dp.callback_query_handler(course_navigation.filter(menu='finalize_course'))
async def finalize_course(call: CallbackQuery, msg: MsgToDict):
    course_db.finalize(msg.table, msg.id)
    await call.answer('Курс помещен в архив!' if msg.id else 'Курс завершен!', show_alert=True)
    await bot.send_message(msg.my_id, text='Вернуться в главное меню /start')


@dp.callback_query_handler(course_navigation.filter(menu='individual'))
async def individual_courses(_, msg: MsgToDict):
    desc = f'{msg.name}, если ты здесь, то видимо тебе нужны индивидуальные курсы\n' \
           f'и , да,  мы можем с тобой поработать\nСамый главный вопрос который интересует всех - ' \
           f'СКОЛЬКО? тут нет однозначного ответа, зависит от того, чем будем заниматься :)\n' \
           f'Так что давай решим этот вопрос при личном общении.\n' \
           f'Жми кнопку "Оставить заявку" и я с тобой свяжусь. Гуд ЛАК!'
    await bot.edit_message_media(media=InputMediaPhoto(media=PICTURES.get('individual_courses'), caption=desc),
                                 chat_id=msg.chat_id, message_id=msg.message_id,
                                 reply_markup=ikb_individual())


@dp.callback_query_handler(course_navigation.filter(menu='want'))
async def want_button(call: CallbackQuery, msg: MsgToDict):
    mention = "[" + msg.name + "](tg://user?id=" + str(msg.my_id) + ")"
    await bot.send_message(chat_id=409205647, text=f'{mention} хочет индивидуалочку! Отпишись ему!',
                           parse_mode='markdown')
    await call.answer(text='Заявка отправлена!\nСкоро ответит... Но это не точно :)', show_alert=True)
