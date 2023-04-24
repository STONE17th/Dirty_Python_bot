from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from Handlers.States import NewCourse
from Keyboards import create_ikb_confirm
from Keyboards.Callback import main_menu
from Keyboards.Standart import kb_cancel
from Misc import MsgToDict
from loader import dp, bot, course_db, user_db


@dp.callback_query_handler(main_menu.filter(button='new_course'), state=None)
async def name_catch(_, admin: bool, msg: MsgToDict):
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
    caption = f"Название: {data.get('name')}\n\nНазвание таблицы: {data.get('name')}\n\n" \
              f"Продолжительность: {data.get('quantity')}\n\n" \
              f"Описание: {data.get('desc')}\n\nРабочая папка: {data.get('url')}\n" \
              f"Телеграм-чат: {data.get('tg_chat')}\n\nЦена курса: " \
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
        user_list = [user[0] for user in user_db.select(alerts_courses='True')]
        caption = f'Курс {data.get("name")} добавлен в список Dirty Python Bot\n' \
                  f'Если не хочешь получать уведомления о курсах и лекциях - '\
                  f'можешь отключить уведомления в настройках'
        for user in user_list:
            try:
                await bot.send_message(user, text=caption)
            except IOError:
                print(f'у {user} нет чата с ботом')
    else:
        await call.answer('Отмена')

    await bot.send_message(call.message.chat.id, text='Вернуться в главное меню /start')
    await state.reset_data()
    await state.finish()
