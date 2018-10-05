<<<<<<< HEAD
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

    stone = gr.Oval(gr.Point(230, 355), gr.Point(320, 320))
    stone.setFill('lightgray')
    stone.setOutline("lightgray")

    sun = gr.Circle(gr.Point(0, 0), 40)
    sun.setFill('yellow')
    sun.setOutline('yellow')

    def draw_cloud_1():
        cloud1 = gr.Circle(gr.Point(60, 30), 20)
        cloud1.setFill('white')
        cloud1.setOutline('white')

        cloud2 = gr.Circle(gr.Point(80, 30), 20)
        cloud2.setFill('white')
        cloud2.setOutline('white')

        cloud3 = gr.Circle(gr.Point(45, 50), 20)
        cloud3.setFill('white')
        cloud3.setOutline('white')

        cloud4 = gr.Circle(gr.Point(70, 50), 20)
        cloud4.setFill('white')
        cloud4.setOutline('white')

        cloud5 = gr.Circle(gr.Point(95, 50), 20)
        cloud5.setFill('white')
        cloud5.setOutline('white')

        cloud1.draw(window)
        cloud2.draw(window)
        cloud3.draw(window)
        cloud4.draw(window)
        cloud5.draw(window)

    def draw_cloud_2():
        cloud6 = gr.Circle(gr.Point(140, 80), 20)
        cloud6.setFill('white')
        cloud6.setOutline('white')

        cloud7 = gr.Circle(gr.Point(160, 80), 20)
        cloud7.setFill('white')
        cloud7.setOutline('white')

        cloud8 = gr.Circle(gr.Point(125, 100), 20)
        cloud8.setFill('white')
        cloud8.setOutline('white')

        cloud9 = gr.Circle(gr.Point(150, 100), 20)
        cloud9.setFill('white')
        cloud9.setOutline('white')

        cloud10 = gr.Circle(gr.Point(175, 100), 20)
        cloud10.setFill('white')
        cloud10.setOutline('white')

        cloud6.draw(window)
        cloud7.draw(window)
        cloud8.draw(window)
        cloud9.draw(window)
        cloud10.draw(window)

    def draw_cloud_3():
        cloud11 = gr.Circle(gr.Point(250, 30), 20)
        cloud11.setFill('white')
        cloud11.setOutline('white')

        cloud12 = gr.Circle(gr.Point(270, 30), 20)
        cloud12.setFill('white')
        cloud12.setOutline('white')

        cloud13 = gr.Circle(gr.Point(235, 50), 20)
        cloud13.setFill('white')
        cloud13.setOutline('white')

        cloud14 = gr.Circle(gr.Point(260, 50), 20)
        cloud14.setFill('white')
        cloud14.setOutline('white')

        cloud15 = gr.Circle(gr.Point(285, 50), 20)
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
    boat = gr.Polygon(gr.Point(230, 225), gr.Point(350, 225), gr.Point(320, 260), gr.Point(260, 260))
    boat.setFill('Chocolate')
    boat.setOutline('Chocolate')

    boat1 = gr.Line(gr.Point(300, 150), gr.Point(300, 225))
    boat1.setWidth(2)
    boat1.setOutline('black')

    sail1 = gr.Polygon(gr.Point(302, 145), gr.Point(302, 220), gr.Point(350, 220))
    sail1.setFill('white')
    sail1.setOutline('white')

    sail2 = gr.Polygon(gr.Point(260, 215), gr.Point(298, 160), gr.Point(298, 215))
    sail2.setFill('white')
    sail2.setOutline('white')

    boat.draw(window)
    boat1.draw(window)
    sail1.draw(window)
    sail2.draw(window)

def draw_house():

    house = gr.Rectangle(gr.Point(20, 210), gr.Point(180,350))
    house.setOutline('gray')
    house.setFill("gray")

    roof = gr.Polygon(gr.Point(20, 210), gr.Point(100, 160), gr.Point(180, 210))
    roof.setFill('black')
    roof.setOutline('black')

    windows = gr.Rectangle(gr.Point(65, 250), gr.Point(135,310))
    windows.setFill('lightblue')
    windows.setOutline('black')

    line1 = gr.Line(gr.Point(100, 250), gr.Point(100, 310))
    line1.setWidth(1)
    line1.setOutline('black')

    line2 = gr.Line(gr.Point(65, 280), gr.Point(135, 280))
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

=======
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

    stone = gr.Oval(gr.Point(230, 355), gr.Point(320, 320))
    stone.setFill('lightgray')
    stone.setOutline("lightgray")

    sun = gr.Circle(gr.Point(0, 0), 40)
    sun.setFill('yellow')
    sun.setOutline('yellow')

    def draw_cloud_1():
        cloud1 = gr.Circle(gr.Point(60, 30), 20)
        cloud1.setFill('white')
        cloud1.setOutline('white')

        cloud2 = gr.Circle(gr.Point(80, 30), 20)
        cloud2.setFill('white')
        cloud2.setOutline('white')

        cloud3 = gr.Circle(gr.Point(45, 50), 20)
        cloud3.setFill('white')
        cloud3.setOutline('white')

        cloud4 = gr.Circle(gr.Point(70, 50), 20)
        cloud4.setFill('white')
        cloud4.setOutline('white')

        cloud5 = gr.Circle(gr.Point(95, 50), 20)
        cloud5.setFill('white')
        cloud5.setOutline('white')

        cloud1.draw(window)
        cloud2.draw(window)
        cloud3.draw(window)
        cloud4.draw(window)
        cloud5.draw(window)

    def draw_cloud_2():
        cloud6 = gr.Circle(gr.Point(140, 80), 20)
        cloud6.setFill('white')
        cloud6.setOutline('white')

        cloud7 = gr.Circle(gr.Point(160, 80), 20)
        cloud7.setFill('white')
        cloud7.setOutline('white')

        cloud8 = gr.Circle(gr.Point(125, 100), 20)
        cloud8.setFill('white')
        cloud8.setOutline('white')

        cloud9 = gr.Circle(gr.Point(150, 100), 20)
        cloud9.setFill('white')
        cloud9.setOutline('white')

        cloud10 = gr.Circle(gr.Point(175, 100), 20)
        cloud10.setFill('white')
        cloud10.setOutline('white')

        cloud6.draw(window)
        cloud7.draw(window)
        cloud8.draw(window)
        cloud9.draw(window)
        cloud10.draw(window)

    def draw_cloud_3():
        cloud11 = gr.Circle(gr.Point(250, 30), 20)
        cloud11.setFill('white')
        cloud11.setOutline('white')

        cloud12 = gr.Circle(gr.Point(270, 30), 20)
        cloud12.setFill('white')
        cloud12.setOutline('white')

        cloud13 = gr.Circle(gr.Point(235, 50), 20)
        cloud13.setFill('white')
        cloud13.setOutline('white')

        cloud14 = gr.Circle(gr.Point(260, 50), 20)
        cloud14.setFill('white')
        cloud14.setOutline('white')

        cloud15 = gr.Circle(gr.Point(285, 50), 20)
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
    boat = gr.Polygon(gr.Point(230, 225), gr.Point(350, 225), gr.Point(320, 260), gr.Point(260, 260))
    boat.setFill('Chocolate')
    boat.setOutline('Chocolate')

    boat1 = gr.Line(gr.Point(300, 150), gr.Point(300, 225))
    boat1.setWidth(2)
    boat1.setOutline('black')

    sail1 = gr.Polygon(gr.Point(302, 145), gr.Point(302, 220), gr.Point(350, 220))
    sail1.setFill('white')
    sail1.setOutline('white')

    sail2 = gr.Polygon(gr.Point(260, 215), gr.Point(298, 160), gr.Point(298, 215))
    sail2.setFill('white')
    sail2.setOutline('white')

    boat.draw(window)
    boat1.draw(window)
    sail1.draw(window)
    sail2.draw(window)

def draw_house():

    house = gr.Rectangle(gr.Point(20, 210), gr.Point(180,350))
    house.setOutline('gray')
    house.setFill("gray")

    roof = gr.Polygon(gr.Point(20, 210), gr.Point(100, 160), gr.Point(180, 210))
    roof.setFill('black')
    roof.setOutline('black')

    windows = gr.Rectangle(gr.Point(65, 250), gr.Point(135,310))
    windows.setFill('lightblue')
    windows.setOutline('black')

    line1 = gr.Line(gr.Point(100, 250), gr.Point(100, 310))
    line1.setWidth(1)
    line1.setOutline('black')

    line2 = gr.Line(gr.Point(65, 280), gr.Point(135, 280))
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

>>>>>>> af75c4d298ce6efd7473b9b0b8e633b7f4ce03bc
window.close()