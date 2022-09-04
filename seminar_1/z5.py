import math

def distance_between_points(x1, y1, x2, y2):
    distance = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
    result = math.sqrt(distance)
    return result

x1 = int(input('Input X1 - '))
y1 = int(input('Input Y1 - '))
x2 = int(input('Input X2 - '))
y2 = int(input('Input Y2 - '))

print('Result - ', distance_between_points(x1, y1, x2, y2))