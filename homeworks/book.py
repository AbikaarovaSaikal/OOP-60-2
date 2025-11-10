class Book:
    def __init__(self, title, author, pages, format='бумажная'): # магический метод для сохранения
        self.title = title
        self.author = author
        self.pages = pages
        self.format = format

    def __str__(self): # маг метод для выведения основной инфо книги
        return f'"{self.title}" - {self.author}, {self.pages} стр'

    def __len__(self): # маг метод для выведения количества страниц
        return self.pages

    def __add__(self, other): # маг метод для выведения суммы страниц двух книг
        return f'Вместе: {self.pages + other.pages} стр'

    def __eq__(self, other): # маг метод для сравнения кол-ва страниц двух книг
        if self.pages == other.pages:
            return True
        else:
            return False

    def __getitem__(self, item): # маг метод, выводит главу соответсвующей книги
        return f'Глава {item}: содержание книги "{self.title}"'

    @classmethod
    def from_string(cls, s): # метод класса, делит строку на атрибуты экземпляра
        title, author, pages = s.split(",")
        return cls(title, author, int(pages))

    @staticmethod
    def is_thick(pages): # статист метод, сравнивает кол-во стр с 500, и возвращает True or False
        if pages > 500:
            return True
        else:
            return False

book1 = Book("1984", "Дж. Оруэлл", 328)
book2 = Book.from_string("Гарри Поттер, Дж. Роулинг, 400")

print(book1)                    # "1984" — Дж. Оруэлл, 328 стр.
print(len(book1))               # 328
print(book1 + book2)            # Вместе: 728 страниц
print(book1 == book2)           # False
print(book1[5])                 # Глава 5: содержание книги '1984'

print(Book.is_thick(600))       # True
print(Book.is_thick(300))       # False

book3 = Book("Python", "Гвидо", 200)
print(book3.format)             # бумажная