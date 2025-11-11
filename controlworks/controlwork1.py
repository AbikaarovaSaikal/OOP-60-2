class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        return f"{self.name} готов к бою!"

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp
    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"

class WarriorHero(MageHero):
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"

merlin = MageHero("Merlin", 100, 1000, 150)
conan = WarriorHero("Conan", 50, 1000, 50)
print(merlin.action())
print(conan.action())


class BankAccount:
    bank_name = "Simba"
    def __init__(self, hero: MageHero or WarriorHero, balance, password):
        self.hero = hero
        self._balance = balance
        self.__password = password

    def login(self, password):
        if self.__password == password:
            return f'Приветствую {self.hero.name}, вы вошли в систему!'
        else:
            return 'Неверный пароль!'

    @property
    def full_info(self):
        return f'Имя - {self.hero.name}, баланс: {self._balance}'

    @classmethod
    def get_bank_name(cls):
        return f'Банк: {cls.bank_name}'

    @staticmethod
    def bonus_for_level(lvl):
        return f'Бонус за {lvl} уровень: {lvl * 10} SOM'

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return f'Вместе: {self._balance + other._balance} SOM'
        else:
            return f'Эти герои разных типов!'

    def __eq__(self, other):
        if self.hero.lvl == other.lvl and self.hero.name == other.name:
            return True
        else:
            return False

merlin2 = BankAccount(merlin, 5000, "123qwerty")
conan2 = BankAccount(conan, 3000, "qwerty123")
# print(conan2.__add__(merlin2))
print(merlin2.__str__())
print(conan2.__str__())
print(BankAccount.get_bank_name())
print(BankAccount.bonus_for_level(50))


from abc import ABC, abstractmethod
class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass

class KGSms(SmsService):
    def send_otp(self, phone):
        return f'<text>Код: 1234</text><phone>+996{phone}</phone>'

class RUSms(SmsService):
    def send_otp(self, phone):
        return {"text": "Код: 1234", "phone": f"+7{phone}"}
kgsms = KGSms()
print(kgsms.send_otp(777123456))
