from tkinter import *
import graphics as gr
import random

root = Tk()
root.geometry("600x600")
canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=1)

red = random.randint(0, 255)
blue = random.randint(0, 255)
gree = random.randint(0, 255)

global ball, x, y, dx, dy

balls = []
for x, y, dx, dy in [(60, 60, 2, 3), (100, 200, 3, 7), (250, 100, -5, 3), (500, 500, 3, 4), (300, 300, -2, -3)]:
    oval = canvas.create_oval(x, y, x + 60, y + 60, fill=gr.color_rgb(red, blue, gree))
    ball = [x, y, dx, dy, oval]
    balls.append(ball)


def tick_handler():
    global ball, x, y, dx, dy, oval
    for ball in balls:
        x, y, dx, dy, oval = ball
        # Отражение от края холста
        if x < 0:
            dx = -dx
            x = 0
        elif x > 600-40:
            dx = -dx
            x = 600-40
        if y < 0:
            dy = -dy
            y = 0
        elif y > 600-40:
            dy = -dy
            y = 600-40
        x = x + dx
        y = y + dy
        canvas.move(oval, dx, dy)
        ball[0] = x
        ball[1] = y
        ball[2] = dx
        ball[3] = dy


def time_handler():
    global freeze
    speed = speed_scale.get()
    if speed == 0:
        print("Заморозка!")
        freeze = True
        return
    tick_handler()
    sleep_dt = 1100 - 100*speed
    root.after(sleep_dt, time_handler)


def unfreezer():
    global freeze
    if freeze == True:
        speed = speed_scale.get()
        if speed != 0:
            freeze = False
            root.after(0, time_handler)


speed_scale = Scale(root, orient=HORIZONTAL, length=300,
                    from_=0, to=10, tickinterval=1, resolution=1)
speed_scale.pack()

# Скорость = 1
speed_scale.set(1)
freeze = False

root.after(10, time_handler)
speed_scale.bind("<Motion>", unfreezer)
root.mainloop()
