from .data_base import DataBase


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

    def save_settings(self, data: dict[str, str], type_settings: str):
        for poster, link in data.items():
            params = (poster, link, type_settings)
            sql = f'''REPLACE INTO settings (name, value, type_set) VALUES (?, ?, ?)'''
            self.execute(sql, params, commit=True)

    def select_url(self, name: str) -> tuple:
        sql = '''SELECT value FROM settings WHERE option_one=?'''
        return self.execute(sql, (name,), fetchone=True)[0]
