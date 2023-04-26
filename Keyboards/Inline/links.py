from aiogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup

from Keyboards.Callback import main_menu
from loader import settings_db


def create_ikb_links() -> InlineKeyboardMarkup:
    ikb_links = InlineKeyboardMarkup(row_width=1)
    link_list = [link[3] for link in settings_db.load(type_set='link')]
    name_list = ['YouTube', 'ZOOM', 'Telegram', 'Boosty',
                 'Donation Alerts', 'Стоун (Личка)', 'Диана (Личка)']
    for i in range(len(name_list)):
        ikb_links.add(IKB(url=link_list[i], text=name_list[i]))
    btn_back = IKB(text='Назад',
                   callback_data=main_menu.new(menu='', button='back'))
    ikb_links.add(btn_back)
    return ikb_links
