from aiogram.utils.callback_data import CallbackData

main_menu = CallbackData('main_menu', 'menu', 'button')

select_task = CallbackData('select_task', 'menu', 'task_type', 'task_level')