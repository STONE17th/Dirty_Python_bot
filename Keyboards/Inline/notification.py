from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as InKB

from Keyboards.Callback import main_menu


def ikb_notification() -> InlineKeyboardMarkup:
    keyboard_notification = InlineKeyboardMarkup(row_width=2)
    btn_stream = InKB(text='Стрим', callback_data=main_menu.new(menu='', button='stream'))
    btn_news = InKB(text='Новость', callback_data=main_menu.new(menu='', button='news'))
    btn_back = InKB(text='Назад', callback_data=main_menu.new(menu='', button='back'))
    keyboard_notification.row(btn_stream, btn_news)
    keyboard_notification.add(btn_back)
    return keyboard_notification


def ikb_user_notification(menu: str, url: str) -> InlineKeyboardMarkup:
    keyboard_user = InlineKeyboardMarkup(row_width=2)
    match menu:
        case 'stream':
            btn_main = InKB(text='Go на cтрим!', url=url)
        case 'courses':
            btn_main = InKB(text='Перейти', callback_data=main_menu.new(menu='main', button='my_courses'))
        case 'news':
            btn_main = InKB(text=('Перейти' if url else 'Закрепить'),
                            callback_data=main_menu.new(menu='main', button=('all_courses' if url else 'pin_news')))
    btn_delete = InKB(text='Удалить', callback_data=main_menu.new(menu='', button='message_delete'))
    keyboard_user.row(btn_main, btn_delete)
    return keyboard_user
