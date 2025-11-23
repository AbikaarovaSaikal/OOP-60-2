import sqlite3

connect = sqlite3.connect('characters.db')
cursor = connect.cursor()

def create_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS characters(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (20) NOT NULL
    ) 
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        grade INTEGER NOT NULL,
        subject VARCHAR (30) NOT NULL,
        student_id INTEGER NOT NULL,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )
    ''')

# many_to_one
# def create_table():
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS studendts(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR (20) NOT NULL
#         grade_id INTEGER NOT NULL,
#         FOREING KEY(grade_id) REFERENCES grades(id)
#     )
#     ''')
#
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS grades(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         grade INTEGER NOT NULL,
#         subject VARCHAR (30) NOT NULL,
#     )
#     ''')

create_table()


def insert_test_db():
    cursor.execute(
        'INSERT INTO students (name) VALUES(?)',
        ('Sasha',)
    )
    cursor.execute(
        'INSERT INTO grades (grade, subject, student_id) VALUES (?,?,?)',
        (80, "History", 99)
    )
    connect.commit()
    print('Данные сохранены')

# insert_test_db()

# INNER - данные из двух таблиц, которые связаны между собой
# RIGHT - все данные правой таблицы
# LEFT - все данные левой таблицы
# FULL OUTER - все данные из обоих таблиц

def get_students_grade():
    cursor.execute('''
    SELECT students.name, grades.subject, grades.grade
    FROM students RIGHT JOIN grades ON students.id = grades.student_id
    ''')
    users = cursor.fetchall()
    print(users)

# get_students_grade()
# MAX, MIN, SUM, COUNT
def get_student_high_grade():
    cursor.execute(
        'SELECT students.name, AVG(grades.subject) FROM students INNER JOIN grades ON students.id = grades.student_id'
    )
    users = cursor.fetchall()
    print(users)

get_student_high_grade()

def get_best_student():

    cursor.execute('''
        SELECT name FROM students WHERE id IN (
            SELECT student_id FROM grades
            WHERE grade >= 50
        );
        '''
    )
    users = cursor.fetchall()
    print(users)

# get_best_student()

def create_my_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS my_view AS
        SELECT students.name, grades.subject, grades.grade
        FROM students LEFT JOIN grades ON students.id = grades.student_id
    ''')
    connect.commit()

# create_my_view()

def get_students():

    cursor.execute('SELECT * FROM my_view')
    users = cursor.fetchall()
    print(users)
get_students()