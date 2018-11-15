import turtle
t = turtle.Turtle()
t.shape("turtle")

N = 180

for step in range(N):
    t.forward(3)
    t.left(360/N)
