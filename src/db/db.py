import sqlite3


# Функция инициализации базы данных
def db_init():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lastname TEXT NOT NULL,
            name TEXT NOT NULL)
        ''')
    conn.commit()
    conn.close()


# Функция для получения соединения с базой данных
def get_db():
    return sqlite3.connect('users.db')


# Функция для создания таблиц в базе данных
def create_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lastname TEXT NOT NULL,
            name TEXT NOT NULL)
    ''')
    conn.commit()
    conn.close()


# Функция для добавления нового пользователя в базу данных
def add_user(lastname, name):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (lastname, name) VALUES (?, ?)", (lastname, name))
    conn.commit()
    conn.close()


# Функция для получения всех пользователей
def getallusers():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    conn.close()
    return users


# Функция для удаления пользователя по ID с обновлением остальных ID
def delete_user(user_id):
    conn = get_db()
    cursor = conn.cursor()

    # Удаляем пользователя
    cursor.execute("DELETE FROM Users WHERE id = ?", (user_id,))

    # Обновляем ID пользователей с id > удаленного
    cursor.execute("UPDATE Users SET id = id - 1 WHERE id > ?", (user_id,))

    conn.commit()
    conn.close()

