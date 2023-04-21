from DataBase import DataBase


class User(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_users(self):
        sql = '''CREATE TABLE IF NOT EXISTS users 
        (tg_id INTEGER PRIMARY KEY, name VARCHAR, courses VARCHAR, lectures VARCHAR)'''
        self.execute(sql, commit=True)

    def create_table_users_options(self):
        sql = '''CREATE TABLE IF NOT EXISTS users_options 
        (tg_id INTEGER PRIMARY KEY, alerts_stream VARCHAR,
        alerts_courses VARCHAR, alerts_news VARCHAR)'''
        self.execute(sql, commit=True)

    def create_table_admins(self):
        sql = '''CREATE TABLE IF NOT EXISTS admins 
                (tg_id INTEGER PRIMARY KEY)'''
        self.execute(sql, commit=True)

    def check(self, tg_id: int, user_name: str):
        sql = '''SELECT * FROM users WHERE tg_id=?'''
        if not self.execute(sql, (tg_id,), fetchone=True):
            new_user = (tg_id, user_name)
            sql = '''INSERT INTO users (tg_id, name) VALUES (?, ?)'''
            self.execute(sql, new_user, commit=True)
            options = (tg_id, 'True', 'True', 'True')
            sql = '''INSERT INTO users_options (tg_id, alerts_stream, alerts_courses, 
                    alerts_news) VALUES (?, ?, ?, ?)'''
            self.execute(sql, options, commit=True)

    def select(self, **kwargs):
        sql = '''SELECT tg_id FROM users_options WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def settings(self, tg_id: int):
        sql = '''SELECT * FROM users_options WHERE tg_id=?'''
        return self.execute(sql, (tg_id,), fetchone=True)

    def switcher(self, tg_id: int, option: str):
        sql = f'''UPDATE users_options SET alerts_{option} = CASE WHEN alerts_{option} = 'True' 
        THEN 'False' ELSE 'True' END WHERE tg_id=?'''
        self.execute(sql, (tg_id,), commit=True)


    def is_admin(self, tg_id: int) -> bool:
        sql = '''SELECT * FROM admins WHERE tg_id=?'''
        return self.execute(sql, (tg_id,), fetchone=True)

    def course_and_lectures(self, tg_id: int) -> tuple[str]:
        sql = '''SELECT courses, lectures FROM users WHERE tg_id=?'''
        return self.execute(sql, (tg_id,), fetchone=True)