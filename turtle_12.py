import turtle
turtle.shape("turtle")
turtle.left(90)
for i in range(5):
    for i in range(180):
        turtle.forward(1)
        turtle.right(1)
    for i in range(180):
        turtle.forward(0.2)
        turtle.right(1)