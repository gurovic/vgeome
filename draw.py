import tkinter
import geometry
import reader

root = tkinter.Tk()
root.title("GIVEN")
x0, y0 = 300, 300
canvas = tkinter.Canvas(root, width=x0 * 2, height=y0 * 2)
canvas.tkinter.create_line(x0, y0 * 2, x0, 0, arrow=LAST)
canvas.tkinter.create_line(0, y0, x0 * 2, y0, arrow=LAST)
canvas.tkinter.create_text(x0 + x0 - 8, y0 + 8, text='x', font='Arial 8')
canvas.tkinter.create_text(x0 - 8, y0 - y0 + 8, text='y', font='Arial 8')
canvas.tkinter.create_text(x0 - 8, y0 + 8, text='0', font='Arial 8')

points = reader.points
segments = reader.segments
for point_ in points:
    point = geometry.Point(1, 1)
    point.y = -point_[0].y 
    point.x = point_[0].x
    symbol = point_[1]
    canvas.tkinter.create_oval(x0 + point.x, y0 + point.y, x0 + point.x, y0 + point.y)
    canvas.tkinter.create_text(x0 + point.x + 4, y0 + point.y - 4, text=symbol, font='Arial 6', fill='darkblue')
for segment in segments:
    segment[0].A.y = -segment[0].A.y
    segment[0].B.y = -segment[0].B.y
    canvas.tkinter.create_line(x0 + segment[0].A.x, y0 + segment[0].A.y, x0 + segment[0].B.x, y0 + segment[0].B.y)
canvas.tkinter.pack()
root.tkinter.mainloop()
