"""
Abstrakt Şəkil Sinfi

Shape adlı abstrakt sinif yaradın və abstrakt metod area() təyin edin.

Aşağıdakı iki alt sinfi yaradın:
    1. Rectangle: width və height atributları olsun, area() metodunu width * height qaytaracaq şəkildə implement etsin.
    2. Circle: radius atributu olsun, area() metodunu π * radius^2 qaytaracaq şəkildə implement etsin.

Hər iki sinifdən obyekt yaradın və onların sahələrini ekrana çıxarın.
"""
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
if __name__=="__main__":
    rectangle=Rectangle(6,8)
    circle=Circle(1)
    print(circle.area())
    print(rectangle.area())
