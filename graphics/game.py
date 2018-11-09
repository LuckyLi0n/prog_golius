from tkinter import *
import random
import graphics as gr

root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
score = 0


def tick():
    global x, y, score
    x = random.randint(1, 500)
    y = random.randint(1, 500)
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    canv.delete(ALL)
    canv.create_text(20, 300, text=score, font='Arial 15')
    root.after(1200, tick)
    canv.create_oval(x, y, x+60, y+60, fill=gr.color_rgb(red, blue, green))


def click(event):
    global score, x, y
    a = event.x
    b = event.y
    if a in range(x, x+60) and b in range(y, y+60):
        canv.delete(ALL)
        canv.create_text(20, 300, text=score, font='Arial 15')
        score += 1
    else:
        canv.delete(ALL)
        canv.create_text(20, 300, text=score, font='Arial 15')
        score -= 1
    x = 1000
    y = 1000


canv.bind('<Button-1>', click)
root.after_idle(tick)
mainloop()
