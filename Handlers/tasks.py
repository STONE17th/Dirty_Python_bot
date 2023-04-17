from loader import *
from aiogram.dispatcher import FSMContext
from Handlers.States import NewCourse, NewTask
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, InputMediaPhoto
from Keyboards import create_ikb_confirm, create_ikb_task_type, create_ikb_task_level, create_ikb_navigation
from Keyboards.Standart import kb_cancel, create_kb_task_type, kb_task_level
from Keyboards.Callback import main_menu, select_task, navigation_menu
import config


@dp.callback_query_handler(main_menu.filter(button='tasks'))
async def select_tasks_type(call: CallbackQuery):
    name = call.from_user.first_name
    poster = config.task_main
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    description = f'{name}, выбери тему!'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=description),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_task_type())


@dp.callback_query_handler(select_task.filter(menu='select_task_type'))
async def select_tasks_type(call: CallbackQuery):
    name = call.from_user.first_name
    poster = config.task_main
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    description = f'{name}, выбери уровень сложности!'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=description),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_task_level(call.data.split(':')[-2]))


@dp.callback_query_handler(navigation_menu.filter(menu='navigation'))
@dp.callback_query_handler(select_task.filter(menu='select_task_level'))
async def navigation_tasks(call: CallbackQuery):
    task_type = call.data.split(':')[-2]
    task_level = call.data.split(':')[-1]
    task_list = db.select_tasks(task_type, task_level)
    count_task = len(task_list)
    curr_id = int(call.data.split(':')[-3]) if call.data.split(':')[-3].isdigit() else 0
    name = call.from_user.first_name
    poster = config.task_main
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    description = f'{curr_id + 1}/{count_task}\n\nТема: {task_type}\nСложность: {task_level}\n\n{task_list[curr_id][-1]}'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=description),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_navigation(curr_id, task_type, task_level))


@dp.message_handler(commands=['add_new_task'], state=None)
async def add_task_command(message: Message):
    await message.answer(text='Введите тип задачи или введите новый:',
                         reply_markup=create_kb_task_type())
    await NewTask.task_type.set()


@dp.message_handler(state=NewTask.task_type)
async def input_task_type(message: Message, state: FSMContext):
    await state.update_data({'task_type': message.text})
    await message.answer(text='Введите сложность задачи:', reply_markup=kb_task_level)
    await NewTask.next()


@dp.message_handler(state=NewTask.task_level)
async def input_task_level(message: Message, state: FSMContext):
    if message.text in ['easy', 'normal', 'hard']:
        await state.update_data({'task_level': message.text})
        await message.answer(text='Введите условие задачи:', reply_markup=kb_cancel)
        await NewTask.next()
    else:
        await message.answer(text='Введите сложность задачи:', reply_markup=kb_task_level)


@dp.message_handler(state=NewTask.task_value)
async def task_confirm(message: Message, state: FSMContext):
    await state.update_data({'task_value': message.text})
    data = await state.get_data()
    caption = f'Тип задачи: {data.get("task_type")}\nСложность: {data.get("task_level")}' \
              f'\nУсловие: {data.get("task_value")}\n\nСохранить?'
    await message.answer(text=caption, reply_markup=create_ikb_confirm('task'))
    await NewTask.next()


# @dp.callback_query_handler(main_menu.filter(menu='task_confirm'), state=NewTask.task_confirm)
@dp.callback_query_handler(state=NewTask.task_confirm)
async def start_command(call: CallbackQuery, state: FSMContext):
    if call.data.split(':')[-1] == 'yes':
        data = await state.get_data()
        db.add_new_task((data.get("task_type"), data.get("task_level"), data.get("task_value")))
        await call.answer('Задача добавлена')
    else:
        await call.answer('Отмена')
    await state.reset_data()
    await state.finish()
