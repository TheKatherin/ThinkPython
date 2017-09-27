import math

def distance(x1,y1, x2,y2):
    dx = x2 - x1
    dy = y1 - y1
    dsquarted = dx**2 + dy**2
    result = math.sqrt(dsquarted)
    return result

print(distance(1, 2, 4, 6))
