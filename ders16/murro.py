from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class  Dog(Animal):
    def make_sound(self):
        print("hav hav")
class Cat(Animal):
    def make_sound(self):
        print("meow")

sosan=Cat()
pofuduk=Dog()
sosan.make_sound()
pofuduk.make_sound()