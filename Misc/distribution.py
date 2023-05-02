from Keyboards import ikb_user_notification
from loader import user_db, bot


async def user_distribution(type_message: str, message: tuple[str, str], table: str = None) -> None:
    keyboard = ikb_user_notification(type_message, table)
    caption, poster = message
    user_list = user_db.at_course(alert=f'alerts_{type_message}', table=table)
    if user_list:
        for user in set(user_list):
            try:
                await bot.send_photo(int(user[0]), photo=poster, caption=caption, reply_markup=keyboard)
            except Exception as e:
                pass
