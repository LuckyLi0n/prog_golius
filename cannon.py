from tkinter import *
from random import randrange as rnd, choice
import math

root = Tk()
root.geometry('800x600')
width = 600
height = 800

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'gray', 'black']

#cannon - пушка  shell - снаряд target - летающая цель


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = r
        self.color = choice(colors)
        self.dx = dx
        self.dy = dy
        self.points = 0
        self.circle = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        self.result = canv.create_text(self.x, self.y, text = self.points)

    def draw(self):
        canv.coords(self.circle, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        #canv.coords(self.result, self.x, self.y)
        #canv.itemconfig(self.result, text = self.points)

    def move(self):
        if (self.x + self.r + self.dx >= width) or (self.x - self.r + self.dx <= 0):
            self.dx = -self.dx
        if (self.y + self.r + self.dy >= height) or (self.y - self.r + self.dy <= 0):
            self.dy = -self.dy

    def collision(self, ball):
        if abs(ball.x - self.x) <= (self.r + ball.r) and abs(ball.y - self.y) <= (self.r + ball.r):
            return True
        else:
            return False
        #a = abs(self.x + self.dx - ball.x)
        #b = abs(self.y + self.dy - ball.y)
        #return (a * a + b * b) ** 0.5 <= self.r + ball.r


class Gun:
    def __init__(self):
        self.power = 10
        self.on = 0
        self.angle = 1
        self.cannon = canv.create_line(20, 450, 50, 420, width=7)

    def begin_shoot(self, event):
        self.on = 1

    def end_shoot(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Ball
        new_ball.r += 3
        self.angle = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.dx = self.power * math.cos(self.angle)
        new_ball.dy = -self.power * math.sin(self.angle)
        balls.append(new_ball)
        self.on = 0
        self.power = 10

    def targetting(self, event=0):
        if event:
            self.angle = math.atan((event.y - 450) / (event.x - 20))
        if self.on:
            canv.itemconfig(self.cannon, fill='orange')
        else:
            canv.itemconfig(self.cannon, fill='black')
        canv.coords(self.cannon, 20, 450, 20 + max(self.power, 20) * math.cos(self.angle),
                    450 + max(self.power, 20) * math.sin(self.angle))

    def power_up(self):
        if self.on:
            if self.power < 100:
                self.power += 1
            canv.itemconfig(self.cannon, fill='orange')
        else:
            canv.itemconfig(self.cannon, fill='black')


mainloop()

import math
from tkinter import *


g = 9.8  # Ускорение свободного падения для снаряда.


class Cannon:
    max_velocity = 1000

    def __init__(self, x, y, canvas):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.shell_num = None  # TODO: оставшееся на данный момент количество снарядов
        self.direction = math.pi / 4

        self.line_length = 100
        self.line = canv.create_line(x + 70, y - 50, 160, 480, width=30, fill="black")
        self.oval = canv.create_oval(x, y, 100, 500, outline="black", fill="black")

    def aim(self, x, y):
        """
        Меняет направление direction так, чтобы он из точки
         (self.x, self.y) указывал в точку (x, y).
        :param x: координата x, в которую целимся
        :param y: координата y, в которую целимся
        :return: None
        """

        self.direction = math.atan((self.y - y)/(self.x - x))

        self.draw()

    def fire(self, dt):
        """
        Создаёт объект снаряда (если ещё не потрачены все снаряды)
        летящий в направлении угла direction
        со скоростью, зависящей от длительности клика мышки
        :param dt:  длительность клика мышки, мс
        :return: экземпляр снаряда типа Shell
        """

        shell = Shell(self.x + 70 + self.line_length*math.cos(self.direction),
                      self.y + - 50 + self.line_length*math.sin(self.direction),
                      self.max_velocity/2, self.max_velocity/2, self.canvas)

        shells.append(shell)

    def draw(self):

        self.canvas.delete(self.line)

        self.line = self.canvas.create_line(
            self.x + 70,
            self.y - 50,
            self.x + 70 + self.line_length*math.cos(self.direction),
            self.y - 50 + self.line_length*math.sin(self.direction), width=30, fill="black"
        )


class Shell:
    global standard_radius
    standard_radius = 30

    def __init__(self, x, y, Vx, Vy, canvas):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vy
        self.r = standard_radius
        x1 = x - standard_radius
        y1 = y - standard_radius
        x2 = x + standard_radius
        y2 = y + standard_radius
        self.delta_x = 0
        self.delta_y = 0


        self.canvas = canvas

        self.oval = self.canvas.create_oval(x1, y1, x2, y2, fill='red', outline="pink")

    def go(self, dt):
        """
        Сдвигает снаряд исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt:
        :return:
        """

        ax, ay = 0, g
        self.delta_x = self.Vx * dt + ax * (dt ** 2) / 2
        self.delta_y = self.Vy * dt + ay * (dt ** 2) / 2
        self.x += self.delta_x
        self.y += self.delta_y
        self.Vx += ax * dt
        self.Vy += ay * dt

        print('x = {}, y = {}'.format(self.x, self.y))
        self.draw()

        # TODO: Уничтожать (в статус deleted) снаряд, когда он касается земли.

    def draw(self):
        self.canvas.move(self.oval, self.delta_x, self.delta_y)

    def detect_collision(self, other):
        """
        Проверяет факт соприкосновения снаряда и объекта other
        :param other: объект, который должен иметь поля x, y, r
        :return: логическое значение типа bool
        """

        length = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return length <= self.r + other.r



class Target:
    standard_radius = 5

    def __init__(self, x, y, Vx, Vy):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vy
        self.r = standard_raduis

    def go(self, dt):
        """
        Сдвигает шарик-мишень исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt:
        :return:
        """

        ax, ay = 0, g
        self.x += self.Vx * dt
        self.y += self.Vy * dt
        self.Vx += ax * dt
        self.Vy += ay * dt

        # TODO: Шарики-мишени должны отражаться от стенок

    def collide(self, other):
        """
        Расчёт абсолютно упругого соударения
        :param other:
        :return:
        """

        pass  # TODO


def mouse_move_handler(event):
    cannon.aim(event.x, event.y)


def mouse_left_click_handler(event):
    cannon.fire(100)


def tick():
    for shell in shells:
        shell.go(0.1)

    root.after(10, tick)


root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

canv.bind('<Motion>', mouse_move_handler)
canv.bind('<Button-1>', mouse_left_click_handler)

shells = []

cannon = Cannon(70, 550, canv)

tick()
root.mainloop()