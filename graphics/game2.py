from tkinter import *
import random
import graphics as gr

root = Tk()
root.geometry('800x800')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


def tick():
    global ball
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    gree = random.randint(0, 255)
    for x, y in [(60, 60), (100, 200), (450, 100), (700, 700), (300, 300)]:
        ball = canv.create_oval(x, y, x+60, y+60, fill=gr.color_rgb(red, blue, gree))


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


def unfreezer(event):
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
speed_scale.set(1);
freeze = False

root.after(10, time_handler)
speed_scale.bind("<Motion>", unfreezer)

root.after_idle(tick)
mainloop()

