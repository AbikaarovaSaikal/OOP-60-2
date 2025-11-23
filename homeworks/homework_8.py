import sqlite3

connect = sqlite3.connect('family.db')
cursor = connect.cursor()

def create_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS family(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (20) NOT NULL
    ) 
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sum_expenses INTEGER NOT NULL,
        category VARCHAR (30) NOT NULL,
        family_id INTEGER NOT NULL,
        FOREIGN KEY(family_id) REFERENCES family(id)
    )
    ''')

create_table()

def insert_family(name):
    cursor.execute(
        'INSERT INTO family (name) VALUES (?)',
        (name,)
    )
    connect.commit()
    print('Данные члена семьи сохранены')
# insert_family('Геннадий Букин')
# insert_family('Дарья Букина')
# insert_family('Светлана Букина')
# insert_family('Роман Букин')
# insert_family('Барон')

def insert_expense(sum_expenses, category, family_id):
    cursor.execute(
        'INSERT INTO expenses (sum_expenses, category, family_id) VALUES (?, ?, ?)',
        (sum_expenses, category, family_id)
    )
    connect.commit()
    print('Данные расходов сохранены')
# insert_expense(200, 'Еда', 1)
# insert_expense(2200, 'Одежда', 2)
# insert_expense(1000, 'Кино', 4)
# insert_expense(1500, 'Салон красоты', 2)
# insert_expense(800, 'Косметика', 3)
# insert_expense(1400, 'Одежда', 3)
# insert_expense(100, 'Еда', 8)
#

def get_family_expenses():
    cursor.execute('''
    SELECT family.name, expenses.category, expenses.sum_expenses
    FROM family RIGHT JOIN expenses ON family.id = expenses.family_id
    ''')
    users = cursor.fetchall()
    print(users)
# get_family_expenses()


def get_all_expenses():
    cursor.execute(
        'SELECT family.name, SUM(expenses.sum_expenses) FROM family LEFT JOIN expenses ON family.id = expenses.family_id'
    )
    users = cursor.fetchall()
    print(f'Все расходы и кто их покрыл: {users}')
# get_all_expenses()

def get_high_expenses():
    cursor.execute('''
        SELECT name FROM family WHERE id IN (
            SELECT family_id FROM expenses
            WHERE sum_expenses >= 1400
        );
        '''
    )
    users = cursor.fetchall()
    print(users)
# get_high_expenses()

def create_expenses_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS expenses_view AS
        SELECT family.name, expenses.category, expenses.sum_expenses
        FROM family FULL OUTER JOIN expenses ON family.id = expenses.family_id
    ''')
    connect.commit()
create_expenses_view()

def get_family():
    cursor.execute('SELECT * FROM expenses_view')
    users = cursor.fetchall()
    print(users)
get_family()