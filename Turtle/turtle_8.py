import turtle
t = turtle.Turtle()
t.shape("turtle")

N = 10

for i in range(50):
    t.forward(N)
    t.left(90)
    N += 10
