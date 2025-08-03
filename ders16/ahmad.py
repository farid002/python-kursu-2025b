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
        print("hav-hav")

class Cat(Animal):
    def make_sound(self):
        print("miyav")

if __name__ == "__main__":
    mesi = Cat()
    coban_iti = Dog()
    mesi.make_sound()
    coban_iti.make_sound()