import graphics as gr
import random

x = random.randint(39, 70)
y = random.randint(20, 45)

window = gr.GraphWin("/", 400, 400)
window.setBackground("skyblue")


def draw_nature():
    sea = gr.Line(gr.Point(0, 250), gr.Point(400, 250))
    sea.setWidth(200)
    sea.setOutline('deepskyblue')

    island = gr.Circle(gr.Point(200, 1175), 900)
    island.setFill('gold')
    island.setOutline('gold')

    stone = gr.Oval(gr.Point(30, 355), gr.Point(120, 320))
    stone.setFill('lightgray')
    stone.setOutline("lightgray")

    sun = gr.Circle(gr.Point(400, 0), 40)
    sun.setFill('yellow')
    sun.setOutline('yellow')

    def draw_cloud(centre_circle_x, centre_circle_y):
        circle_centers = [(centre_circle_x, centre_circle_y), (centre_circle_x + 20, centre_circle_y),
                          (centre_circle_x - 15, centre_circle_y + 20),
                          (centre_circle_x + 10, centre_circle_y + 20), (centre_circle_x + 35, centre_circle_y + 20)]
        for centre_circle_x, centre_circle_y in circle_centers:
            circle = gr.Circle(gr.Point(centre_circle_x, centre_circle_y), 20)
            circle.setFill('white')
            circle.setOutline('white')
            circle.draw(window)

    for circles_x, circles_y in [(40, 30), (120, 80), (230, 30)]:
        draw_cloud(circles_x, circles_y)

    sea.draw(window)
    sun.draw(window)
    island.draw(window)
    stone.draw(window)


def draw_boat():
    boat = gr.Polygon(gr.Point(30, 225), gr.Point(150, 225), gr.Point(120, 260), gr.Point(60, 260))
    boat.setFill('Chocolate')
    boat.setOutline('Chocolate')

    boat1 = gr.Line(gr.Point(100, 150), gr.Point(100, 225))
    boat1.setWidth(2)
    boat1.setOutline('black')

    boat.draw(window)
    boat1.draw(window)

    def draw_sails(centre_circle_x, centre_circle_y):
        circle_centers = [(centre_circle_x, centre_circle_y), (centre_circle_x + 20, centre_circle_y),
                          (centre_circle_x - 15, centre_circle_y + 20),
                          (centre_circle_x + 10, centre_circle_y + 20), (centre_circle_x + 35, centre_circle_y + 20)]
        for centre_circle_x, centre_circle_y in circle_centers:
            circle = gr.Circle(gr.Point(centre_circle_x, centre_circle_y), 20)
            circle.setFill('white')
            circle.setOutline('white')
            circle.draw(window)

    for circles_x, circles_y in [(40, 30), (120, 80), (230, 30)]:
        draw_cloud(circles_x, circles_y)

    for c, v, b, n, m, u in [(102, 145, 102, 220, 150, 220), (60, 215, 98, 160, 98, 215)]:
        sails = gr.Polygon(gr.Point(c, v), gr.Point(c, v + 75), gr.Point(c + 48, v + 75))
        sails.setFill('white')
        sails.setOutline('white')
        sails.draw(window)

    for c, v, b, n, m, u in [(102, 145, 102, 220, 150, 220), (60, 215, 98, 160, 98, 215)]:
        sails = gr.Polygon(gr.Point(c, v), gr.Point(b, n), gr.Point(m, u))
        sails.setFill('white')
        sails.setOutline('white')
        sails.draw(window)


def draw_house():
    house = gr.Rectangle(gr.Point(220, 210), gr.Point(380, 350))
    house.setOutline('gray')
    house.setFill("gray")

    roof = gr.Polygon(gr.Point(220, 210), gr.Point(300, 160), gr.Point(380, 210))
    roof.setFill('black')
    roof.setOutline('black')

    windows = gr.Rectangle(gr.Point(265, 250), gr.Point(335, 310))
    windows.setFill('lightblue')
    windows.setOutline('black')

    house.draw(window)
    roof.draw(window)
    windows.draw(window)

    for start_line_x, start_line_y, end_line_x, end_line_y in [(300, 250, 300, 310), (265, 280, 335, 280)]:
        line = gr.Line(gr.Point(start_line_x, start_line_y), gr.Point(end_line_x, end_line_y))
        line.setWidth(1)
        line.setOutline('black')
        line.draw(window)


def draw_picture():
    draw_nature()
    draw_house()
    draw_boat()


draw_picture()

window.getMouse()

window.close()
