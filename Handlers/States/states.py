from aiogram.dispatcher.filters.state import StatesGroup, State


class NewCourse(StatesGroup):
    name = State()
    desc = State()
    url_course = State()
    poster = State()
    quantity = State()
    price = State()