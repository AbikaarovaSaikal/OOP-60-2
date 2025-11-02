# Наследование

# родительский\супер Класс
class Hero:
    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
    # Методы класса
    def action(self):
        return self.name

class Profile:
    pass

# дочерний класс
class MageHero(Hero, Profile):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f'Я потомок {self.name}'

obj_1 = Hero('Oleg', 10, 100)
obj_2 = MageHero('Ardager', 10, 100, 200)

# print(obj_1.action())
# print(obj_2.action())

# class A:
#     def action(self):
#         return 'A'
#
# class B(A):
#     def action(self):
#         return 'B'
#
# class C(A):
#     def action(self):
#         return 'C'
#
# class D(C, B):
#     pass
#     # def action(self):
#     #     return 'A'
# obj_4 = D()
# print(obj_4.action())

class Animal:
    def action(self):
        return 'Animal'


class Swim(Animal):
    def action(self):
        return 'Swim'

class Fly(Animal):
    def action(self):
        return 'Fly'

class Duck(Swim, Fly):
    ...
duck = Duck()

print(duck.action())
