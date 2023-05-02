from .data_base import DataBase


class Lecture(DataBase):
    def __init__(self):
        super().__init__()

    def all(self, table_name: str):
        sql = f'''SELECT * FROM course_{table_name}'''
        return self.execute(sql, fetchall=True)

    def select(self, table: str, index: int):
        sql = f'''SELECT * FROM course_{table} WHERE lecture_id=?'''
        return self.execute(sql, (index + 1,), fetchone=True)

    def update(self, data: dict[str]):
        params = (data.get('name'), data.get('desc'), data.get('poster'),
                  data.get('video'), data.get('compendium'), data.get('price'), int(data.get('id')) + 1)
        sql = f'''UPDATE course_{data.get("table")} SET name=?, desc=?, poster=?, video_url=?,
        compendium_url=?, price=? WHERE lecture_id=?'''
        self.execute(sql, params, commit=True)

    def users(self, tg_id: int):
        sql = '''SELECT lectures FROM users WHERE tg_id=?'''
        lectures_list = self.execute(sql, (tg_id,), fetchone=True)
        sql = '''SELECT name, table_name FROM courses WHERE course_id=?'''
        lectures = []
        print(lectures_list)
        if lectures_list != (None,):
            for lecture in lectures_list:
                sql = f'''SELECT * FROM course_{lecture.split(":")[0]} WHERE class_id=?'''
                lectures.append(self.execute(sql, (int(lecture.split(':')[1]) + 1,), fetchone=True))
        return lectures

    def purchase(self, user_id: int, table: str, index: int):
        sql = '''SELECT lectures FROM users WHERE tg_id=?'''
        lectures = self.execute(sql, (user_id,), fetchone=True)
        if lectures != (None,):
            lectures = [lecture for lecture in lectures]
        else:
            lectures = []
        lectures.append(f'{table}:{index}')
        data = ' '.join(lectures)
        sql = '''UPDATE users SET lectures=? WHERE tg_id=?'''
        params = (data, user_id)
        self.execute(sql, params, commit=True)
