# from loader import dp, db, bot
# from aiogram.types import Message, CallbackQuery
# from aiogram.dispatcher import FSMContext
# from Handlers.States import NewCourse
# from Keyboards.Standart import kb_cancel
# from Keyboards import create_ikb_confirm
# from Keyboards.Callback import main_menu
#
#
# # @dp.message_handler(commands=['add_new_course'], state=None)
# @dp.callback_query_handler(main_menu.filter(button='new_course'), state=None)
# async def new_course_catch(call: CallbackQuery, admin: bool):
#     if admin:
#         await bot.send_message(call.message.chat.id, 'Введите название курса:', reply_markup=kb_cancel)
#         await NewCourse.name.set()
#     else:
#         await bot.send_message(call.message.chat.id, 'Извините, у вас нет прав для этой команды')
#
#
# @dp.message_handler(state=NewCourse.name)
# async def name_catch(message: Message, state: FSMContext):
#     await state.update_data({'name': message.text})
#     await message.answer(text='Введите название таблицы:', reply_markup=kb_cancel)
#     await NewCourse.next()
#
# @dp.message_handler(state=NewCourse.table)
# async def name_catch(message: Message, state: FSMContext):
#     await state.update_data({'table': message.text})
#     await message.answer(text='Введите количество лекций:', reply_markup=kb_cancel)
#     await NewCourse.next()
#
# @dp.message_handler(state=NewCourse.quantity)
# async def name_catch(message: Message, state: FSMContext):
#     await state.update_data({'quantity': message.text})
#     await message.answer(text='Введите описание курса:', reply_markup=kb_cancel)
#     await NewCourse.next()
# @dp.message_handler(state=NewCourse.desc)
# async def name_catch(message: Message, state: FSMContext):
#     await state.update_data({'desc': message.text})
#     await message.answer(text='Введите URL для облака курса:', reply_markup=kb_cancel)
#     await NewCourse.next()
#
#
# @dp.message_handler(state=NewCourse.url)
# async def name_catch(message: Message, state: FSMContext):
#     await state.update_data({'url': message.text})
#     await message.answer(text='Введите обложку для курса:', reply_markup=kb_cancel)
#     await NewCourse.next()
#
#
# @dp.message_handler(content_types='photo', state=NewCourse.poster)
# async def name_catch(message: Message, state: FSMContext):
#     await state.update_data({'poster': message.photo[0].file_id})
#     await message.answer(text='Введите цену курса:', reply_markup=kb_cancel)
#     await NewCourse.next()
#
#
# @dp.message_handler(state=NewCourse.price)
# async def name_catch(message: Message, state: FSMContext):
#     await state.update_data({'price': message.text})
#     await message.answer(text='Введите дату начала курса:', reply_markup=kb_cancel)
#     await NewCourse.next()
#
#
# @dp.message_handler(state=NewCourse.start_date)
# async def name_catch(message: Message, state: FSMContext):
#     await state.update_data({'start_date': message.text})
#     data = await state.get_data()
#     caption = f"Название: {data.get('name')}\n\nНазвание таблицы: {data.get('name')}\n\nПродолжительность: {data.get('quantity')}\n\n" \
#               f"Описание: {data.get('desc')}\n\nРабочая папка: {data.get('url')}\n\nЦена курса: " \
#               f"{data.get('price')}\n\nДата начала: {data.get('start_date')}"
#     await bot.send_photo(chat_id=message.from_user.id, photo=data.get('poster'), caption=caption,
#                          reply_markup=create_ikb_confirm('course', 'confirm'))
#     await NewCourse.next()
#
#
# @dp.callback_query_handler(state=NewCourse.course_confirm)
# async def start_command(call: CallbackQuery, state: FSMContext):
#     if call.data.split(':')[-1] == 'yes':
#         data = await state.get_data()
#         db.add_new_course(data)
#         await call.answer(f'Курс {data.get("name")} добавлен в БД')
#     else:
#         await call.answer('Отмена')
#     await bot.send_message(call.message.chat.id, text='Вернуться в главное меню /start')
#     await state.reset_data()
#     await state.finish()
