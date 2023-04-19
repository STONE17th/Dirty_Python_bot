from aiogram.types import Message, CallbackQuery
class MsgToDict:
    def __init__(self, message: Message | CallbackQuery):
        if isinstance(message, Message):
            self.name = message.from_user.first_name
            self.my_id = message.from_user.id
            self.my_id = message.from_user.id
            self.msg_id = message.message_id
            self.data = message.text
        elif isinstance(message, CallbackQuery):
            self.name = message.from_user.first_name
            self.chat_id = message.from_user.id
            self.my_id = message.from_user.id
            self.msg_id = message.message.message_id
            self.data = message.data.split(':')
