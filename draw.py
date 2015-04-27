from tkinter import *
import sys
import time


root = Tk()
root.title("geometry")
x0, y0 = 300, 300
canvas = Canvas(root, width = x0 * 2, height = y0 * 2)
canvas.create_line(x0, y0 * 2, x0, 0, arrow=LAST)
canvas.create_line(0, y0, x0 * 2, y0, arrow=LAST)
canvas.create_text(x0 + x0 - 8, y0 + 8, text='x', font='Arial 8')
canvas.create_text(x0 - 8, y0 - y0 + 8, text='y', font='Arial 8')
canvas.create_text(x0 - 8, y0 + 8, text='0', font='Arial 8')


points = []
segments = []
for i in range(100):
    points.append([Point(random.randint(-300, 300), random.randint(-300, 300)), LETTERS[random.randint(0, 25)]])
for point1 in points:
    for point2 in points:
        flag = random.randint(0, 1000)
        if flag == 1:
            segments.append(Segment(point1[0], point2[0]))
for point_ in points:
    point = Point(1, 1)
    point.y = -point_[0].y
    point.x = point_[0].x
    symbol = point_[1]
    canvas.create_oval(x0 + point.x, y0 + point.y, x0 + point.x, y0 + point.y)
    canvas.create_text(x0 + point.x + 4, y0 + point.y - 4, text=symbol, font='Arial 6', fill='darkblue') 
for segment in segments:
    segment.A.y = -segment.A.y
    segment.B.y = -segment.B.y
    canvas.create_line(x0 + segment.A.x, y0 + segment.A.y, x0 + segment.B.x, y0 + segment.B.y)

canvas.pack()
root.mainloop()
