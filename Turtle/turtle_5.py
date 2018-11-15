import turtle
t = turtle.Turtle()
t.shape("turtle")

N = 20

for y in range(10):
    t.penup()
    t.goto(-N/2, -N/2)
    t.pendown()
    for x in range(4):
        t.forward(N)
        t.left(90)
    N += 20
