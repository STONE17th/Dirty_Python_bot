from aiogram.dispatcher.filters.state import StatesGroup, State


class NewCourse(StatesGroup):
    course_name = State()
    table_name = State()
    course_desc = State()
    course_url = State()
    poster = State()
    price = State()
    start_date = State()
    course_confirm = State()


class NewTask(StatesGroup):
    task_type = State()
    task_level = State()
    task_value = State()
    task_confirm = State()
