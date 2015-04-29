LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random
import geometry
points = []
segments = []
p_num = 100
s_num = 10

points = [[geometry.Point(random.randint(-300, 300), random.randint(-300, 300)), LETTERS[random.randint(0, 25)]] for i in range(p_num)]
segments = []
for point1 in points:
    for point2 in points:
        if point1[0] != point2[0]:
            flag = random.randint(1, p_num ** 2 / s_num)
            if flag == 1:
                segments.append([geometry.Segment(point1[0], point2[0]), point1[1] + point2[1]])
