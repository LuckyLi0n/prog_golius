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

stone = gr.Oval(gr.Point(30, 355), gr.Point(120, 320))
stone.setFill('lightgray')
stone.setOutline("lightgray")



sea.draw(window)
cloud1.draw(window)
cloud2.draw(window)
cloud3.draw(window)
cloud4.draw(window)
cloud5.draw(window)
sun.draw(window)
island.draw(window)
boat.draw(window)
boat1.draw(window)
sail1.draw(window)
sail2.draw(window)
house.draw(window)
roof.draw(window)
windows.draw(window)
line1.draw(window)
line2.draw(window)
stone.draw(window)




window.getMouse()

window.close()