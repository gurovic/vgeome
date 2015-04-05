def write(objects):
    writer = open('output', 'w')
    for obj in objects:
        print(type(obj), file=writer)
        print(obj, file=writer)
        print('---', file=writer)
