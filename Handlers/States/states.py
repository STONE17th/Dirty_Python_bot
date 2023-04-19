from aiogram.dispatcher.filters.state import StatesGroup, State


class NewCourse(StatesGroup):
    name = State()
    table = State()
    quantity = State()
    desc = State()
    url = State()
    poster = State()
    price = State()
    start_date = State()
    course_confirm = State()


class NewTask(StatesGroup):
    task_type = State()
    task_level = State()
    task_value = State()
    task_confirm = State()

class Stream(StatesGroup):
    name = State()
    desc = State()
    poster = State()
    url = State()
    confirm = State()

class Announcement(StatesGroup):
    name = State()
    desc = State()
    poster = State()
    url = State()
    confirm = State()