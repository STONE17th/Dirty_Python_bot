from loader import dp
from aiogram.types import Message
from Handlers.help import help_helper
from Keyboards import kb_main


@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    name = await help_helper(message)
    await message.answer(f'{name}, да, да, я готов работать\nВыбери уже че-нить', reply_markup=kb_main)
