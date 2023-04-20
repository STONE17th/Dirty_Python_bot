from aiogram.utils import executor

import MiddleWare
from Handlers import dp
from loader import course_db, lecture_db, task_db, user_db


async def on_start(_):
    try:
        course_db.create_table_courses()
        task_db.create_table_tasks()
        user_db.create_table_users()
        user_db.create_table_users_options()
        user_db.create_table_admins()
        print('DB connection.. OK')
    except IOError:
        print('DB connection... FAILURE!!!')
    print('Бот запущен!')


if __name__ == '__main__':
    MiddleWare.setup(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)
