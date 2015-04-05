def enter():
    reader = open('input', 'r')
    objects = reader.readlines()
    for obj in objects:
        obj = obj.split()
        if obj[0] == 'Point':
            obj = Point(int(obj[1]), int(obj[2]))
        if obj[0] == 'Vector':
            obj = Vector(int(obj[1]), int(obj[2]))
        if obj[0] == 'Segment':
            obj = Segment(Point(int(obj[1]), int(obj[2])), 
                             Point(int(obj[3]), int(obj[4])))
        if obj[0] == 'Line':
            if len(obj) == 5:
                obj = Line(Point(int(obj[1]), int(obj[2])), 
                              Point(int(obj[3]), int(obj[4])))
            if len(obj) == 4:
                obj = Line(int(obj[1]), int(obj[2]), int(obj[3]))
        if obj[0] == Circle:
            obj = Circle(Point(int(obj[1]), int(obj[2])), int(obj[3]))
        if obj[0] == Triangle:
            obj = Triangle(Point(int(obj[1]), int(obj[2])), 
                              Point(int(obj[3]), int(obj[4])), 
                              Point(int(obj[5]), int(obj[6])))
    
    return objects

def write(objects):
    writer = open('output', 'w')
    for obj in objects:
        print(type(obj), file=writer)
        print(obj, file=writer)
        print('---', file=writer)
