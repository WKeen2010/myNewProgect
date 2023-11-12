from time import *
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=200)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
for x in range(60):
    canvas.move(1, 5, 0)
    tk.update()
    sleep(0.05)