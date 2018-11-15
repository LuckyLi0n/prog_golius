import turtle
t = turtle.Turtle()
t.shape("turtle")

t.left(90)
for i in range(5):
    for j in range(180):
        t.forward(1)
        t.right(1)
    for k in range(180):
        t.forward(0.2)
        t.right(1)
