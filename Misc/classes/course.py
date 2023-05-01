from loader import course_db, lecture_db
from .lecture import Lecture


class Course:
    def __init__(self, data: tuple | str):
        id, name, table, desc, poster, url, tg_chat, price, start, active = data
        self.id = id
        self.name = name
        self.table = table
        self.desc = desc
        self.poster = poster
        self.url = url
        self.tg_chat = tg_chat
        self.price = int(price) if isinstance(price, str) and price.isdigit() else 0
        self.start = start
        self.active = active
        self.lectures = [Lecture(lecture, self.table) for lecture in
                         course_db.whole(self.table)] if self.table != 'custom' else []

    def __str__(self):
        return '\n'.join(map(str, self.lectures))

    def info(self):
        completed = course_db.done(self.table)
        finalize = f'{round((completed[1] - completed[0]) / completed[1], 2) * 100}% ({len(self.lectures) - len(completed)}/{len(self.lectures)})'
        return f'Название курса {self.name}\n\nОписание: {self.desc}\n\n' \
               f'Стоимость всего курса: {self.price}\nДата старта: {self.start}\nКурс завершен на {finalize}'

    def full_info(self):
        pass

    def is_active(self):
        return self.active

    def __len__(self):
        return len(self.lectures)

    def all(self):
        return self.lectures

    def lecture(self, index: int, admin: bool, is_bought: bool = False):
        if admin:
            return f'Название: {self.lectures[index].name}\n\nОписание: ' \
                   f'{self.lectures[index].desc}\n\nВидео: {self.lectures[index].video}' \
                   f'\nКонспект: {self.lectures[index].compendium}' + \
                (f'\n\nЦена: {self.lectures[index].price}' if not is_bought else '')
        return f'Название: {self.lectures[index].name}\n\nОписание: {self.lectures[index].desc}' + (
            f'\n\nЦена: {self.lectures[index].price}' if not is_bought else '')

    def add_new(self, target_lecture: str):
        table, index = target_lecture.split(':')
        lecture = lecture_db.select(table, int(index) + 1)
        self.lectures.append(Lecture(lecture, table))
