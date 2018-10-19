from tkinter import *
import random
import graphics as gr

root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
i = 0


def tick():
    global x, y,i
    x = random.randint(1, 500)
    y = random.randint(1, 500)
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    gree = random.randint(0, 255)
    canv.delete(ALL)
    i -= 1
    canv.create_text(20, 300, text=i, font='Arial 15')
    root.after(1200, tick)
    canv.create_oval(x, y, x+60, y+60, fill=gr.color_rgb(red, blue, gree))



def click(event):
    global i, x, y
    a = event.x
    b = event.y
    if a in range(x, x+60) and b in range(y, y+60):
        canv.delete(ALL)
        canv.create_text(20, 300, text=i, font='Arial 15')
        i += 2
    else:

        canv.delete(ALL)
        canv.create_text(20, 300, text=i, font='Arial 15')
    x = 1000
    y = 1000

canv.bind('<Button-1>', click)
root.after_idle(tick)
mainloop()
