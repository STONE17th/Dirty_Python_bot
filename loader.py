from aiogram import Dispatcher, Bot
import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)