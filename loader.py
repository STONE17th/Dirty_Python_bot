from aiogram import Dispatcher, Bot
from DataBase import Course, Lecture, Task, User, Settings
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os


memory = MemoryStorage()

PICTURES: dict[str, str] = {}.fromkeys(['start_poster', 'task_main', 'my_courses', 'all_courses',
                                        'no_lecture', 'task_easy', 'task_normal', 'task_hard', 'individual_courses',
                                        'settings'])

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=memory)
course_db = Course()
lecture_db = Lecture()
task_db = Task()
user_db = User()
settings_db = Settings()
