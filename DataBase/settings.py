from DataBase import DataBase


class Settings(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_settings(self):
        sql = '''CREATE TABLE IF NOT EXISTS settings 
        (settings_id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, type_set VARCHAR,
        value VARCHAR, option_one VARCHAR, option_two VARCHAR, option_three VARCHAR)'''
        self.execute(sql, commit=True)
        sql = '''CREATE UNIQUE INDEX IF NOT EXISTS idx_settings_name ON settings (name)'''
        self.execute(sql, commit=True)

    def load(self, **kwargs):
        sql = '''SELECT * FROM settings WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def save_posters(self, data: dict[str, str]):
        for poster, link in data.items():
            params = (poster, link)
            sql = f'''REPLACE INTO settings (name, type_set, value) VALUES (?, "poster", ?)'''
            self.execute(sql, params, commit=True)

