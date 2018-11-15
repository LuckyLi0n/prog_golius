import turtle
t = turtle.Turtle()
t.shape("turtle")

a = 0.2

for i in range(12):
    for k in range(180):
        t.forward(a)
        t.left(1)
    a += 0.2
