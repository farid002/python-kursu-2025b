"""
Abstrakt Şəkil Sinfi

Shape adlı abstrakt sinif yaradın və abstrakt metod area() təyin edin.

Aşağıdakı iki alt sinfi yaradın:
    1. Rectangle: width və height atributları olsun, area() metodunu width * height qaytaracaq şəkildə implement etsin.
    2. Circle: radius atributu olsun, area() metodunu π * radius^2 qaytaracaq şəkildə implement etsin.

Hər iki sinifdən obyekt yaradın və onların sahələrini ekrana çıxarın.
"""
from abc import ABC, abstractmethod
from math import pi, pow
class Shape:
    @abstractmethod
    def area(self):
        pass
class Duzbucaqli(Shape):
    def __init__(self,en,uzun):
        self.en=en
        self.uzun=uzun
    def area(self):
        return self.en*self.uzun
class Yumuru(Shape):
    def __init__(self,r):
        self.r=r
def area(self):
    #return 3,141592653589793238462643383279*self.r**2
    return pi*pow(self.r,2)
if __name__=="__main__":
    a_duzbucaqli=Duzbucaqli(5,5)
    a_daire=Yumuru(3)
    print(a_duzbucaqli.area())
    print(a_daire.area())