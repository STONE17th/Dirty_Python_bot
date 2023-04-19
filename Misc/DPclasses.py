from aiogram.types import Message, CallbackQuery
from config import tasks

class Class:
    def __init__(self, db_answer: tuple[str]):
        self.stream = db_answer[5]
        self.video = db_answer[6]
        self.compendium = db_answer[7]

    def __repr__(self):
        return f'Название: {self.name}\n\nОписание: {self.desc}\n\nСтрим: {self.stream}\nВидео: {self.video}\nКонспект: {self.compendium}\n\nЦена: {self.price}'

class_id INTEGER PRIMARY KEY AUTOINCREMENT,
        class_name VARCHAR, class_desc VARCHAR,
        class_poster VARCHAR, video_url VARCHAR,
        compendium_url VARCHAR, class_price VARCHAR

class Course:
    def __init__(self, bd_answer: list[tuple[str]]):
        self.classes = [Class(class_) for class_ in bd_answer]
        self.size = len(self.classes)

    def whole(self):
        return self.classes


class CurrentTask:
    def __init__(self, task_list: tuple[str]):
        self.type = task_list[1]
        self.level = task_list[2]
        self.value = task_list[3]
        self.poster = tasks.get(self.type).get(self.level)

    def task(self, index: int, total: int):
        return f'{index+1}/{total}\nТема: {self.type}\nУровень: {self.level}\n\n{self.value}'


class MsgToDict:
    def __init__(self, message: Message | CallbackQuery):
        if isinstance(message, Message):
            self.name = message.from_user.first_name
            self.my_id = message.from_user.id
            self.my_id = message.from_user.id
            self.message_id = message.message_id
            self.data = message.text
        elif isinstance(message, CallbackQuery):
            self.name = message.from_user.first_name
            self.chat_id = message.from_user.id
            self.my_id = message.from_user.id
            self.message_id = message.message.message_id
            self.data = message.data.split(':')
        if self.data[0] == 'list_navigation':
            self.type = self.data[2]
            self.level = self.data[3]
            self.id = int(self.data[4])
