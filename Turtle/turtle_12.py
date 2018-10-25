import turtle
turtle.shape("turtle")
turtle.left(90)
for i in range(5):
    for j in range(180):
        turtle.forward(1)
        turtle.right(1)
    for k in range(180):
        turtle.forward(0.2)
        turtle.right(1)
