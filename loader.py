from aiogram import Dispatcher, Bot
from DataBase import DataBase
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os


memory = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=memory)
db = DataBase()
