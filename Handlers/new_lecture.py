from loader import dp, bot, course_db, lecture_db
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from Handlers.States import NewLecture
from Keyboards.Standart import kb_cancel
from Keyboards import create_ikb_confirm, create_ikb_class_navigation
from Keyboards.Callback import course_navigation
from Misc import MsgToDict


@dp.callback_query_handler(course_navigation.filter(menu='edit_class'), state=None)
async def new_course_catch(admin: bool, msg: MsgToDict, state: FSMContext):
    if admin:
        await state.update_data({'table': msg.table})
        await state.update_data({'id': msg.id})
        await bot.send_message(msg.my_id, 'Введите название лекции:', reply_markup=kb_cancel)
        await NewLecture.name.set()
    else:
        await bot.send_message(msg.my_id, 'Извините, у вас нет прав для этой команды')


@dp.message_handler(state=NewLecture.name)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'name': message.text})
    await message.answer(text='Введите описание лекции:', reply_markup=kb_cancel)
    await NewLecture.next()

@dp.message_handler(state=NewLecture.desc)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'desc': message.text})
    await message.answer(text='Отправьте обложку лекции:', reply_markup=kb_cancel)
    await NewLecture.next()

@dp.message_handler(content_types=['photo', 'text'], state=NewLecture.poster)
async def name_catch(message: Message, state: FSMContext, msg: MsgToDict):
    # data = await state.get_data()
    photo = course_db.poster(msg.table)
    if 'photo' in message:
        photo = message.photo[0].file_id
    await state.update_data({'poster': photo})
    await message.answer(text='Введите ссылку на видео:', reply_markup=kb_cancel)
    await NewLecture.next()
@dp.message_handler(state=NewLecture.video)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'video': message.text})
    await message.answer(text='Введите ссылку на конспект:', reply_markup=kb_cancel)
    await NewLecture.next()


@dp.message_handler(state=NewLecture.compendium)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'compendium': message.text})
    await message.answer(text='Введите цену за лекцию:', reply_markup=kb_cancel)
    await NewLecture.next()


@dp.message_handler(state=NewLecture.price)
async def name_catch(message: Message, state: FSMContext, msg: MsgToDict):
    await state.update_data({'price': message.text})
    data = await state.get_data()
    caption = f"Название: {data.get('name')}\nОписание: {data.get('desc')}\n\n" \
              f"Ссылка на видео: {data.get('video')}\nСсылка на конспект: {data.get('compendium')}" \
              f"\n\nЦена курса: {data.get('price')}"
    await bot.send_photo(chat_id=msg.my_id, photo=data.get('poster'), caption=caption,
                         reply_markup=create_ikb_confirm('class', 'confirm'))
    await NewLecture.next()


@dp.callback_query_handler(state=NewLecture.confirm)
async def start_command(call: CallbackQuery, state: FSMContext, msg: MsgToDict):
    if call.data.split(':')[-1] == 'yes':
        data = await state.get_data()
        lecture_db.update(data)
        await call.answer(f'Лекция {data.get("name")} внесена в БД')
    else:
        await call.answer('Отмена')
    await bot.send_message(msg.my_id, text='Вернуться в главное меню /start')
    await state.reset_data()
    await state.finish()