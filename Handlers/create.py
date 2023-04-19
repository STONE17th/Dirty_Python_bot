from loader import *
from aiogram.types import CallbackQuery
from Keyboards.Callback import main_menu
from Misc import MsgToDict


@dp.callback_query_handler(main_menu.filter(button='create'))
async def create_menu(call: CallbackQuery):
    msg = MsgToDict(call)