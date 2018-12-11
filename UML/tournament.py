from enemies import *
from hero import *


def annoying_input_int(message=''):
    answer = None

    while answer is None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list, troll_list):

    for dragon in dragon_list:
        print('Вышел', dragon._color, 'дракон!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** дракон кричит от боли **')
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... ** \n** дракон отвлекся **')
                for troll in troll_list:
                    print('Из-за куста выскакивает', troll._character, 'троль! ')
                    while troll.is_alive() and hero.is_alive():
                        print('Вопрос:', troll.question())
                        answer = annoying_input_int('Ответ:')

                        if troll.check_answer(answer):
                            hero.attack(troll)
                            print('Верно! \n** троль громко ругается **')
                        else:
                            troll.attack(hero)
                            print('Ошибка! \n** вам нанесён удар... **')
                    if troll.is_alive():
                        break
                    print(troll._character, 'тролль', 'повержен!\n')
                    troll_number = 1
                    troll_list = generate_troll_list(troll_number)
                print('Вернулся', dragon._color, 'дракон!')
        if dragon.is_alive():
            break
        print('Дракон', dragon._color, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')
        print('Хотите начать заново? (Для подтверждения введите "Да")')
        if input() == 'Да':
            start_game()


def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с коварными драконами и хитрыми троллями!')
        print('Представьтесь, пожалуйста: ', end='')
        hero = Hero(input())

        dragon_number = 3
        troll_number = 1
        dragon_list = generate_dragon_list(dragon_number)
        troll_list = generate_troll_list(troll_number)
        assert(len(dragon_list) == 3)
        print('У Вас на пути', dragon_number, 'драконов!')
        game_tournament(hero, dragon_list, troll_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
