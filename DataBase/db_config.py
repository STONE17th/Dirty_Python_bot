import sqlite3


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
        (tg_id INTEGER PRIMARY KEY, name VARCHAR, courses VARCHAR)'''
        self.execute(sql, commit=True)

    def create_table_tasks(self):
        sql = '''CREATE TABLE IF NOT EXISTS tasks 
        (task_id INTEGER PRIMARY KEY AUTOINCREMENT, task_type VARCHAR, 
        task_level VARCHAR, task_value VARCHAR)'''
        self.execute(sql, commit=True)

    def create_table_courses(self):
        sql = '''CREATE TABLE IF NOT EXISTS courses 
        (course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR, stream INT, description VARCHAR,
        poster VARCHAR, video VARCHAR, price VARCHAR,
        active VARCHAR, start_date VARCHAR)'''
        self.execute(sql, commit=True)

    def create_table_users_options(self):
        sql = '''CREATE TABLE IF NOT EXISTS users_options 
        (tg_id INTEGER PRIMARY KEY, alerts_stream VARCHAR,
        alerts_courses VARCHAR, alerts_news VARCHAR)'''
        self.execute(sql, commit=True)

    def new_user(self, user: tuple):
        new_user = (user[0], user[1], '')
        sql = '''INSERT INTO users (tg_id, name, courses) VALUES (?, ?, ?)'''
        self.execute(sql, new_user, commit=True)
        options = (user[0], 'True', 'True', 'True')
        sql = '''INSERT INTO users_options (tg_id, alerts_stream, alerts_courses, 
        alerts_news) VALUES (?, ?, ?, ?)'''
        self.execute(sql, options, commit=True)

    def check_user(self, tg_id: int):
        user = (tg_id,)
        sql = '''SELECT * FROM users WHERE tg_id=?'''
        if self.execute(sql, user, fetchone=True):
            return True

    def user_settings(self, tg_id: int):
        user = (tg_id,)
        sql = '''SELECT * FROM users_options WHERE tg_id=?'''
        return self.execute(sql, user, fetchone=True)

    def change_option(self, tg_id: int, option: str):
        parameters = (tg_id,)
        sql = f'''UPDATE users_options SET alerts_{option} = CASE
                                                            WHEN alerts_{option} = 'True' THEN 'False'
                                                                                        ELSE 'True'
                                                            END 
                                                            WHERE tg_id=?'''
        self.execute(sql, parameters, commit=True)

    def add_new_course(self, new_course: dict[str, str]):
        course = (new_course.get('name'), '', new_course.get('desc'), new_course.get('poster'),
                  new_course.get('url_course'), new_course.get('price'), '', '')
        sql = '''INSERT INTO courses (name, stream, description, poster, video, price, active,
        start_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
        self.execute(sql, course, commit=True)

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

    # def insert_new_item(self, my_dict: dict):
    #     item = (my_dict.get('name'), my_dict.get('age'), my_dict.get('city'))
    #     sql = '''INSERT INTO goods (name, age, city) VALUES (?, ?, ?)'''
    #     self.execute(sql, item, commit=True)
    #
    # def create_table_basket(self):
    #     sql = '''CREATE TABLE IF NOT EXISTS basket
    #     (id_order INTEGER PRIMARY KEY AUTOINCREMENT,
    #     id_user INTEGER, id_goods INTEGER)'''
    #     self.execute(sql, commit=True)
    #
    # def create_table_purchase(self):
    #     sql = '''CREATE TABLE IF NOT EXISTS purchase
    #     (id_order INTEGER PRIMARY KEY AUTOINCREMENT,
    #     name TEXT, phone_number TEXT, email TEXT,
    #     shipping TEXT, address TEXT, goods TEXT)'''
    #     self.execute(sql, commit=True)
    #
    # def add_goods(self, goods: dict):
    #     parameters = (goods.get('g_type'), goods.get('image'), goods.get('name'),
    #                   goods.get('desc'), goods.get('quantity'), goods.get('price'))
    #     sql = '''INSERT INTO goods (g_type, image, name, desc, quantity, price)
    #     VALUES (?, ?, ?, ?, ?, ?)'''
    #     self.execute(sql, parameters, commit=True)
    #
    # def get_goods(self, **kwargs):
    #     sql = '''SELECT * FROM goods WHERE '''
    #     sql, parameters = self.extract_kwargs(sql, kwargs)
    #     return self.execute(sql, parameters, fetchall=True)
    #
    # def get_basket(self, **kwargs):
    #     sql = '''SELECT * FROM basket WHERE '''
    #     sql, parameters = self.extract_kwargs(sql, kwargs)
    #     return self.execute(sql, parameters, fetchall=True)
    #
    # def add_to_basket(self, id_user: int, id_goods: int):
    #     parameters = (id_user, id_goods)
    #     sql = '''INSERT INTO basket (id_user, id_good) VALUES (?, ?)'''
    #     self.execute(sql, parameters, commit=True)
    #     parameters = (id_goods,)
    #     sql = '''UPDATE goods SET quantity = quantity - 1 WHERE id=?'''
    #     self.execute(sql, parameters, commit=True)
    #
    # def remove_from_basket(self, id_order: int, id_goods: int):
    #     parameters = (id_order,)
    #     sql = '''DELETE FROM basket WHERE id_order=?'''
    #     self.execute(sql, parameters, commit=True)
    #     parameters = (id_goods,)
    #     sql = '''UPDATE goods SET quantity = quantity + 1 WHERE id=?'''
    #     self.execute(sql, parameters, commit=True)
    #
    # def clear_basket(self, id_user):
    #     parameters = (id_user,)
    #     sql = '''DELETE FROM basket WHERE id_user=?'''
    #     self.execute(sql, parameters, commit=True)
    #
    # def add_purchase(self, id_user: int, order: dict, shipping: str):
    #     sql = '''INSERT INTO purchase (name, phone_number, email, shipping, address, goods)
    #     VALUES (?, ?, ?, ?, ?, ?)'''
    #     for goods in self.get_basket(id_user=id_user):
    #         item = self.get_goods(id=int(goods[2]))
    #         parameters = (order.get('name'), order.get('phone_number'), order.get('email'),
    #                       shipping, str(order.get('shipping_address')), str(item[0][3]))
    #         self.execute(sql, parameters, commit=True)

    @staticmethod
    def extract_kwargs(sql: str, parameters: dict) -> tuple:
        sql += ' AND '.join([f'{key} = ?' for key in parameters])
        return sql, tuple(parameters.values())

    def disconnect(self):
        self.connection.close()
