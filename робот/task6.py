import robot
import random
r = robot.rmap()
r.lm('task6')


def task():
    x = random.randint(6, 24)
    y = random.randint(6, 24)
    for a in range(x//2):
        r.pt()
        r.rt()
    r.lt()
    for d in range(y):
        r.dn()
        r.pt()
    for c in range(y):
        r.up()
    for b in range(x//2-1):
        r.rt()
        r.pt()


r.start(task)
