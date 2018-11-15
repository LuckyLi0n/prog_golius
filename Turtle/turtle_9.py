import turtle
t = turtle.Turtle()
t.shape("turtle")

x = 0
y = 0
a = 50
k = 3
o = 18

for aa in range(11):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(k):
        t.forward(a)
        t.left(360/k)
    a += 20
    k += 1
    y -= o
    o += 7
    x -= 10
