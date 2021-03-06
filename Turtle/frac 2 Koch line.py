import turtle
t = turtle.Turtle()
t.shape("turtle")


def alignment():
    t.penup()
    t.back(350)
    t.pendown()


def draw(size, n):
    if n == 0:
        t.fd(size)
        return

    a = size / 3
    draw(a, n - 1)
    t.left(60)
    draw(a, n - 1)
    t.right(120)
    draw(a, n - 1)
    t.left(60)
    draw(a, n - 1)


alignment()
draw(800, 0)
