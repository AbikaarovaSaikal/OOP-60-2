# Инкапсуляция

#
import random
import string

class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name # открытая
        self._balance = balance # Защищенная атрибута
        self.__password = password # Приватная атрибута

    def login(self, password):
        if self.__password == password:
            print("Вы вошли!!")
        else:
            print("Не верный пароль!!")

    def get_balance(self, password):
        if self.__password == password:
            return self._balance
        else:
            return "не верный пароль!!"

    def __random_pass(self):
        chart = string.ascii_letters + string.digits
        password = ''.join(random.choice(chart) for _ in range(6))
        return password

    def get_new_pass(self):
        return self.__random_pass()

#
#
#
#
# john = BankAccount("John", 100, "123qwerty")
#
# # john.login("123321")
# # print(john.get_balance("123qwerty"))
# # print(john.get_new_pass())
#
#
#
#
#
#
#
from abc import ABC, abstractmethod


# Абстрактный класс
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):

    def make_sound(self):
        return "Gaf Gaf"

    def move(self):
        return "Step"

# gufi = Dog()

# print(gufi.make_sound())

class SmsSend(ABC):

    @abstractmethod
    def send_otp(self):
        pass

class KGSms(SmsSend):

    def send_otp(self):
        text = "<text>1234</text>"
        phone = "<phone>+996779</phone>"
        # self.send(text, phone)

class RUSms(SmsSend):

    def __init__(self, text):
        self.text = text

    def send_sms(self, data):
        pass

    def send_otp(self):
        data = {
            "text": self.text,
            "phone": "+7925"
        }
        self.send_sms(data)