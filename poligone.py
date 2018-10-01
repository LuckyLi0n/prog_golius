<<<<<<< HEAD
import graphics as gr

window = gr.GraphWin("/", 400, 400)
window.setBackground("skyblue")

sea = gr.Line(gr.Point(0, 250), gr.Point(400, 250))
sea.setWidth(200)
sea.setOutline('deepskyblue')


island = gr.Circle(gr.Point(200, 1175), 900)
island.setFill('gold')
island.setOutline('gold')

cloud1 = gr.Circle(gr.Point(40, 40), 20)
cloud1.setFill('white')
cloud1.setOutline('white')

cloud2 = gr.Circle(gr.Point(60, 40), 20)
cloud2.setFill('white')
cloud2.setOutline('white')

cloud3 = gr.Circle(gr.Point(25, 60), 20)
cloud3.setFill('white')
cloud3.setOutline('white')

cloud4 = gr.Circle(gr.Point(50, 60), 20)
cloud4.setFill('white')
cloud4.setOutline('white')

cloud5 = gr.Circle(gr.Point(75, 60), 20)
cloud5.setFill('white')
cloud5.setOutline('white')

sun = gr.Circle(gr.Point(400, 0), 40)
sun.setFill('yellow')
sun.setOutline('yellow')

aPolygon = Polygon([Point(10,20), Point(30,40), Point(50,60)])
aPolygon.setFill('black')


a = gr.Rectangle(gr.Point(150, 260), gr.Point(300,300))
a.setOutline('red')
a.setFill("red")

sea.draw(window)
a.draw(window)
cloud1.draw(window)
cloud2.draw(window)
cloud3.draw(window)
cloud4.draw(window)
cloud5.draw(window)
sun.draw(window)
island.draw(window)
aPolygon.draw(window)
window.getMouse()

=======
import graphics as gr

window = gr.GraphWin("/", 400, 400)
window.setBackground("skyblue")

sea = gr.Line(gr.Point(0, 250), gr.Point(400, 250))
sea.setWidth(200)
sea.setOutline('deepskyblue')


island = gr.Circle(gr.Point(200, 1175), 900)
island.setFill('gold')
island.setOutline('gold')

cloud1 = gr.Circle(gr.Point(40, 40), 20)
cloud1.setFill('white')
cloud1.setOutline('white')

cloud2 = gr.Circle(gr.Point(60, 40), 20)
cloud2.setFill('white')
cloud2.setOutline('white')

cloud3 = gr.Circle(gr.Point(25, 60), 20)
cloud3.setFill('white')
cloud3.setOutline('white')

cloud4 = gr.Circle(gr.Point(50, 60), 20)
cloud4.setFill('white')
cloud4.setOutline('white')

cloud5 = gr.Circle(gr.Point(75, 60), 20)
cloud5.setFill('white')
cloud5.setOutline('white')

sun = gr.Circle(gr.Point(400, 0), 40)
sun.setFill('yellow')
sun.setOutline('yellow')

aPolygon = Polygon([Point(10,20), Point(30,40), Point(50,60)])
aPolygon.setFill('black')


a = gr.Rectangle(gr.Point(150, 260), gr.Point(300,300))
a.setOutline('red')
a.setFill("red")

sea.draw(window)
a.draw(window)
cloud1.draw(window)
cloud2.draw(window)
cloud3.draw(window)
cloud4.draw(window)
cloud5.draw(window)
sun.draw(window)
island.draw(window)
aPolygon.draw(window)
window.getMouse()

>>>>>>> f8560bdfc3a826f48a2185e505def1372a6bd6cd
window.close()