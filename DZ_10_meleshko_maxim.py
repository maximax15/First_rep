class Auto():
    def __init__(self, brand, age, mark, color='', weight=''):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight
    def move(self):
        print('move')
    def stop(self):
        print('stop')
    def birthday(self):
        self.age += 1
# task2
import time
class truck(Auto):
    def __init__(self,brand, age, mark, max_load, color='', weight=''):
        super().__init__(brand, age, mark, color='', weight='')
        self.max_load = max_load
    def move(self):
        print('attention')
        super().move()
    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)
class car(Auto):
    def __init__(self, brand, age, mark, maxspeed, color='', weight=''):
        super().__init__(brand, age, mark, color='', weight='')
        self.maxspeed = maxspeed
    def move(self):
        print('attention')
        super().move()
        print(f'max speed is {self.maxspeed}')

BMW = car('BMW', 7, "X5", 250, 'red')
BMW.move()
volvo = car('volvo', 10, 'V70', 200)
volvo.move()
audi = truck('audi', 10, 'A8', 240)
audi.move()
audi.load()
honda = truck('honda', 10, 'civic', 240)
honda.move()
honda.load()
# task3
import math

class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other): #если х == у -> True
        return self.x == other.x and self.y == other.y

    def __add__(self, other): #сложение объектов
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self): #обычный вывод информации
        return f'({self.x}, {self.y})'

    def distance_from_origin(self):
        return math.hypot(self.x, self.y) #расстояние между двумя векторами (координатами)

# task3
class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return super().__str__()[:-1] + f', radius={self.radius})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        radius = self.radius + other.radius
        return Circle(radius, x, y)

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = self.radius - other.radius
        return Point(radius, x, y)