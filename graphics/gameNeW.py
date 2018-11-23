from tkinter import *
import graphics as gr
import random

root = Tk()
root.geometry("600x600")
canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=1)

width = 600
height = 600

balls = []


def generation_balls():
    for number in range(10):
        global ball, x, y, r, dx, dy, oval
        x = random.randint(40, 560)
        y = random.randint(40, 560)
        r = random.randint(15, 40)
        dx = random.randint(-10, 10)
        dy = random.randint(-10, 10)
        red = random.randint(0, 255)
        blue = random.randint(0, 255)
        gree = random.randint(0, 255)
        oval = canvas.create_oval(x - r, y - r, x + r, y + r, fill=gr.color_rgb(red, blue, gree))
        ball = [x, y, r, dx, dy, oval]
        balls.append(ball)


def flight_and_reflection():
    for i in range(len(balls)):
        global ball, x, y, r, dx, dy, oval
        x, y, r, dx, dy, oval = balls[i]
        x += dx
        y += dy
        canvas.move(oval, dx, dy)

        if x + r > width or x - r < 0:
            dx = -dx
        if y + r > height or y - r < 0:
            dy = -dy

        balls[i] = [x, y, r, dx, dy, oval]


def time_handler():
    global freeze
    speed = speed_scale.get()
    if speed == 0:
        print("Заморозка!")
        freeze = True
        return
    flight_and_reflection()
    sleep_dt = 700 - 69*speed
    root.after(sleep_dt, time_handler)


def unfreezer(event):
    global freeze
    if freeze is True:
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

generation_balls()
root.after(10, time_handler)
speed_scale.bind("<Motion>", unfreezer)
root.mainloop()
