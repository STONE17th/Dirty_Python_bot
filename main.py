from aiogram.utils import executor
import MiddleWare
from Handlers import dp
from loader import db


async def on_start(_):
    try:
        db.create_table_users()
        db.create_table_users_options()
        db.create_table_courses()
        db.create_table_tasks()
        print('DB connection.. OK')
    except:
        print('DB connection... FAILURE!!!')
    print('Бот запущен!')

MiddleWare.setup(dp)
executor.start_polling(dp, skip_updates=True, on_startup=on_start)  