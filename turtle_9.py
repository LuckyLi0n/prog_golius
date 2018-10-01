import turtle
turtle.shape("turtle")
aa=True
x = 0
y = 0
a = 50
k = 3
o=18
while aa:
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(k):
        turtle.forward(a)
        turtle.left(360/k)

    a += 20
    k += 1
    y -=o
    o +=7
    x -=10