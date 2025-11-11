import random
import string

class BankAccount:
   def __init__(self, name, balance, password):
       self.name = name
       self._balance = balance
       self.__password = password

   def deposit(self, amount, password):
        self.amount = amount
        if self.__password == password:
            self._balance += self.amount
            return self._balance
        else:
            return "Неверный пароль!"

   def withdraw(self, amount, password):
        self.amount = amount
        if self.__password == password and self._balance >= self.amount:
            self._balance -= self.amount
            return self._balance
        elif self.__password == password and self._balance <= self.amount:
            return "Недостаточно средств!"
        else:
            return "Неверный пароль!"

   def change_password(self, old_password, new_password):
        self.old_password = old_password
        self.new_password = new_password
        if self.old_password == self.__password:
            self.__password = self.old_password
            return "Пароль изменён"
        else:
            return "Старый пароль неверный"

   def get_balance(self, password):
        if self.__password == password:
            return self._balance
        else:
            return "Неверный пароль!"

   def __generate_pin(self):
       chart = string.digits
       pin = ''.join(random.choice(chart) for _ in range(4))
       return pin

   def reset_pin(self, password):
        if self.__password == password:
            new_pin = self.__generate_pin()
            self.__password = new_pin
            return new_pin
        else:
            return "Неверный пароль!"

john = BankAccount("John", 100, "123qwerty")

# print(john.deposit(50, "123qwerty"))
# print(john.withdraw(200, "123qwerty"))
# print(john.get_balance("123qwerty"))
# print(john.change_password("wrong", "new"))
# print(john.reset_pin("123qwerty"))
# print(john.get_balance("4467"))

from abc import ABC, abstractmethod

class NotificationSender(ABC):
   @abstractmethod
   def send(self, message, recipient):
       pass
   def get_service(self):
       return f"Сервис: {self._service}"

class EmailSender(NotificationSender):
    def __init__(self):
        self._service = "Gmail"
    def send(self, message, recipient):
        return f"Email sent to {recipient}"

class SmsSender(NotificationSender):
    def __init__(self):
        self._service = "Twilio"
    def send(self, message, recipient):
        return f"SMS sent to {recipient}" # or return f"SMS sent to system"

class PushSender(NotificationSender):
    def __init__(self):
        self._service = "Firebase"
    def send(self, message, recipient):
        return f"Push sent to {recipient}"


email = EmailSender()
# print(email.send("Привет", "john@mail.ru"))
# print(email.get_service())

class UserAuth:
   def __init__(self, username, account: BankAccount, notifier: NotificationSender):
       self.username = username
       self.account = account
       self.notifier = notifier

   def login(self, password):
       balance = self.account.get_balance(password)
       if isinstance(balance, int):
           print(self.notifier.send(f"Успешный вход: {self.username}", "system"))
           return True
       else:
           return False

   def transfer(self, amount, password, recipient_account: BankAccount):
       balance = self.account.get_balance(password)
       if not isinstance(balance, int):
           return False

       if self.account.withdraw(amount, password):
           recipient_account._balance += amount
           print(self.notifier.send(f'Перевод {amount} отправлен', "system"))
           print(self.notifier.send(f'Получено {amount} от {self.username}', 'system'))
           return True
       else:
           return False

john2 = BankAccount("John", 100, "secret")
alice = BankAccount("Alice", 100, "pass123")
notifier = SmsSender()
auth = UserAuth("john_doe", john, notifier)
auth.login("secret")
auth.transfer(20, "secret", alice)
print(f"Перевод успешен. Новый баланс: {john._balance}")
print(f"John balance: {john._balance}")
print(f"Alice balance: {alice._balance}")


print(john.deposit(150, "123qwerty"))
print(john.withdraw(100, "123qwerty"))
print(john.get_balance("123qwerty"))
print(john.change_password("helo", "new"))
print(john.change_password("123qwerty", "new"))
# print(john.reset_pin("123qwerty"))
new_pin = john.reset_pin("123qwerty")
print(new_pin)
print(john.get_balance(new_pin))

print(email.send("Helo!", "test@mail.ru"))
print(email.get_service())
sms = SmsSender()
print(sms.get_service())

john = BankAccount("John", 100, "secret")
alice = BankAccount("Alice", 100, "pass123")
notifier = SmsSender()
auth = UserAuth("john_doe", john, notifier)
auth.login("secret")
auth.transfer(20, "secret", alice)
print(f"Перевод успешен. Новый баланс: {john._balance}")
print(f"John balance: {john._balance}")
print(f"Alice balance: {alice._balance}")