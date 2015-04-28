import geometry
import reader

points = reader.points
segments = reader.segments

for point1 in points:
    for point2 in points:
        for point3 in points:
            if point1 != point2 and point1 != point3 and point2 != point3:
                if point1[0] in geometry.Line(point2[0], point3[0]):
                    print(point1[1] + ' ' + point2[1] + ' ' + point3[1] + ' on one line')

for segment1 in segments:
    for segment2 in segments:
        if (geometry.Line(segment1[0].A, segment1[0].B) & geometry.Line(segment2[0].A, segment2[0].B)) == ():
            print(segment1[1] + ' parallel ' + segment2[1])
        if segment1[0] == segment2[0]:
            print(segment1[1] + ' = ' + segment2[1])
