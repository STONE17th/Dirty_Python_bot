from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, InputMediaPhoto

import config
from Handlers.States import NewTask
from Keyboards import create_ikb_confirm, create_ikb_list_navigation, create_ikb_select_option
from Keyboards.Callback import main_menu, task_navigation, confirm_request
from Keyboards.Standart import kb_cancel, create_kb_task_type, kb_task_level
from Misc import MsgToDict, CurrentTask
from loader import *


@dp.callback_query_handler(main_menu.filter(button='tasks'))
async def select_tasks_type(call: CallbackQuery, admin: bool):
    msg = MsgToDict(call)
    poster = config.task_main
    description = f'{msg.name}, выбери тему!'
    btn_list = [btn[0] for btn in set(db.collect_tasks('task_type'))]
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=description),
                                 chat_id=msg.chat_id, message_id=msg.message_id,
                                 reply_markup=create_ikb_select_option('type', admin, btn_list))


@dp.callback_query_handler(task_navigation.filter(menu='type'))
async def select_tasks_type(call: CallbackQuery, admin: bool):
    msg = MsgToDict(call)
    btn_list = [btn[0] for btn in set(db.collect_tasks('task_level', msg.type))]
    btn_list = [btn for btn in ['easy', 'normal', 'hard'] if btn in btn_list]
    poster = config.task_main
    description = f'{msg.name}, выбери уровень сложности!'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=description),
                                 chat_id=msg.chat_id, message_id=msg.message_id,
                                 reply_markup=create_ikb_select_option('level', admin, btn_list, msg.type))


@dp.callback_query_handler(task_navigation.filter(menu='level'))
@dp.callback_query_handler(task_navigation.filter(menu='tasks'))
async def select_tasks_type(call: CallbackQuery, admin: bool):
    msg = MsgToDict(call)
    task_list = db.select_tasks(msg.type, msg.level)
    current_task = CurrentTask(task_list[msg.id])
    await bot.edit_message_media(
        media=InputMediaPhoto(media=current_task.poster, caption=current_task.task(msg.id, len(task_list))),
        chat_id=msg.chat_id, message_id=msg.message_id,
        reply_markup=create_ikb_list_navigation('tasks', admin, msg.type, msg.level, msg.id, len(task_list)))


@dp.callback_query_handler(main_menu.filter(button='add_task'))
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
        user_list = [user[0] for user in db.select_users(alerts_news='True')]
        print(user_list)
        for user in user_list:
            try:
                await bot.send_message(user,
                                       f'Добавлена новая задача на {data.get("task_type")}, сложности {data.get("task_level")}')
            except:
                print('Юзер не в ресурсе')
    else:
        await call.answer('Отмена')
    await state.reset_data()
    await state.finish()


@dp.callback_query_handler(task_navigation.filter(menu='task_delete'))
async def add_task_command(call: CallbackQuery):
    msg = MsgToDict(call)
    task_id = db.select_tasks(msg.type, msg.level)[msg.id][0]
    await bot.send_message(msg.chat_id, text='Точно удалить задачу?',
                           reply_markup=create_ikb_confirm('delete', task_id))


@dp.callback_query_handler(confirm_request.filter(menu='delete'))
async def add_task_command(call: CallbackQuery):
    msg = MsgToDict(call)
    if msg.data[-1] == 'yes':
        db.delete_task(int(msg.data[-2]))
        await call.answer('Задача удалена', show_alert=True)
    await bot.send_message(msg.chat_id, text='Возврат в главное меню /start')
