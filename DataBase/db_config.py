import sqlite3

PATH = 'DataBase/db_new_bot.db'

connect = sqlite3.connect(PATH)
cursor = connect.cursor()


def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY
    AUTOINCREMENT, name VARCHAR, tg_id INTEGER, phone VARCHAR, comment VARCHAR)''')
    connect.commit()

def add_new_user(new_user: tuple):
    cursor.execute('''INSERT INTO users (name, tg_id, phone, comment)
    VALUES (?, ?, ?, ?)''', new_user)
    connect.commit()

def find_user(name: tuple):
    user = cursor.execute('''SELECT tg_id FROM users WHERE name=?''', name).fetchall()
    return user

def change_user(new_data: tuple):
    cursor.execute('''UPDATE users SET name=?, phone=?, comment=? WHERE user_id=?''', new_data)
    connect.commit()

def delete_user(user: tuple):
    cursor.execute('''DELETE FROM users WHERE user_id=?''', user)
    connect.commit()
