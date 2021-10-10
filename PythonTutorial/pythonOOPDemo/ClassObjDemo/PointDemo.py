from math import sqrt


class Point :
    def __init__(self,x,y,z):
        self.x=x;
        self.y = y;
        self.z = z;
    def __str__(self):
        return 'point : (x:{},y:{},z:{})'.format(self.x,self.y,self.z)
    def distance(self,p2):
        distance = sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2 + (self.z - p2.z) ** 2)
        return distance
    def __add__(self, p3):
        return f'{self} + {p3}'

p1 = Point(4, 2, 9)
p2 = Point(4, 5, 6)
p3 = Point(-2, -1, 4)
print(p2 +p3)
print(p2.distance(p3))