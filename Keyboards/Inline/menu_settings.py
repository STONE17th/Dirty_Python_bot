from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as IKB
from loader import user_db
from Misc import MsgToDict
from Keyboards.Callback import main_menu, settings_option


def create_ikb_settings(my_set: tuple, msg: MsgToDict) -> InlineKeyboardMarkup:
    *_, stream, courses, news = my_set
    ON_ = '\u2705'
    OFF_ = '\u274C'
    ikb_settings = InlineKeyboardMarkup(row_width=2)

    btn_stream = IKB(text=f'Оповещения о стримах DP: {ON_ if stream == "True" else OFF_}',
                     callback_data=settings_option.new(menu='settings',
                                                       button='stream'))
    btn_courses = IKB(text=f'Оповещения о моих курсах DP: {ON_ if courses == "True" else OFF_}',
                      callback_data=settings_option.new(menu='settings',
                                                        button='courses'))
    btn_news = IKB(text=f'Оповещения о новостях и акциях DP: {ON_ if news == "True" else OFF_}',
                   callback_data=settings_option.new(menu='settings',
                                                     button='news'))
    btn_back = IKB(text='Назад',
                   callback_data=main_menu.new(menu='main',
                                               button='back'))

    def btn_switch_admin(status: int) -> IKB:
        text = 'admin' if status else 'user'
        return IKB(text=text, callback_data=main_menu.new(menu='adm_switch', button=''))

    ikb_settings.add(btn_stream)
    ikb_settings.add(btn_courses)
    ikb_settings.add(btn_news)
    if adm := user_db.is_admin(msg.my_id):
        ikb_settings.add(btn_switch_admin(adm[0]), btn_back)
    else:
        ikb_settings.add(btn_back)
    return ikb_settings
