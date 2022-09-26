from math import sqrt
import check_number as ch

ax, ay, bx, by = ch.check_digit('Введите  координаты x и y для точек а и b (через пробел) - ').split()
coord = []
coord.extend((ax, ay, bx, by))
print(coord) 
distance = lambda x1, y1, x2, y2: (round((sqrt((int(x2) - int(x1)) ** 2 + (int(y1) - int(y2)) ** 2)), 2))
print('Расстояние между точками - ', distance(coord[0], coord[1], coord[2], coord[3]))