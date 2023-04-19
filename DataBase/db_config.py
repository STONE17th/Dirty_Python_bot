import sqlite3
from config import no_lection

class DataBase:

    def __init__(self, db_path: str = 'DataBase/DP_bot_db.db'):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_users(self):
        sql = '''CREATE TABLE IF NOT EXISTS users 
        (tg_id INTEGER PRIMARY KEY, name VARCHAR, courses VARCHAR, classes VARCHAR)'''
        self.execute(sql, commit=True)

    def create_table_users_options(self):
        sql = '''CREATE TABLE IF NOT EXISTS users_options 
        (tg_id INTEGER PRIMARY KEY, alerts_stream VARCHAR,
        alerts_courses VARCHAR, alerts_news VARCHAR)'''
        self.execute(sql, commit=True)

    def create_table_tasks(self):
        sql = '''CREATE TABLE IF NOT EXISTS tasks 
        (task_id INTEGER PRIMARY KEY AUTOINCREMENT, task_type VARCHAR, 
        task_level VARCHAR, task_value VARCHAR)'''
        self.execute(sql, commit=True)

    def create_table_courses(self):
        sql = '''CREATE TABLE IF NOT EXISTS courses 
        (course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR, table_name VARCHAR, desc VARCHAR,
        poster VARCHAR, url VARCHAR, price VARCHAR,
        active VARCHAR, start_date VARCHAR)'''
        self.execute(sql, commit=True)


    def create_table_custom_course(self, name_table: str):
        sql = f'''CREATE TABLE IF NOT EXISTS course_{name_table} 
        (class_id INTEGER PRIMARY KEY AUTOINCREMENT,
        class_name VARCHAR, class_desc VARCHAR,
        class_poster VARCHAR, video_url VARCHAR, 
        compendium_url VARCHAR, class_price VARCHAR)'''
        self.execute(sql, commit=True)

    def new_user(self, user: tuple):
        new_user = (user[0], user[1], '')
        sql = '''INSERT INTO users (tg_id, name, courses) VALUES (?, ?, ?)'''
        self.execute(sql, new_user, commit=True)
        options = (user[0], 'True', 'True', 'True')
        sql = '''INSERT INTO users_options (tg_id, alerts_stream, alerts_courses, 
        alerts_news) VALUES (?, ?, ?, ?)'''
        self.execute(sql, options, commit=True)

    def select_users(self, **kwargs):
        sql = '''SELECT tg_id FROM users_options WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def check_user(self, tg_id: int):
        user = (tg_id,)
        sql = '''SELECT * FROM users WHERE tg_id=?'''
        if self.execute(sql, user, fetchone=True):
            return True

    def user_settings(self, tg_id: int):
        user = (tg_id,)
        sql = '''SELECT * FROM users_options WHERE tg_id=?'''
        return self.execute(sql, user, fetchone=True)

    def all_active_courses(self):
        sql = '''SELECT name, table_name FROM courses WHERE active="True"'''
        return self.execute(sql, fetchall=True)

    def all_classes(self, table_name: str):
        sql = f'''SELECT * FROM course_{table_name}'''
        return self.execute(sql, fetchall=True)


    def user_courses(self, tg_id: int):
        sql = '''SELECT courses FROM users WHERE tg_id=?'''
        courses_list = self.execute(sql, (tg_id,), fetchone=True)[0].split(',')
        if '' not in courses_list:
            courses_list = list(map(int, courses_list))
        sql = '''SELECT name, table_name FROM courses WHERE course_id=?'''
        courses_name = [self.execute(sql, (course_id,), fetchone=True) for course_id in courses_list]
        print(courses_name)
        return courses_name

    def user_classes(self, tg_id: int):
        sql = '''SELECT classes FROM users WHERE tg_id=?'''
        classes_list = self.execute(sql, (tg_id,), fetchone=True)[0].split(',')
        if '' not in classes_list:
            classes_list = list(map(int, classes_list))
        sql = '''SELECT course_name, table_name FROM courses WHERE course_id=?'''
        courses_name = [self.execute(sql, (course_id,), fetchone=True) for course_id in classes_list]
        print(courses_name)
        return courses_name

    def change_option(self, tg_id: int, option: str):
        parameters = (tg_id,)
        sql = f'''UPDATE users_options SET alerts_{option} = CASE
                                                            WHEN alerts_{option} = 'True' THEN 'False'
                                                                                        ELSE 'True'
                                                            END 
                                                            WHERE tg_id=?'''
        self.execute(sql, parameters, commit=True)

    def whole_course(self, table_name: str):
        sql = f'''SELECT * FROM course_{table_name}'''
        return self.execute(sql, fetchall=True)


    def add_new_course(self, new_course: dict[str, str]):
        sql = '''INSERT INTO courses (name, table_name, desc, poster, url, price, active, start_date) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
        course = (new_course.get('name'), new_course.get('table'), new_course.get('desc'), new_course.get('poster'),
                  new_course.get('url'), new_course.get('price'), 'True', new_course.get('start_date'))
        self.execute(sql, course, commit=True)
        self.create_table_custom_course(new_course.get('table'))
        empty_course = (None, None, no_lection, None, None, None)
        for _ in range(int(new_course.get('quantity'))):
            sql = f'''INSERT INTO course_{new_course.get('table')} (class_name, class_desc, class_poster,
            video_url, compendium_url, class_price) VALUES (?, ?, ?, ?, ?, ?)'''
            self.execute(sql, empty_course, commit=True)

    def collect_tasks(self, target: str, task_type: str = None) -> list[tuple[str]]:
        if not task_type:
            sql = f'''SELECT {target} FROM tasks'''
            return self.execute(sql, fetchall=True)
        else:
            sql = f'''SELECT {target} FROM tasks WHERE task_type=?'''
            return self.execute(sql, (task_type,), fetchall=True)

    def add_new_task(self, task: tuple[str]):
        sql = '''INSERT INTO tasks (task_type, task_level, task_value) VALUES (?, ?, ?)'''
        self.execute(sql, task, commit=True)

    def select_tasks(self, task_type: str, task_level: str) -> tuple:
        user = (task_type, task_level)
        sql = '''SELECT * FROM tasks WHERE task_type=? AND task_level=?'''
        return self.execute(sql, user, fetchall=True)

    def delete_task(self, task_id: int):
        sql = '''DELETE FROM tasks WHERE task_id=?'''
        self.execute(sql, (task_id,), commit=True)

    @staticmethod
    def extract_kwargs(sql: str, parameters: dict) -> tuple:
        sql += ' AND '.join([f'{key} = ?' for key in parameters])
        return sql, tuple(parameters.values())

    def disconnect(self):
        self.connection.close()
