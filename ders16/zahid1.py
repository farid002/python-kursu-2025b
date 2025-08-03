"""
Animal adlı abstrakt sinif yaradın və abstrakt metod make_sound() təyin edin.

Aşağıdakı iki alt sinfi yaradın:
    1. Dog sinfi make_sound() metodunu "Hav-hav!" qaytaracaq şəkildə implement etsin.
    2. Cat sinfi make_sound() metodunu "Miyov!" qaytaracaq şəkildə implement etsin.

Dog və Cat siniflərindən obyektler yaradın və make_sound() metodunu çağırın.
"""
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,ad):
        self.ad=ad
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Hav-hav!🐶🐕")

class Cat(Animal):
    def __init__(self,ad, pence_sayi):
        super().__init__(ad)
        self.pence_sayi=pence_sayi
    def make_sound(self):
        print("Meowww😺🐈")
if __name__=="__main__":
    kuche_iti=Dog("Adsiz")
    mestan=Cat("Mestan", 5)
    kuche_iti.make_sound()
    mestan.make_sound()
