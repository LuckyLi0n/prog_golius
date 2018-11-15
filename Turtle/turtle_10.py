import turtle
t = turtle.Turtle()
t.shape("turtle")

for n in range(6):
    for i in range(360):
        t.forward(1)
        t.left(1)
    for k in range(360):
        t.forward(1)
        t.right(1)
    t.left(60)
