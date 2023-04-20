from aiogram.utils.callback_data import CallbackData

main_menu = CallbackData('main_menu', 'menu', 'button')

tasks = CallbackData('tasks', 'select', 'task_type', 'task_level')

navigation_menu = CallbackData('navigation', 'menu', 'curr_id', 'task_type', 'task_level')

new_admin = CallbackData('new_admin', 'menu', 'user_id', 'button')

task_navigation = CallbackData('list_navigation', 'menu', 'task_type', 'task_level', 'current_id')

course_navigation = CallbackData('course_navigation', 'menu', 'table', 'current_id')

confirm_request = CallbackData('confirm', 'menu', 'args', 'button')
