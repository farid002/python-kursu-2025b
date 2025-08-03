"""
Animal adlı abstrakt sinif yaradın və abstrakt metod make_sound() təyin edin.

Aşağıdakı iki alt sinfi yaradın:
    1. Dog sinfi make_sound() metodunu "Hav-hav!" qaytaracaq şəkildə implement etsin.
    2. Cat sinfi make_sound() metodunu "Miyov!" qaytaracaq şəkildə implement etsin.

Dog və Cat siniflərindən obyektler yaradın və make_sound() metodunu çağırın.
"""
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "hav hav"
class Cat(Animal):
    def make_sound(self):
        return "miyav"

if __name__=="__main__":
    dog=Dog()
    cat=Cat()
    print(dog.make_sound())
    print(cat.make_sound())