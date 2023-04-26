from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as IKB

from Keyboards.Callback import main_menu


def create_ikb_notification() -> InlineKeyboardMarkup:
    ikb_notification = InlineKeyboardMarkup(row_width=2)
    btn_stream = IKB(text='Стрим', callback_data=main_menu.new(menu='', button='back'))
    btn_news = IKB(text='Новость', callback_data=main_menu.new(menu='', button='back'))
    btn_back = IKB(text='Назад', callback_data=main_menu.new(menu='', button='back'))
    ikb_notification.row(btn_stream, btn_news)
    ikb_notification.add(btn_back)
    return ikb_notification


# def create_ikb_list_navigation(menu: str, admin: bool, task_type: str, task_level: str, curr_id: int,
#                                list_size: int) -> InlineKeyboardMarkup:
#     ikb_navigation = InlineKeyboardMarkup(row_width=1)
#     prev_id = int(curr_id - 1) if curr_id != 0 else int(list_size - 1)
#     next_id = int(curr_id + 1) if curr_id != (list_size - 1) else 0
#     btn_prev = IKB(text='<<<',
#                    callback_data=list_navigation.new(menu=menu,
#                                                      task_type=task_type,
#                                                      task_level=task_level,
#                                                      current_id=prev_id))
#     btn_next = IKB(text='>>>',
#                    callback_data=list_navigation.new(menu=menu,
#                                                      task_type=task_type,
#                                                      task_level=task_level,
#                                                      current_id=next_id))
#     btn_back = IKB(text='Назад',
#                    callback_data=list_navigation.new(menu='type',
#                                                      task_type=task_type,
#                                                      task_level='',
#                                                      current_id=0))
#     btn_task_delete = IKB(text='Удалить задачу',
#                           callback_data=list_navigation.new(menu='task_delete',
#                                                             task_type=task_type,
#                                                             task_level=task_level,
#                                                             current_id=curr_id))
#     if list_size > 1:
#         ikb_navigation.add(btn_prev, btn_next)
#     if admin:
#         ikb_navigation.add(btn_task_delete, btn_back)
#     else:
#         ikb_navigation.add(btn_back)
#     return ikb_navigation
