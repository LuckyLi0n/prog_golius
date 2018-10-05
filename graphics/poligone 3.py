import graphics as gr

x = int(input('Введи X (40-70) облаков:'))
y = int(input('Введи Y (30-55) облаков:'))

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

    def draw_cloud_1():
        cloud1 = gr.Circle(gr.Point(x, y), 20)
        cloud1.setFill('white')
        cloud1.setOutline('white')

        cloud2 = gr.Circle(gr.Point(x+20, y), 20)
        cloud2.setFill('white')
        cloud2.setOutline('white')

        cloud3 = gr.Circle(gr.Point(x-15, y+20), 20)
        cloud3.setFill('white')
        cloud3.setOutline('white')

        cloud4 = gr.Circle(gr.Point(x+10, y+20), 20)
        cloud4.setFill('white')
        cloud4.setOutline('white')

        cloud5 = gr.Circle(gr.Point(x+35, y+20), 20)
        cloud5.setFill('white')
        cloud5.setOutline('white')

        cloud1.draw(window)
        cloud2.draw(window)
        cloud3.draw(window)
        cloud4.draw(window)
        cloud5.draw(window)

    def draw_cloud_2():
        cloud6 = gr.Circle(gr.Point(x+80, y+50), 20)
        cloud6.setFill('white')
        cloud6.setOutline('white')

        cloud7 = gr.Circle(gr.Point(x+100, y+50), 20)
        cloud7.setFill('white')
        cloud7.setOutline('white')

        cloud8 = gr.Circle(gr.Point(x+65, y+70), 20)
        cloud8.setFill('white')
        cloud8.setOutline('white')

        cloud9 = gr.Circle(gr.Point(x+90, y+70), 20)
        cloud9.setFill('white')
        cloud9.setOutline('white')

        cloud10 = gr.Circle(gr.Point(x+115, y+70), 20)
        cloud10.setFill('white')
        cloud10.setOutline('white')

        cloud6.draw(window)
        cloud7.draw(window)
        cloud8.draw(window)
        cloud9.draw(window)
        cloud10.draw(window)

    def draw_cloud_3():
        cloud11 = gr.Circle(gr.Point(x+190, y), 20)
        cloud11.setFill('white')
        cloud11.setOutline('white')

        cloud12 = gr.Circle(gr.Point(x+210, y), 20)
        cloud12.setFill('white')
        cloud12.setOutline('white')

        cloud13 = gr.Circle(gr.Point(x+175, y+20), 20)
        cloud13.setFill('white')
        cloud13.setOutline('white')

        cloud14 = gr.Circle(gr.Point(x+200, y+20), 20)
        cloud14.setFill('white')
        cloud14.setOutline('white')

        cloud15 = gr.Circle(gr.Point(x+225, y+20), 20)
        cloud15.setFill('white')
        cloud15.setOutline('white')

        cloud11.draw(window)
        cloud12.draw(window)
        cloud13.draw(window)
        cloud14.draw(window)
        cloud15.draw(window)
    draw_cloud_1()
    draw_cloud_2()
    draw_cloud_3()
    sea.draw(window)
    sun.draw(window)
    island.draw(window)
    stone.draw(window)

def draw_boat():
    boat = gr.Polygon(gr.Point(30, 225), gr.Point(150, 225), gr.Point(120, 260), gr.Point(60, 260))
    boat.setFill('Chocolate')
    boat.setOutline('Chocolate')

    boat1 = gr.Line(gr.Point(100, 150), gr.Point( 100, 225))
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

    house = gr.Rectangle(gr.Point(220, 210), gr.Point(380,350))
    house.setOutline('gray')
    house.setFill("gray")

    roof = gr.Polygon(gr.Point(220, 210), gr.Point(300, 160), gr.Point(380, 210))
    roof.setFill('black')
    roof.setOutline('black')

    windows = gr.Rectangle(gr.Point(265, 250), gr.Point(335,310))
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