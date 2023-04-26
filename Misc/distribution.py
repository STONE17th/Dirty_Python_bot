from loader import user_db, bot


async def user_distribution(type_message: str,  message: str, table: str = None) -> None:
    match type_message:
        case 'stream':
            user_list = user_db.at_course(alert='alerts_stream')
        case 'courses':
            if table:
                user_list = user_db.at_course(alert='alerts_courses', table=table)
            else:
                user_list = user_db.at_course(alert='alerts_courses')
        case 'news':
            user_list = user_db.at_course(alert='alerts_news')
        case _:
            user_list = []
    print(user_list)
    print(set(user_list))
    if user_list:
        for user in set(user_list):
            try:
                await bot.send_message(int(user[0]), text=message)
            except Exception as e:
                pass
