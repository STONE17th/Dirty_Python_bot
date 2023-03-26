from loader import dp
from aiogram.types import Message
from Keyboards.Standart.main_kb import remover


@dp.message_handler(commands=['help'])
async def help_command(message: Message):
    name = await help_helper(message)
    await message.answer(f'Бог поможет, {name}', reply_markup=remover)


async def help_helper(message: Message):
    user = message.from_user.first_name
    user = 'Уважаемый ' + user
    return user