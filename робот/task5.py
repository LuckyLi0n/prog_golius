import robot
r = robot.rmap()
r.lm('task5')

def task():
    for y in range(3):
        for x in range(4):
            r.pt()
            r.dn()
            r.rt()
            r.pt()
            r.rt()
            r.up()
            r.pt()
            if r.fr():
                r.rt()
                r.rt()
        r.dn()
        r.dn()
        r.dn()
        while r.fl():
            r.lt()

r.start(task)