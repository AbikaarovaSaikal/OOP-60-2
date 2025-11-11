class Test:
    # double underline - магический метод
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __call__(self, *args, **kwargs): # увеличивал кол-во просмотров
        pass

    def __new__(cls, *args, **kwargs): # отрабатывает в момент обращения к классу
        pass

# int_test = 123
# int_test2 = 1233
#
# print(int_test > int_test2)

# test_obj = Test('test')
#
# test_str = '123'
#
# print(test_obj)

class Vector:
    def __init__(self, x, y, array):
        self.x = x
        self.y = y
        self.array = array

    def __lt__(self, other):
        return self.x < other.x

    def __gt__(self, other):
        return self.y > other.x

    def __getitem__(self, item): # список
        return self.array[item]

class Mylist:

    def __init__(self, value):
        self.value = value

    def __getitem__(self, item):
        return self.value[item]

# my_list = Mylist([1, 2, 3]) # мы создали
# origin_list = [1, 2, 3] # встроенный лист
#
# print(my_list[2])
# print(origin_list[2])

# obj_1 = Vector(1, 2, [1, 2, 3])
# # obj_2 = Vector(3, 4)
# print(obj_1[3])

class Money:
    def __init__(self, sum, currency):
        self.sum = sum
        self.currency = currency
    # ==
    def __eq__(self, other):
        if self.currency == other.currency:
            return True
        else:
            return False
    # +
    def __add__(self, other):
        if self.currency == other.currency:
            return self.sum + other.sum
        else:
            return f'Валюты не равны: {self.currency} и {other.currency}'

# SOM = Money(100, 'SOM')
# SOM2 = Money(100, 'SOM')
# USD = Money(100, 'USD')
# print(SOM + USD)
# print(SOM + SOM2)

class BankAccount:
    # Атрибута класса, хранятся в самом классе
    bank_name = 'Simba'

    def __init__(self, name, balance):
        # Атрибута экземпляра класса, без объекта не создается
        self.name = name
        self.balance = balance
    def get_name(self):
        return self.name

    @classmethod # не работает с объектами, вместо self есть cls(ссылка на сам класс)
    def get_bank_name(cls):
        return cls.bank_name

    @staticmethod # Нужен когда не будет использ экземпляр и класс
    def get_balance():
        return 123

# argader = BankAccount("Ardager", 10000)
# print(BankAccount.get_bank_name()) # позволяет работать с самим классом
# print(argader.get_name())
print(BankAccount.get_balance())

class ServiceCalculate:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    @staticmethod
    def calculate_deposit(amount, procent):
        return amount * procent
# print(ServiceCalculate.calculate_deposit(12, 2))

