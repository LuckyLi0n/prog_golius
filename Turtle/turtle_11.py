import turtle
t = turtle.Turtle()
t.shape("turtle")

n = 1

t.left(90)
for k in range(6):
    for i in range(360):
        t.forward(n)
        t.left(1)
    for l in range(360):
        t.forward(n)
        t.right(1)
    n += 0.2
