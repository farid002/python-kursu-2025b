"""
ABSTRAKSIYA

 - ABC
 - abstractmethod
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    name = ""
    year = 1970
    speed = 0

    @abstractmethod
    def move(self):
        pass

    def increase_speed(self, speed):
        self.speed += speed

class Car(Vehicle):
    def move(self):
        print("yolda hereket edir")

class Boat(Vehicle):
    def move(self):
        print("suda hereket edir")


my_boat = Boat()
my_boat.move()
my_boat.increase_speed(100)
my_boat.increase_speed(56)
print(my_boat.speed)
print("------------------------------")


# Vehicle-in instansını yaratmaq mümkün deyil:
# vehicle = Vehicle()

car = Car()
car.move()  # Çıxış: Maşın yolda gedir

boat = Boat()
boat.move()  # Çıxış: Qayıq suda üzür

"""
ABC Modulu Olmadan Abstraksiya

class Animal:
    def make_sound(self):
        raise NotImplementedError("Bu metod təyin olunmalıdır.")

class Dog(Animal):
    def make_sound(self):
        return "Hav-hav!"

dog = Dog()
print(dog.make_sound())  # Çıxış: Hav-hav!

cat = Animal()  # Bu xətaya səbəb olacaq, çünki `make_sound` metodu təyin edilməyib.
"""

class Animal:
    def make_sound(self):
        raise NotImplementedError("Bu metod təyin olunmalıdır.")

class Dog(Animal):
    def make_sound(self):
        return "Hav-hav!"

dog = Dog()
print(dog.make_sound())  # Çıxış: Hav-hav!

cat = Animal()
cat.make_sound()


"""
1. Kodun məcburi strukturlaşdırılması - yəni ana sinifdən (class) törəyən classlar mütləq həmin abstract methodları yenidən yazmalıdır
2. Təhlükəsiz obyekt istifadəsi
3. Daha yaxşı dizayn
"""
