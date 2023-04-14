from aiogram.dispatcher.filters.state import StatesGroup, State


class NewCourse(StatesGroup):
    name = State()
    desc = State()
    url_course = State()
    poster = State()
    quantity = State()
    price = State()

class NewTask(StatesGroup):
    task_type = State()
    task_level = State()
    task_value = State()
    task_confirm = State()