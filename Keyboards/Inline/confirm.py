from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as InKB

from Keyboards.Callback import confirm_request


def ikb_confirm(target: str, args: str = '') -> InlineKeyboardMarkup:
    def crt_cb(targ: str, args: str, button: str) -> str:
        return confirm_request.new(menu=targ, args=args, button=button)
    keyboard_confirm = InlineKeyboardMarkup(row_width=2)

    btn_yes = InKB(text='Да', callback_data=crt_cb(target, args, 'yes'))
    btn_no = InKB(text='Нет', callback_data=crt_cb(target, args, 'no'))

    keyboard_confirm.add(btn_yes, btn_no)

    return keyboard_confirm
