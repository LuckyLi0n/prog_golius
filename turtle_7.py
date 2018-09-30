import turtle
turtle.shape("turtle")
a = 0.2
for i in range(12):
    for t in range(180):
        turtle.forward(a)
        turtle.left(1)
    a += 0.2