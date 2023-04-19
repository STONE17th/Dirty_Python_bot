# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from Keyboards.Callback import main_menu, tasks
# from loader import db
#
#
# def create_ikb_task_level(task_type: str) -> InlineKeyboardMarkup:
#     kb_task_level = InlineKeyboardMarkup(row_width=3)
#     ibtn_list = []
#     list_levels = set([level[0] for level in db.collect_tasks('task_level', task_type)])
#     btn_levels = [level for level in ['easy', 'normal', 'hard'] if level in list_levels]
#     for task_level in btn_levels:
#         ibtn_list.append(InlineKeyboardButton(text=task_level,
#                                               callback_data=tasks.new(menu='select_task_level',
#                                                                             task_type=task_type,
#                                                                             task_level=task_level)))
#     ibtn_back = InlineKeyboardButton(text='Назад',
#                                      callback_data=main_menu.new(menu='main',
#                                                                  button='tasks'))
#     kb_task_level.add(*ibtn_list)
#     kb_task_level.add(ibtn_back)
#
#     return kb_task_level
