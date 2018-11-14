import robot
r = robot.rmap()
r.lm('task6')
y = 45

x = input("Введите ширину меньше 17")
while True:
    while 1:
        try:
            x = int(x)
            break
        except ValueError:
            x = input("Пожалуйста, введите натуральное число меньше 17")
    if x < 17:
        break
    else:
        x = "d"

y = input("Введите длину меньше 17")
while True:
    while 1:
        try:
            y = int(y)
            break
        except ValueError:
            y = input("Пожалуйста, введите натуральное число меньше 17")
    if y < 17:
        break
    else:
        y = "d"

y -= 1


def task():
    for a in range(x//2):
        r.pt()
        r.rt()
    for d in range(y):
        r.dn()
        r.pt()
    for c in range(y+1):
        r.up()
    for b in range(x//2+1):
        r.pt()
        r.rt()


r.start(task)
