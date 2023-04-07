from loader import dp, bot
from aiogram.types import Message, CallbackQuery
from Keyboards import kb_main, create_clicker, ikb_start
from data import counter
from Keyboards.Callback import main_menu


@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    await message.answer('Привет, я кликер, жмакай кнопку', reply_markup=ikb_start)
    # bot.send_photo()


@dp.message_handler(commands=['restart'])
async def clicker(message: Message):
    counter[message.from_user.id] = 0
    await message.answer(f'Ты сбросил свой счетчик\nНачинай заново', reply_markup=create_clicker(message))
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)


@dp.message_handler()
async def clicker(message: Message):
    print(counter)
    if message.text.isdigit():
        counter[message.from_user.id] = int(counter.get(message.from_user.id, 0)) + 1
        await message.answer(f'Ты нажал {counter.get(message.from_user.id, 0)} раз',
                             reply_markup=create_clicker(message))
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)

@dp.callback_query_handler(main_menu.filter(menu='main'))
async def inline_start(callback: CallbackQuery):
    data = callback.data.split(':')[-1]
    current_chat = callback.from_user.id
    current_message = callback.message.message_id
    await bot.edit_message_text(chat_id=current_chat, message_id=current_message,
                          text=f'Нажата кнопка {data}', reply_markup=ikb_start)

