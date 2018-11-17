import turtle
t = turtle.Turtle()
t.shape("turtle")

size = 400
n = 0


def snowflake():
    draw(size, n)
    t.right(120)
    draw(size, n)
    t.right(120)
    draw(size, n)


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


snowflake()

