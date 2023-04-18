from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.middlewares import BaseMiddleware

from loader import dp, db
from config import admins_id


class Administrator(BaseMiddleware):
    async def on_process_message(self, message: Message, data: dict):
        for admin in admins_id:
            if message.from_user.id == admin:
                data['admin'] = True
                break
        else:
            data['admin'] = False

    async def on_process_callback_query(self, call: CallbackQuery, data: dict):
        for admin in admins_id:
            if call.message.from_user.id == admin:
                data['admin'] = True
                break
        else:
            data['admin'] = False