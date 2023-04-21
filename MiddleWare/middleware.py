from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from Misc import MsgToDict
from loader import user_db


class Administrator(BaseMiddleware):
    async def on_process_message(self, message: Message, data: dict):
        data['admin'] = bool(user_db.is_admin(message.from_user.id))
        data['msg'] = MsgToDict(message)

    async def on_process_callback_query(self, call: CallbackQuery, data: dict):
        data['admin'] = bool(user_db.is_admin(call.from_user.id))
        data['msg'] = MsgToDict(call)
