import graphics as gr

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

    def draw_cloud(x, y):
        cloud_color = "white"
        circle_centers = [(x, y), (x + 20, y), (x - 15, y + 20),
                          (x + 10, y + 20), (x + 35, y + 20)]
        for x, y in circle_centers:
            circle = gr.Circle(gr.Point(x, y), 20)
            circle.setFill('white')
            circle.setOutline('white')
            circle.draw(window)

    for x, y in [(40, 30), (120, 80), (230, 30)]:
        draw_cloud(x, y)
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

    sail1 = gr.Polygon(gr.Point(102, 145), gr.Point(102, 220), gr.Point(150, 220))
    sail1.setFill('white')
    sail1.setOutline('white')

    sail2 = gr.Polygon(gr.Point(60, 215), gr.Point(98, 160), gr.Point(98, 215))
    sail2.setFill('white')
    sail2.setOutline('white')

    boat.draw(window)
    boat1.draw(window)
    sail1.draw(window)
    sail2.draw(window)


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

    line1 = gr.Line(gr.Point(300, 250), gr.Point(300, 310))
    line1.setWidth(1)
    line1.setOutline('black')

    line2 = gr.Line(gr.Point(265, 280), gr.Point(335, 280))
    line2.setWidth(1)
    line2.setOutline('black')

    house.draw(window)
    roof.draw(window)
    windows.draw(window)
    line1.draw(window)
    line2.draw(window)


def draw_picture():
    draw_nature()
    draw_house()
    draw_boat()


draw_picture()

window.getMouse()

window.close()
