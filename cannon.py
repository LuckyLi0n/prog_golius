from tkinter import *
from random import randrange as rnd, choice
import math

# print (dir(math))

import time

root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'gray', 'black']


class Ball:
    """ Класс ball описывает мяч. """

    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(colors)
        self.circle = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                       fill=self.color)
        self.live = 30

    def coord(self):
        canv.coords(self.circle, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        if self.y <= 500:
            self.Vy -= 1.2
            self.y -= self.Vy
            self.x += self.Vx
            self.Vx *= 0.99
            self.coord()
        else:
            if self.Vx**2+self.Vy**2 > 10:
                self.Vy = -self.Vy/2
                self.Vx = self.Vx/2
                self.y = 499
            if self.live < 0:
                balls.pop(balls.index(self))
                canv.delete(self.circle)
            else:
                self.live -= 1
        if self.x > 780:
            self.Vx = - self.Vx/2
            self.x = 779

    def collision(self, ball):
        if abs(ball.x - self.x) <= (self.r + ball.r) and abs(ball.y - self.y) <= (self.r + ball.r):
            return True
        else:
            return False


class Gun:
    def __init__(self):
        self.power = 10
        self.on = 0
        self.angle = 1
        self.gun = canv.create_line(20, 450, 50, 420, width=7)

    def begin_shoot(self, event):
        self.on = 1

    def end_shoot(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.angle = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.Vx = self.power * math.cos(self.angle)
        new_ball.Vy = -self.power * math.sin(self.angle)
        balls.append(new_ball)
        self.on = 0
        self.power = 10

    def targetting(self, event=0):
        if event:
            self.angle = math.atan((event.y - 450) / (event.x - 20))
        if self.on:
            canv.itemconfig(self.gun, fill='orange')
        else:
            canv.itemconfig(self.gun, fill='black')
        canv.coords(self.gun, 20, 450, 20 + max(self.power, 20) * math.cos(self.angle),
                    450 + max(self.power, 20) * math.sin(self.angle))

    def power_up(self):
        if self.on:
            if self.power < 100:
                self.power += 1
            canv.itemconfig(self.gun, fill='orange')
        else:
            canv.itemconfig(self.gun, fill='black')


class target():
    def __init__(self):
        self.points = 0
        self.circle = canv.create_oval(0, 0, 0, 0)
        self.point = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()
        self.live = 1

    def new_target(self):
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.circle, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.circle, fill=color)

    def hit(self, points=1):
        canv.coords(self.circle, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.point, text=self.points)


target_1 = target()
screen = canv.create_text(400, 300, text='', font='28')
gun_1 = Gun()
bullet = 0
balls = []


def new_game(event=''):
    global Gun, target_1, screen, balls, bullet
    target_1.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', gun_1.begin_shoot)
    canv.bind('<ButtonRelease-1>', gun_1.end_shoot)
    canv.bind('<Motion>', gun_1.targetting)

    target_1.live = 1
    while balls or target_1.live:
        for bal in balls:
            bal.move()
            if bal.collision(target_1) and target_1.live:
                target_1.live = 0
                target_1.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        canv.update()
        time.sleep(0.03)
        gun_1.targetting()
        gun_1.power_up()
    canv.itemconfig(screen, text='')
    canv.delete(Gun)
    root.after(750, new_game)


new_game()

mainloop()
