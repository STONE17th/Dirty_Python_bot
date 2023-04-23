from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from Handlers.States import Posters
from Keyboards.Standart import kb_next_pict
from loader import dp, bot
from Misc import save_posters


@dp.message_handler(commands=['setup_pict'], state=None)
async def set_start_poster(message: Message, admin: bool):
    if admin:
        await bot.send_message(message.from_user.id, 'Начальная заставка: ', reply_markup=kb_next_pict)
        await Posters.start_poster.set()
    else:
        await bot.send_message(message.from_user.id, 'Извините, у вас нет прав для этой команды')


@dp.message_handler(content_types=['photo', 'text'], state=Posters.start_poster)
async def set_start_poster(message: Message, state: FSMContext):
    if message.text != 'Дальше':
        await state.update_data({'start_poster': message.photo[0].file_id})
    await bot.send_message(message.from_user.id, 'Задачи: ', reply_markup=kb_next_pict)
    await Posters.next()


@dp.message_handler(content_types=['photo', 'text'], state=Posters.task_main)
async def set_start_poster(message: Message, state: FSMContext):
    if message.text != 'Дальше':
        await state.update_data({'task_main': message.photo[0].file_id})
    await bot.send_message(message.from_user.id, 'Мои курсы: ', reply_markup=kb_next_pict)
    await Posters.next()


@dp.message_handler(content_types=['photo', 'text'], state=Posters.my_courses)
async def set_start_poster(message: Message, state: FSMContext):
    if message.text != 'Дальше':
        await state.update_data({'my_courses': message.photo[0].file_id})
    await bot.send_message(message.from_user.id, 'Все курсы: ', reply_markup=kb_next_pict)
    await Posters.next()


@dp.message_handler(content_types=['photo', 'text'], state=Posters.all_courses)
async def set_start_poster(message: Message, state: FSMContext):
    if message.text != 'Дальше':
        await state.update_data({'all_courses': message.photo[0].file_id})
    await bot.send_message(message.from_user.id, 'Нет лекции: ', reply_markup=kb_next_pict)
    await Posters.next()


@dp.message_handler(content_types=['photo', 'text'], state=Posters.no_lecture)
async def set_start_poster(message: Message, state: FSMContext):
    if message.text != 'Дальше':
        await state.update_data({'no_lecture': message.photo[0].file_id})
    await bot.send_message(message.from_user.id, 'Легкая задача: ', reply_markup=kb_next_pict)
    await Posters.next()


@dp.message_handler(content_types=['photo', 'text'], state=Posters.task_easy)
async def set_start_poster(message: Message, state: FSMContext):
    if message.text != 'Дальше':
        await state.update_data({'task_easy': message.photo[0].file_id})
    await bot.send_message(message.from_user.id, 'Средняя задача: ', reply_markup=kb_next_pict)
    await Posters.next()


@dp.message_handler(content_types=['photo', 'text'], state=Posters.task_normal)
async def set_start_poster(message: Message, state: FSMContext):
    if message.text != 'Дальше':
        await state.update_data({'task_normal': message.photo[0].file_id})
    await bot.send_message(message.from_user.id, 'Тяжелая задача: ', reply_markup=kb_next_pict)
    await Posters.next()

@dp.message_handler(content_types=['photo', 'text'], state=Posters.task_hard)
async def set_start_poster(message: Message, state: FSMContext):
    if message.text != 'Дальше':
        await state.update_data({'task_hard': message.photo[0].file_id})
    await bot.send_message(message.from_user.id, 'Настройки: ', reply_markup=kb_next_pict)
    await Posters.next()


@dp.message_handler(content_types=['photo', 'text'], state=Posters.settings)
async def set_start_poster(message: Message, state: FSMContext):
    if message.text != 'Дальше':
        await state.update_data({'settings': message.photo[0].file_id})
    await bot.send_message(message.from_user.id, 'Индивидуалочки: ', reply_markup=kb_next_pict)
    await Posters.next()


@dp.message_handler(content_types=['photo', 'text'], state=Posters.individual_courses)
async def set_start_poster(message: Message, state: FSMContext):
    if message.text != 'Дальше':
        await state.update_data({'individual_courses': message.photo[0].file_id})
    data = await state.get_data()
    print(data)
    save_posters(data)
    await state.reset_data()
    await state.finish()
    await bot.send_message(message.from_user.id, 'Заставки обновлены. Главное меню /start',
                           reply_markup=ReplyKeyboardRemove())
