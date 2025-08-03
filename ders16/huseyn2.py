"""
Abstrakt Şəkil Sinfi

Shape adlı abstrakt sinif yaradın və abstrakt metod area() təyin edin.

Aşağıdakı iki alt sinfi yaradın:
    1. Rectangle: width və height atributları olsun, area() metodunu width * height qaytaracaq şəkildə implement etsin.
    2. Circle: radius atributu olsun, area() metodunu π * radius^2 qaytaracaq şəkildə implement etsin.

Hər iki sinifdən obyekt yaradın və onların sahələrini ekrana çıxarın.
"""

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        rec_area = self.width * self.height
        return rec_area

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        cir_area = (self.radius ** 2) * pi
        return round(cir_area, 2)

if __name__ == '__main__':
    my_rec = Rectangle(5,6)
    print(my_rec.area())

    my_cir = Circle(4)
    print(my_cir.area())
