class Animal:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type


class Dolphin(Animal):
    def description(self):
        description = 'Я ' + self.type + '. ' + 'Меня зовут ' + self.name + ', ' + 'мне ' + self.age + '.'
        return description


class Zebra(Animal):
    def description(self):
        description = 'Я ' + self.type + '. ' + 'Меня зовут ' + self.name + ', ' + 'мне ' + self.age + '.'
        return description


d = Dolphin("Семен", "40", "дельфин")
z = Zebra("Зинаида", "56", "зебра")

print(z.description())
print(d.description())
