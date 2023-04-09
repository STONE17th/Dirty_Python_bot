from aiogram import Dispatcher, Bot
from DataBase import DataBase
import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
db = DataBase()
