import turtle
turtle.shape("turtle")
for n in range (6):
    for i in range(360):
        turtle.forward(1)
        turtle.left(1)
    for i in range(360):
        turtle.forward(1)
        turtle.right(1)
    turtle.left(60)