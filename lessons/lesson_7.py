import sqlite3

# A4 - Лист
connect = sqlite3.connect('users.db')
# Рука с карандашом
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (20) NOT NULL,
    age INTEGER NOT NULL,
    hobby TEXT
    )
''')
connect.commit()

# CRUD - Create Read Update Delete

def create_user(name, age, hobby):
    # cursor.execute(f"INSERT INTO users(name, age, hobby) VALUES('{name}', {age}, '{hobby}')")
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print('Пльзователь добавлен!')
# create_user('Ardager', 26, 'бегать')
# create_user('John', 16, 'плавать')
# create_user('Oleg', 33, 'спорт')

def read_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    # users = cursor.fetchone() - выдает самого первого
    # users = cursor.fetchmany(2) - выдает первых
    print(users)
    # for i in users:
    #     print(f'NAME: {i[0]} AGE: {i[1]} HOBBY: {i[2]}')
# read_users()

def detail_user(id):
    cursor.execute(
        'SELECT name, age FROM users WHERE id = ?',
        (id,)
    )
    user = cursor.fetchone()
    print(user)
# detail_user(4)

def update_user(name, rowid):
    cursor.execute(
        'UPDATE users SET name = ? WHERE rowid = ?',
        (name, rowid)
    )
    connect.commit()
    print(f'Пользователь с id {rowid} обновлен!')
# update_user('Nikita', 3)

def delete_user(id):
    cursor.execute('DELETE FROm users WHERE id = ?', (id,))
    connect.commit()
    print(f'Пользователь с id {id} удален')
# delete_user(2)

