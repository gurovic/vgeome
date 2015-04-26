from tkinter import *
import sys
import time

points = [Point(1, 1), Point(10, 20)]
x0, y0 = 300, 300
root = Tk()
canvas = Canvas(root, width = x0 * 2, height = y0 * 2)
canvas.create_line(x0, y0 * 2, x0, 0, arrow=LAST)
canvas.create_line(0, y0, x0 * 2, y0, arrow=LAST)

for point in points:
    point.y = -point.y
    canvas.create_oval(x0 + point.x - 1, y0 + point.y - 1, x0 + point.x + 1, y0 + point.y + 1)

canvas.pack()
root.mainloop()
