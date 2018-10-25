import turtle
N = 20
for y in range(10):
    turtle.penup()
    turtle.goto(-N/2, -N/2)
    turtle.pendown()
    for x in range(4):
        turtle.forward(N)
        turtle.left(90)
    N += 20
