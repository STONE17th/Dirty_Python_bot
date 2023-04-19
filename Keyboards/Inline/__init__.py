from .all_courses import create_ikb_all_courses, create_ikb_all_classes
from .confirm import create_ikb_confirm
from .menu_navigation import create_ikb_list_navigation, create_ikb_select_option
from .menu_settings import create_ikb_settings
from .start import create_start_menu

# from .my_courses import create_ikb_my_courses
# from .confirm_admin import create_new_admin_confirm
# from .select_task_type import create_ikb_task_type
# from .select_task_level import create_ikb_task_level
__all__ = ['create_start_menu', 'create_ikb_confirm', 'create_ikb_settings', 'create_ikb_list_navigation',
           'create_ikb_select_option', 'create_ikb_all_courses', 'create_ikb_all_classes']
# ,'create_ikb_task_type', 'create_new_admin_confirm','create_ikb_my_courses','create_ikb_task_level',]
