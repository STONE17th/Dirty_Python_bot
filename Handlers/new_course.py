from loader import dp, db
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from Handlers.States import NewCourse
from Keyboards.Standart import kb_cancel


@dp.message_handler(commands=['new_course'], state=None)
async def new_course_catch(message: Message):
    await message.answer(text='Введите название курса:', reply_markup=kb_cancel)
    await NewCourse.name.set()

@dp.message_handler(state=NewCourse.name)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'name': message.text})
    await message.answer(text='Введите описание курса:', reply_markup=kb_cancel)
    await NewCourse.next()

@dp.message_handler(state=NewCourse.desc)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'desc': message.text})
    await message.answer(text='Введите URL для облака курса:', reply_markup=kb_cancel)
    await NewCourse.next()

@dp.message_handler(state=NewCourse.url_course)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'url_course': message.text})
    await message.answer(text='Введите обложку для курса:', reply_markup=kb_cancel)
    await NewCourse.next()

@dp.message_handler(content_types='photo', state=NewCourse.poster)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'poster': message.photo[0].file_id})
    await message.answer(text='Введите количество мест:', reply_markup=kb_cancel)
    await NewCourse.next()

@dp.message_handler(state=NewCourse.quantity)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'quantity': message.text})
    await message.answer(text='Введите цену курса:', reply_markup=kb_cancel)
    await NewCourse.next()

@dp.message_handler(state=NewCourse.price)
async def price_catch(message: Message, state: FSMContext):
    price = message.text.replace(',', '.')
    await state.update_data({'price': float(price)})
    data = await state.get_data()
    db.add_new_course(data)
    await state.reset_data()
    await state.finish()
    print(data)