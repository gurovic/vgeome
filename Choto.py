import geometry
import reader

data = data()

def new_height(triangle):
    height_1 = Segment(triangle.A, Line(triangle.C, triangle.B).perpendicular_line(triangle.A) & Line(triangle.C, triangle.B))
    height_2 = Segment(triangle.B, Line(triangle.A, triangle.C).perpendicular_line(triangle.B) & Line(triangle.A, triangle.C))
    height_3 = Segment(triangle.C, Line(triangle.A, triangle.B).perpendicular_line(triangle.C) & Line(triangle.A, triangle.B))                   
    return([height_1, height_2, height_3])
    
def new_bisector(triangle):    
    bisector_1 = Segment(triangle.A, Line(triangle.A, triangle.incenter()) & Line(triangle.B, triangle.C))
    bisector_1 = Segment(triangle.B, Line(triangle.B, triangle.incenter()) & Line(triangle.A, triangle.C))
    bisector_1 = Segment(triangle.C, Line(triangle.C, triangle.incenter()) & Line(triangle.B, triangle.A))
    return [bisector_1, bisector_2, bisector_3]

def new_median(tringle):
    median_1 = Segment(triangle.A, Segment(triangle.B, triangle.C).midle())
    median_2 = Segment(triangle.A, Segment(triangle.B, triangle.C).midle())
    median_3 = Segment(triangle.A, Segment(triangle.B, triangle.C).midle())
    return [median_1, median_2, median_3] 
    
def new_Cevian(triangle):
    list_1 = new_height(triangle)
    list_2 = new_bisector(triangle)
    list_3 = new_median(triangle)
    data[segment] = data[segment]  + list_1 + list_2 + list_3

def new_middle():
    data[point] += [triangle.AB.midle(), triangle.AC.midle(), triangle.CB.midle()

def incenter(triangle):
    pass

def ortocenter(triangle):
    return circle(triangle.A, triangle.C, triangle.B)

def excircle(triangle):
    pass                
                    
def new_circle(triangle):
    list_1 = incenter(triangle)
    list_2 = ortocenter(triangle)                
  
def main():
    for triangle in data[triangle]:
        new_Cevian(triangle)
        new_middle(triangle)
        new_circle(triangle)            
