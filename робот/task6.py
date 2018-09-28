import robot
r = robot.rmap()
r.lm('task6')

def task():
    x=int(input())
    y=int(input())
    for a in range (x//2):
        r.pt()
        r.rt()
    r.lt()
    for d in range(y):
        r.dn()
        r.pt()
    for c in range (y-1):
        r.up()
    for b in range (x//2):
        r.rt()
        r.pt()
r.start(task)