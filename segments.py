def give_segments():
    objects = enter()
    points = []
    segments = []
    for obj in objects:
        if type(obj) == Point:
            points.append(obj)
        if type(obj) == Segment:
            points.append(obj.A)
            points.append(obj.B)
        if type(obj) == Triangle:
            points.append(obj.A)
            points.append(obj.B)
            points.append(obj.C)
        if type(obj) == Circle:
            points.append(obj.O)
    for i in range(len(points)):
        for j in range(len(points) - i):
            segments.append(Segment(points[i], points[j]))
    return segments
