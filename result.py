import random
import geometry
import generator

points = generator.points
segments = generator.segments

for point1 in points:
    for point2 in points:
        for point3 in points:
            if point1[0] != point2[0] and point1[0] != point3[0] and point2[0] != point3[0]:
                if point1[0] in geometry.Line(point2[0], point3[0]):
                    print(point1[1] + ' ' + point2[1] + ' ' + point3[1] + ' on one line')

for point1 in points:
    for point2 in points:
        for point3 in points:
            for point4 in points:
                if point1[0] in geometry.Circle(point2[0], point3[0], point4[0]):
                    print(point1[1] + ' ' + point2[1] + ' ' + point3[1] + ' ' + point4[1] + ' on one circle')

for segment1 in generator.segments:
    for segment2 in generator.segments:
        if (geometry.Line(segment1[0].A, segment1[0].B) & geometry.Line(segment2[0].A, segment2[0].B)) == ():
            print(segment1[1] + ' parallel ' + segment2[1])
        if segment1[0] == segment2[0]:
            if segment1 != segment2:
                print(segment1[1] + ' = ' + segment2[1])
