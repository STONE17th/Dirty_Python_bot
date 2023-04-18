from loader import dp, db, bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from Handlers.States import NewCourse
from Keyboards.Standart import kb_cancel
from Keyboards import create_ikb_confirm
from Keyboards.Callback import main_menu


# @dp.message_handler(commands=['add_new_course'], state=None)
@dp.callback_query_handler(main_menu.filter(button='new_course'), state=None)
async def new_course_catch(call: CallbackQuery):
    await bot.send_message(call.message.chat.id, 'Введите название курса:', reply_markup=kb_cancel)
    await NewCourse.course_name.set()


@dp.message_handler(state=NewCourse.course_name)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'course_name': message.text})
    await message.answer(text='Введите название таблицы:', reply_markup=kb_cancel)
    await NewCourse.next()

@dp.message_handler(state=NewCourse.table_name)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'table_name': message.text})
    await message.answer(text='Введите описание курса:', reply_markup=kb_cancel)
    await NewCourse.next()


@dp.message_handler(state=NewCourse.course_desc)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'course_desc': message.text})
    await message.answer(text='Введите URL для облака курса:', reply_markup=kb_cancel)
    await NewCourse.next()


@dp.message_handler(state=NewCourse.course_url)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'course_url': message.text})
    await message.answer(text='Введите обложку для курса:', reply_markup=kb_cancel)
    await NewCourse.next()


@dp.message_handler(content_types='photo', state=NewCourse.poster)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'poster': message.photo[0].file_id})
    await message.answer(text='Введите цену курса:', reply_markup=kb_cancel)
    await NewCourse.next()


@dp.message_handler(state=NewCourse.price)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'price': message.text})
    await message.answer(text='Введите дату начала курса:', reply_markup=kb_cancel)
    await NewCourse.next()


@dp.message_handler(state=NewCourse.start_date)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'start_date': message.text})
    data = await state.get_data()
    caption = f"Название: {data.get('course_name')}\n\nНазвание таблицы: {data.get('table_name')}\n\nОписание: " \
              f"{data.get('course_desc')}\n\nРабочая папка: {data.get('course_url')}\n\nЦена курса: " \
              f"{data.get('price')}\n\nДата начала: {data.get('start_date')}"
    await bot.send_photo(chat_id=message.from_user.id, photo=data.get('poster'), caption=caption,
                         reply_markup=create_ikb_confirm('course'))
    await NewCourse.next()


@dp.callback_query_handler(state=NewCourse.course_confirm)
async def start_command(call: CallbackQuery, state: FSMContext):
    if call.data.split(':')[-1] == 'yes':
        data = await state.get_data()
        db.add_new_course(data)
        await call.answer(f'Курс {data.get("course_name")} добавлен в БД')
    else:
        await call.answer('Отмена')
    await bot.send_message(call.message.chat.id, text='Вернуться в главное меню /start')
    await state.reset_data()
    await state.finish()
