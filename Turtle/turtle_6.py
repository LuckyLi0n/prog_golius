import turtle
t = turtle.Turtle()
t.shape("turtle")

for i in range(12):
    t.forward(100)
    t.stamp()
    t.goto(0, 0)
    t.right(30)
