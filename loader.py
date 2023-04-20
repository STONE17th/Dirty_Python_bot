from aiogram import Dispatcher, Bot
from DataBase import DataBase, Course, Lecture, Task, User
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os


memory = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=memory)
course_db = Course()
lecture_db = Lecture()
task_db = Task()
user_db = User()
