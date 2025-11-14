# Декоратора - функция, которая принимает другую функцию как аргумент и
# возвращает новую функцию, обычно обернутую в допольнительную функциональность.
# Изменяет логику функцию, не затрагивая ее.
#

# class Person:
#
#     def simple_method(self):
#         pass
#
#     @staticmethod
#     def static_method():
#         pass
#
#     @classmethod
#     def class_method(cls):
#         pass

def simple_decorator(func):
    def wrapper():
        print('До выполнения')
        func()
        print('После выполнения')
    return wrapper

@simple_decorator
def test():
    return print('test')

# test()

def greeting_decorator(func):
    def wrapper(name):
        print(f"{func.__name__}")
        print(f"Hello, {name}")
        func(name)
    return wrapper

@greeting_decorator
def greeting(name, age=None, hobby=None): # name попадает в х
    return print(f"How are you, {name}?")

# greeting('Ardager')


def repeat_decorator(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat_decorator(5)
def hello_world():
    return print("Hello World")

# hello_world()

def class_decorator(cls):
    class NewClass(cls):
        def new_method(self):
            return print('I am a new method')
    return NewClass

@class_decorator
class OldClass:
    def old_method(self):
        return print("I am an old method")

# obj_1 = OldClass()   # стал объектом NewClass
# obj_1.new_method()

black_list = ['lya', 'lol']
def admin_decorator(func):
    def wrapper(msg):
        if msg.value in black_list:
            print('Ban!')
        else:
            func()
    return wrapper

@admin_decorator
def send_msg(msg):
    print(msg)

send_msg('Hello')

