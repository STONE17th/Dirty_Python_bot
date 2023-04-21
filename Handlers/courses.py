from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, InputMediaPhoto

from Handlers.States import NewCourse
from Keyboards import create_ikb_all_courses, create_ikb_confirm, create_ikb_class_navigation, create_ikb_online_course
from Keyboards.Callback import main_menu, course_navigation
from Keyboards.Standart import kb_cancel
from Misc import MsgToDict, Course, Lecture, pictures
from loader import dp, bot, course_db


@dp.callback_query_handler(main_menu.filter(button='all_courses'))
async def user_courses(call: CallbackQuery, admin: bool, msg: MsgToDict):
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
async def online_courses(call: CallbackQuery, admin: bool, msg: MsgToDict):
    course = Course(course_db.select(msg.table))
    desc = course.info()
    keyboard = create_ikb_online_course(msg, msg.table, msg.id)
    await bot.edit_message_media(media=InputMediaPhoto(media=course.lectures[msg.id].poster, caption=desc),
                                 chat_id=msg.chat_id, message_id=msg.message_id, reply_markup=keyboard)


@dp.callback_query_handler(course_navigation.filter(menu='offline'))
async def offline_courses(call: CallbackQuery, admin: bool, msg: MsgToDict):
    course = Course(course_db.select(msg.table))
    desc = f'{msg.id + 1}/{course.size}\n{course.lecture(msg.id, admin)}'
    await bot.edit_message_media(media=InputMediaPhoto(media=course.lectures[msg.id].poster, caption=desc),
                                 chat_id=msg.chat_id, message_id=msg.message_id,
                                 reply_markup=create_ikb_class_navigation('offline', course.size, msg.table, msg.id,
                                                                          admin, msg))


@dp.callback_query_handler(course_navigation.filter(menu='finalize_course'))
async def offline_courses(call: CallbackQuery, admin: bool, msg: MsgToDict):
    course_db.finalize(msg.table)
    await call.answer(f'Курс завершен!', show_alert=True)
    await bot.send_message(msg.my_id, text='Вернуться в главное меню /start')


@dp.callback_query_handler(main_menu.filter(button='new_course'), state=None)
async def name_catch(call: CallbackQuery, admin: bool, msg: MsgToDict):
    if admin:
        await bot.send_message(msg.my_id, 'Введите название курса:', reply_markup=kb_cancel)
        await NewCourse.name.set()
    else:
        await bot.send_message(msg.my_id, 'Извините, у вас нет прав для этой команды')


@dp.message_handler(state=NewCourse.name)
async def table_catch(message: Message, state: FSMContext):
    await state.update_data({'name': message.text})
    await message.answer(text='Введите название таблицы:', reply_markup=kb_cancel)
    await NewCourse.next()


@dp.message_handler(state=NewCourse.table)
async def quantity_catch(message: Message, state: FSMContext):
    await state.update_data({'table': message.text})
    await message.answer(text='Введите количество лекций:', reply_markup=kb_cancel)
    await NewCourse.next()


@dp.message_handler(state=NewCourse.quantity)
async def desc_catch(message: Message, state: FSMContext):
    await state.update_data({'quantity': message.text})
    await message.answer(text='Введите описание курса:', reply_markup=kb_cancel)
    await NewCourse.next()


@dp.message_handler(state=NewCourse.desc)
async def url_catch(message: Message, state: FSMContext):
    await state.update_data({'desc': message.text})
    await message.answer(text='Введите URL для облака курса:', reply_markup=kb_cancel)
    await NewCourse.next()


@dp.message_handler(state=NewCourse.url)
async def tg_catch(message: Message, state: FSMContext):
    await state.update_data({'url': message.text})
    await message.answer(text='Введите ссылку на рабочую группу в TG:', reply_markup=kb_cancel)
    await NewCourse.next()


@dp.message_handler(state=NewCourse.tg_chat)
async def poster_catch(message: Message, state: FSMContext):
    await state.update_data({'tg_chat': message.text})
    await message.answer(text='Введите обложку для курса:', reply_markup=kb_cancel)
    await NewCourse.next()


@dp.message_handler(content_types='photo', state=NewCourse.poster)
async def price_catch(message: Message, state: FSMContext):
    await state.update_data({'poster': message.photo[0].file_id})
    await message.answer(text='Введите цену курса:', reply_markup=kb_cancel)
    await NewCourse.next()


@dp.message_handler(state=NewCourse.price)
async def start_catch(message: Message, state: FSMContext):
    await state.update_data({'price': message.text})
    await message.answer(text='Введите дату начала курса:', reply_markup=kb_cancel)
    await NewCourse.next()


@dp.message_handler(state=NewCourse.start_date)
async def confirm_new_course(message: Message, state: FSMContext):
    await state.update_data({'start_date': message.text})
    data = await state.get_data()
    caption = f"Название: {data.get('name')}\n\nНазвание таблицы: {data.get('name')}\n\nПродолжительность: {data.get('quantity')}\n\n" \
              f"Описание: {data.get('desc')}\n\nРабочая папка: {data.get('url')}\nТелеграм-чат: {data.get('tg_chat')}\n\nЦена курса: " \
              f"{data.get('price')}\n\nДата начала: {data.get('start_date')}"
    await bot.send_photo(chat_id=message.from_user.id, photo=data.get('poster'), caption=caption,
                         reply_markup=create_ikb_confirm('course', 'confirm'))
    await NewCourse.next()


@dp.callback_query_handler(state=NewCourse.course_confirm)
async def save_new_course(call: CallbackQuery, state: FSMContext):
    if call.data.split(':')[-1] == 'yes':
        data = await state.get_data()
        course_db.add(data)
        await call.answer(f'Курс {data.get("name")} добавлен в БД')
    else:
        await call.answer('Отмена')
    await bot.send_message(call.message.chat.id, text='Вернуться в главное меню /start')
    await state.reset_data()
    await state.finish()
