from aiogram.types import Message, CallbackQuery

from Misc import pictures
from loader import course_db


class Lecture:
    def __init__(self, data: tuple[str] | str):
        if isinstance(data, str):
            data = course_db.whole(data.split(':')[0])[int(data.split(':')[1]) + 1]
        self.name = data[1]
        self.desc = data[2]
        self.poster = data[3]
        self.video = data[4]
        self.compendium = data[5]
        self.price = int(data[6]) if isinstance(data[6], str) and data[6].isdigit() else 0

    def __str__(self):
        return f'Название: {self.name}\n\nОписание: {self.desc}\n\nВидео: {self.video}\nКонспект: {self.compendium}\n\nЦена: {self.price}'


class Course:
    def __init__(self, data: tuple | str):
        if isinstance(data, tuple):
            self.id = data[0]
            self.name = data[1]
            self.table = data[2]
            self.desc = data[3]
            self.poster = data[4]
            self.url = data[5]
            self.tg_chat = data[6]
            self.price = int(data[7]) if isinstance(data[7], str) and data[7].isdigit() else 0
            self.start = data[8]
            self.active = data[9]
            self.lectures = [Lecture(lecture) for lecture in
                             course_db.whole(self.table)] if self.table != 'custom' else []
        else:
            raise ValueError

    def __str__(self):
        return '\n'.join(map(str, self.lectures))

    def info(self):
        list_lecture = course_db.is_completed(self.table)
        completed = [1 for i in list_lecture if i == (None,)]
        finalize = f'{round((len(self.lectures) - len(completed)) / len(self.lectures), 2) * 100}% ({len(self.lectures) - len(completed)}/{len(self.lectures)})'
        return f'Название курса {self.name}\n\nОписание: {self.desc}\n\n' \
               f'Стоимость всего курса: {self.price}\nДата старта: {self.start}\nКурс завершен на {finalize}'

    def full_info(self):
        pass

    def is_active(self):
        return True if self.active == 'True' else False

    def __len__(self):
        return len(self.lectures)

    def all(self):
        return self.lectures

    def lecture(self, index: int, admin: bool, is_bought: bool = False):
        if admin:
            return f'Название: {self.lectures[index].name}\n\nОписание: {self.lectures[index].desc}\n\nВидео: {self.lectures[index].video}' \
                   f'\nКонспект: {self.lectures[index].compendium}' + ('\n\nЦена: {self.lectures[index].price}' if not is_bought else '')
        return f'Название: {self.lectures[index].name}\n\nОписание: {self.lectures[index].desc}\n\nЦена: {self.lectures[index].price}'

    def add_new(self, target_lecture: str):
        self.lectures.append(Lecture(target_lecture))


class CurrentTask:
    def __init__(self, task_list: tuple[str]):
        self.type = task_list[1]
        self.level = task_list[2]
        self.value = task_list[3]
        self.poster = pictures.tasks.get(self.type).get(self.level)

    def task(self, index: int, total: int):
        return f'{index + 1}/{total}\nТема: {self.type}\nУровень: {self.level}\n\n{self.value}'


class MsgToDict:
    def __init__(self, message: Message | CallbackQuery):
        if isinstance(message, Message):
            self.name = message.from_user.first_name
            self.my_id = message.from_user.id
            self.chat_id = message.from_user.id
            self.message_id = message.message_id
            self.data = message.text
        elif isinstance(message, CallbackQuery):
            self.name = message.from_user.first_name
            self.chat_id = message.from_user.id
            self.my_id = message.from_user.id
            self.message_id = message.message.message_id
            self.data = message.data.split(':')
        if self.data:
            if self.data[0] == 'list_navigation':
                self.type = self.data[2]
                self.level = self.data[3]
                self.id = int(self.data[4])
            elif self.data[0] == 'course_navigation':
                self.table = self.data[-2]
                self.id = int(self.data[-1])
            elif self.data[0] == 'settings_option':
                self.menu = self.data[-2]
                self.button = self.data[-1]
