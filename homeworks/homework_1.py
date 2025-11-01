class AvatarCharacters:
    def __init__(self, name, element, lvl):
        self.name = name
        self.element = element
        self.lvl = int(lvl)
    def description(self):
        return f'{self.name} - is {self.element}bender, lvl - {self.lvl}'
    def action(self):
        self.lvl += 10
        return self.lvl

aang = AvatarCharacters('Aang', 'air', 90)
katara = AvatarCharacters('Katara', 'water', 80)

print(aang.description())
print(aang.action())
print(katara.description())
print(katara.action())