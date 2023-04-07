from aiogram.utils import executor
from Handlers import dp
from DataBase import create_table


async def on_start(_):
    try:
        create_table()
        print('DB connection.. OK')
    except:
        print('DB connection... FAILURE!!!')

    print('Бот запущен!')


executor.start_polling(dp, skip_updates=True, on_startup=on_start)