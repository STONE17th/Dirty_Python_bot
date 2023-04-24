from aiogram.dispatcher.filters.state import StatesGroup, State


class NewCourse(StatesGroup):
    name = State()
    table = State()
    quantity = State()
    desc = State()
    url = State()
    tg_chat = State()
    poster = State()
    price = State()
    start_date = State()
    course_confirm = State()


class NewLecture(StatesGroup):
    name = State()
    desc = State()
    poster = State()
    video = State()
    compendium = State()
    price = State()
    confirm = State()


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


class Posters(StatesGroup):
    start_poster = State()
    task_main = State()
    my_courses = State()
    all_courses = State()
    no_lecture = State()
    task_easy = State()
    task_normal = State()
    task_hard = State()
    settings = State()
    individual_courses = State()
