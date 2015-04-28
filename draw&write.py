#coding:utf-8
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
from tkinter import *
import random
import sys
import time

root = Tk()
root.title("geometry")
x0, y0 = 300, 300
canvas = Canvas(root, width=x0 * 2, height=y0 * 2)
canvas.create_line(x0, y0 * 2, x0, 0, arrow=LAST)
canvas.create_line(0, y0, x0 * 2, y0, arrow=LAST)
canvas.create_text(x0 + x0 - 8, y0 + 8, text='x', font='Arial 8')
canvas.create_text(x0 - 8, y0 - y0 + 8, text='y', font='Arial 8')
canvas.create_text(x0 - 8, y0 + 8, text='0', font='Arial 8')

points = [[Point(10, 10), 'A1'], [Point(10, 30), 'B1'], [Point(4, 4), 'C1'], [Point(4, 24), 'D1']]
segments = [[Segment(Point(10, 10), Point(10, 30)), 'A1B1'], [Segment(Point(4, 4), Point(4, 24)), 'C1D1']]
for i in range(100):
    points.append([Point(random.randint(-300, 300), random.randint(-300, 300)), LETTERS[random.randint(0, 25)]])
for point1 in points:
    for point2 in points:
        flag = random.randint(0, 100)
        if flag == 1:
            segments.append([Segment(point1[0], point2[0]), point1[1] + point2[1]])

for point_ in points:
    point = Point(1, 1)
    point.y = -point_[0].y
    point.x = point_[0].x
    symbol = point_[1]
    canvas.create_oval(x0 + point.x, y0 + point.y, x0 + point.x, y0 + point.y)
    canvas.create_text(x0 + point.x + 4, y0 + point.y - 4, text=symbol, font='Arial 6', fill='darkblue') 
for segment in segments:
    segment[0].A.y = -segment[0].A.y
    segment[0].B.y = -segment[0].B.y
    canvas.create_line(x0 + segment[0].A.x, y0 + segment[0].A.y, x0 + segment[0].B.x, y0 + segment[0].B.y)

canvas.pack()
root.mainloop()

for segment1 in segments:
    for segment2 in segments:
        if (Line(segment1[0].A, segment1[0].B) & Line(segment2[0].A, segment2[0].B)) == ():
            print(segment1[1] + ' parallel ' + segment2[1])   
for point1 in points:
    for point2 in points:
        for point3 in points:
            if point1 != point2 and point1 != point3 and point2 != point3:
                if point1[0] in Line(point2[0], point3[0]):
                    print(point1[1] + ' ' + point2[1] + ' ' + point3[1] + ' on one line')
