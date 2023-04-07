from aiogram import Dispatcher, Bot
from aiogram.types import Message
import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)