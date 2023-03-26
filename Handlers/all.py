from loader import dp
from aiogram.types import Message


@dp.message_handler()
async def help_command(message: Message):
    await message.answer(f'{message.from_user.first_name}, смотри че поймал - '
                         f'{message.text}')