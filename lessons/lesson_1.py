class Hero:
    # Конструктор класса
    def __init__(self, nick_name, lvl, hp):
        # Атрибуты класса
        self.nick_name = nick_name
        self.lvl = lvl
        self.hp = hp
    # Методы класса
    def action(self):
        return f'{self.nick_name}: Hi! This is my base action!'


# объект\экземпляр класса
kirito = Hero('Kirito', 100, 1000)
asuna = Hero( 'Asuna', 100, 1000)

print(kirito.nick_name)
print(kirito.action())