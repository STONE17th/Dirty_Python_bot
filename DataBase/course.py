from .data_base import DataBase


class Course(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_courses(self):
        sql = '''CREATE TABLE IF NOT EXISTS courses 
        (course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR, table_name VARCHAR, desc VARCHAR,
        poster VARCHAR, cloud_url VARCHAR, tg_chat VARCHAR, price VARCHAR,
        start_date VARCHAR, active VARCHAR)'''
        self.execute(sql, commit=True)

    def create_table_lectures(self, name_table: str):
        sql = f'''CREATE TABLE IF NOT EXISTS course_{name_table} 
        (lecture_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR, desc VARCHAR, poster VARCHAR,
        video_url VARCHAR, compendium_url VARCHAR, price VARCHAR)'''
        self.execute(sql, commit=True)

    def add(self, new_course: dict[str, str]):
        sql = '''INSERT INTO courses (name, table_name, desc, poster, cloud_url, tg_chat, price, start_date, active) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        course = (new_course.get('name'), new_course.get('table'), new_course.get('desc'),
                  new_course.get('poster'), new_course.get('url'), new_course.get('tg_chat'),
                  new_course.get('price'), new_course.get('start_date'), 1)
        self.execute(sql, course, commit=True)
        self.create_table_lectures(new_course.get('table'))
        empty_course = (None, None, None, None, None, None)
        for _ in range(int(new_course.get('quantity'))):
            sql = f'''INSERT INTO course_{new_course.get('table')} (name, desc, poster,
            video_url, compendium_url, price) VALUES (?, ?, ?, ?, ?, ?)'''
            self.execute(sql, empty_course, commit=True)

    def select(self, table: str):
        sql = '''SELECT * FROM courses WHERE table_name=?'''
        return self.execute(sql, (table,), fetchone=True)

    def all(self):
        sql = '''SELECT * FROM courses'''
        return self.execute(sql, fetchall=True)

    def whole(self, table_name: str):
        sql = f'''SELECT * FROM course_{table_name}'''
        return self.execute(sql, fetchall=True)

    def poster(self, table: str):
        sql = f'''SELECT poster FROM courses WHERE table_name=?'''
        return self.execute(sql, (table,), fetchone=True)

    def users(self, tg_id: int):
        sql = '''SELECT courses FROM users WHERE tg_id=?'''
        courses_list = self.execute(sql, (tg_id,), fetchone=True)[0]
        print(courses_list)
        if courses_list != (None,):
            courses_list = list(map(int, courses_list.split()))
        else:
            return None
        sql = '''SELECT name, table_name FROM courses WHERE course_id=?'''
        courses = [self.execute(sql, (course_id,), fetchone=True) for course_id in courses_list]
        return courses

    def done(self, table_name: str) -> tuple[int, int]:
        sql = f'''SELECT name FROM course_{table_name}'''
        result = self.execute(sql, fetchall=True)
        return sum([1 for x in result if x[0] != None]), len(result)

    def is_completed(self, table_name: str):
        sql = f'''SELECT name FROM course_{table_name}'''
        if all(map(lambda x: x[0], self.execute(sql, fetchall=True))):
            return True

    def status(self, table_name: str):
        sql = f'''SELECT active FROM courses WHERE table_name=?'''
        result = self.execute(sql, (table_name,), fetchone=True)
        if result:
            return result[0]

    def finalize(self, table_name: str, status: int = 0):
        sql = f'''UPDATE courses SET active=? WHERE table_name=?'''
        self.execute(sql, (status, table_name), commit=True)

    def purchase(self, user_id: int, table: str):
        sql = '''SELECT courses FROM users WHERE tg_id=?'''
        courses = self.execute(sql, (user_id,), fetchone=True)
        if courses != (None,):
            courses = [course for course in courses]
        else:
            courses = []
        courses.append(table)
        data = ' '.join(courses)
        sql = '''UPDATE users SET courses=? WHERE tg_id=?'''
        params = (data, user_id)
        self.execute(sql, params, commit=True)
