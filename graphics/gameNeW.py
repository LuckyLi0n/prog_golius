from tkinter import *
import graphics as gr
import random

root = Tk()
root.geometry("600x600")
canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=1)


global FREEZER
FREEZER = False
Events = []
width = 600
height = 600
visible_area_min = 40
visible_area_max = 560
displacement_min = -10
displacement_max = 10
ball_radius_min = 15
ball_radius_max = 40

color_min = 0
color_max = 255
ball_number = 10

balls = []


class Ball:
    def __init__(self):
        self.x, self.y, self.r, self.dx, self.dy, self.red, self.blue, self.gree, self.oval = 0, 0, 0, 0, 0, 0, 0, 0, 0
        self.oval = 0
        self.ball = []

    def generation_balls(self):
        for number in range(ball_number):
            self.x = random.randint(visible_area_min, visible_area_max)
            self.y = random.randint(visible_area_min, visible_area_max)
            self.r = random.randint(ball_radius_min, ball_radius_max)
            self.dx = random.randint(displacement_min, displacement_max)
            self.dy = random.randint(displacement_min, displacement_max)
            self.red = random.randint(color_min, color_max)
            self.blue = random.randint(color_min, color_max)
            self.gree = random.randint(color_min, color_max)
            self.oval = canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                           fill=gr.color_rgb(self.red, self.blue, self.gree))
            self.ball = [self.x, self.y, self.r, self.dx, self.dy, self.oval]
            balls.append(self.ball)

    def flight_and_reflection(self):
        for i in range(len(balls)):
            self.x, self.y, self.r, self.dx, self.dy, self.oval = balls[i]
            self.x += self.dx
            self.y += self.dy
            canvas.move(self.oval, self.dx, self.dy)

            if self.x + self.r > width or self.x - self.r < 0:
                self.dx = -self.dx
            if self.y + self.r > height or self.y - self.r < 0:
                self.dy = -self.dy

            balls[i] = [self.x, self.y, self.r, self.dx, self.dy, self.oval]


def game():
    ball = Ball()

    def time_handler():
        global FREEZER
        speed = speed_scale.get()
        if speed == 0:
            FREEZER = True
            return
        ball.flight_and_reflection()
        sleep_dt = 700 - 69 * speed
        root.after(sleep_dt, time_handler)

    def unfreeze(event):
        Events.append(event)
        global FREEZER
        if FREEZER is True:
            speed = speed_scale.get()
            if speed != 0:
                FREEZER = False
                root.after(0, time_handler)

    speed_scale = Scale(root, orient=HORIZONTAL, length=300,
                        from_=0, to=10, tickinterval=1, resolution=1)
    speed_scale.pack()

    # Скорость = 1
    speed_scale.set(1)

    ball.generation_balls()
    root.after(10, time_handler)
    speed_scale.bind("<Motion>", unfreeze)
    root.mainloop()


game()
