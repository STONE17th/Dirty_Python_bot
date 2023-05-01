from aiogram.types import Message, CallbackQuery


class MsgToDict:
    def __init__(self, message: Message | CallbackQuery):
        self.name = message.from_user.first_name
        self.chat_id = message.from_user.id
        self.my_id = message.from_user.id
        if isinstance(message, Message):
            self.message_id = message.message_id
            self.data = message.text
        elif isinstance(message, CallbackQuery):
            self.message_id = message.message.message_id
            self.data = message.data.split(':')
            if self.data:
                match self.data:
                    case ['list_navigation', _, task_type, level, current_id]:
                        self.type = task_type
                        self.level = level
                        self.id = int(current_id)
                    case ['course_navigation', _, table, lecture_id]:
                        self.table = table
                        self.id = int(lecture_id)
                    case ['settings_option', menu, button]:
                        self.menu = menu
                        self.button = button
                    case _:
                        self.data = message.data
