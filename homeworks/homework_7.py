import sqlite3

connect = sqlite3.connect('books.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR (50) NOT NULL,
    author VARCHAR (40) NOT NULL,
    year INTEGER NOT NULL,
    genre TEXT
    )
''')
# connect.commit()

def create_book(title, author, year, genre):
    cursor.execute(
        'INSERT INTO books(title, author, year, genre) VALUES (?, ?, ?, ?)',
        (title, author, year, genre)
    )
    connect.commit()
    print('Добавлена новая книга!')

# create_book('1984', 'Джордж Оруэлл', 1948 ,'Антиутопия, Научная фантастика')
# create_book('Собор Парижской Богоматери', 'Виктор Гюго', 1831 ,'Французская литература')
# create_book('Убить пересмешника', 'Харпер Ли', 1961 ,'Историческая литература')
# create_book('Незнакомка из Уайлдфелл-Холла', 'Энн Бронте', 1848 ,'Романтика, Британская литература')
# create_book('Гордость и предубеждение', "Джейн Остин", 1813, "Романтика")

def read_books():
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    for i in books:
        print(f'TITLE: {i[1]} AUTHOR: {i[2]} YEAR: {i[3]} GENRE: {i[4]}')
# read_books()

def detail_book(id):
    cursor.execute(
        'SELECT * FROM books WHERE id = ?',
        (id,)
    )
    book = cursor.fetchone()
    print(book)
# detail_book(4)

def update_book(title, id):
    cursor.execute(
        'UPDATE books SET title = ? WHERE id = ?',
        (title, id)
    )
    connect.commit()
    print(f'Название книги под номером {id} обновлено!')
# update_book('Убить Пересмешника', 3)

def delete_book(id):
    cursor.execute('DELETE FROM books WHERE id = ?', (id,))
    connect.commit()
    print(f'Книга под номером {id} удалена!')
# delete_book(5)