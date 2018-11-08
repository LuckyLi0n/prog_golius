import math
from tkinter import *

root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

g = 9.8  # Ускорение свободного падения для снаряда.


def draw_cannon():
    canv.create_line(70, 550, 160, 480, width=30, fill="black")
    canv.create_oval(0, 600, 100, 500,outline="black", fill="black")


class Cannon:
    max_velocity = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shell_num = None  # TODO: оставшееся на данный момент количество снарядов
        self.direction = math.pi / 4

    def aim(self, x, y):
        """
        Меняет направление direction так, чтобы он из точки
         (self.x, self.y) указывал в точку (x, y).
        :param x: координата x, в которую целимся
        :param y: координата y, в которую целимся
        :return: None
        """

        pass  # TODO

    def fire(self, dt):
        """
        Создаёт объект снаряда (если ещё не потрачены все снаряды)
        летящий в направлении угла direction
        со скоростью, зависящей от длительности клика мышки
        :param dt:  длительность клика мышки, мс
        :return: экземпляр снаряда типа Shell
        """

        pass


class Shell:
    global standard_radius
    standard_radius = 30

    def __init__(self, x, y, Vx, Vy):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vy
        self.r = standard_radius
        x1 = x - standard_radius
        y1 = y - standard_radius
        x2 = x + standard_radius
        y2 = y + standard_radius
        canv.create_oval(x1, y1, x2, y2, fill='red', outline="pink")

    def go(self, dt):
        """
        Сдвигает снаряд исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt:
        :return:
        """

        ax, ay = 0, g
        self.x += self.Vx * dt + ax * (dt ** 2) / 2
        self.y += self.Vy * dt + ay * (dt ** 2) / 2
        self.Vx += ax * dt
        self.Vy += ay * dt

        # TODO: Уничтожать (в статус deleted) снаряд, когда он касается земли.

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


shell2 = Shell(80, 98, 86, 86)

draw_cannon()
root.mainloop()