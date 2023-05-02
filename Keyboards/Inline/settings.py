from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as InKB

from Keyboards.Callback import main_menu, settings
from Misc import MsgToDict
from loader import user_db, settings_db


def ikb_settings(msg: MsgToDict) -> InlineKeyboardMarkup:
    on, off = '\u2705', '\u274C'

    def crt_cb(button: str) -> str:
        return settings.new(menu='settings', button=button)

    def btn_switch_admin(status: int) -> InKB:
        text = 'Admin: ' + (on if status else off)
        return InKB(text=text, callback_data=crt_cb('admin'))

    keyboard_settings = InlineKeyboardMarkup(row_width=2)
    *_, stream, courses, news = user_db.settings(msg.my_id)
    btn_alert_list = [(':Стримы', on if stream == 1 else off, 'stream'),
                      (':Мои курсы', on if courses == 1 else off, 'courses'),
                      (':Новости', on if news == 1 else off, 'news')]

    btn_back = InKB(text='Назад', callback_data=main_menu.new(menu='main', button='back'))

    keyboard_settings.row(*[InKB(text=f'{switch}{text}', callback_data=crt_cb(button))
                            for text, switch, button in btn_alert_list])

    if adm := user_db.is_admin(msg.my_id):
        keyboard_settings.add(btn_switch_admin(adm[0]), btn_back)
    else:
        keyboard_settings.add(btn_back)
    return keyboard_settings


def ikb_links() -> InlineKeyboardMarkup:
    keyboard_links = InlineKeyboardMarkup(row_width=3)
    link_list = {link[4]: link[3] for link in settings_db.load(type_set='link')}
    for text, link in link_list.items():
        keyboard_links.insert(InKB(url=link, text=text))
    btn_back = InKB(text='Назад', callback_data=main_menu.new(menu='', button='back'))
    keyboard_links.add(btn_back)
    return keyboard_links
