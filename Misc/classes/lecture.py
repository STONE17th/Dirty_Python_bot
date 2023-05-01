from loader import course_db


class Lecture:
    def __init__(self, data: tuple[str], table_name: str):
        _, name, desc, poster, video, compendium, price = data
        self.name = name
        self.desc = desc
        self.table = table_name
        self.poster = poster if poster else course_db.poster(table_name)[0]
        self.video = video
        self.compendium = compendium
        self.price = int(price) if isinstance(price, str) and price.isdigit() else 0

    def __str__(self):
        return f'Название: {self.name}\n\nОписание: {self.desc}\n\nВидео: {self.video}' \
               f'\nКонспект: {self.compendium}\n\nЦена: {self.price}'

    def is_empty(self):
        return not (self.name or self.desc or self.poster or self.video or self.compendium or self.price)
