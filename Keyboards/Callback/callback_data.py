from aiogram.utils.callback_data import CallbackData

main_menu = CallbackData('main_menu', 'menu', 'button')

select_task = CallbackData('select_task', 'menu', 'task_type', 'task_level')

navigation_menu = CallbackData('navigation', 'menu', 'curr_id', 'task_type', 'task_level')

new_admin = CallbackData('new_admin', 'menu', 'user_id', 'button')
