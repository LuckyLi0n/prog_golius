from gameunit import *
from random import randint, choice


class Enemy(Attacker):
    def __init__(self):
        self.__quest = None
        self.__answer = None


def generate_random_dragon():
    random_dragon_type = choice(dragon_types)
    dragon = random_dragon_type()
    return dragon


def generate_dragon_list(dragon_number):
    dragon_list = [generate_random_dragon() for dragon in range(dragon_number)]
    return dragon_list


def generate_random_troll():
    random_troll_type = choice(troll_types)
    troll = random_troll_type()
    return troll


def generate_troll_list(troll_number):
    troll_list = [generate_random_troll() for troll in range(troll_number)]
    return troll_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 20
        self._color = 'зеленый'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 20
        self._color = 'красный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest


class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 20
        self._color = 'черный'

    def question(self):
        x = randint(1, 11)
        y = randint(1, 11)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest


class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GoofyTroll(Troll):
    def __init__(self):
        self._health = 50
        self._attack = 10
        self._character = 'бестолковый'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = "Целая часть " + str(x) + '/' + str(y)
        self.set_answer(x // y)
        return self.__quest


class GreedyTroll(Troll):
    def __init__(self):
        self._health = 50
        self._attack = 90
        self._character = 'жадный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = "Остаток от " + str(x) + '/' + str(y)
        self.set_answer(x % y)
        return self.__quest


class DangerousTroll(Troll):
    def __init__(self):
        self._health = 50
        self._attack = 100
        self._character = 'опасный'

    def question(self):
        x = randint(1, 5)
        y = randint(1, 4)
        self.__quest = str(x) + '^' + str(y)
        self.set_answer(x**y)
        return self.__quest


dragon_types = [GreenDragon, RedDragon, BlackDragon]
troll_types = [DangerousTroll, GreedyTroll, GoofyTroll]
