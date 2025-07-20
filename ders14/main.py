"""
__init__ icinde self-le ve xaricinde attribute ferqi
"""

"""
class Restaurant:
    name = "Z"
    def __init__(self, name):
        self.name = name
    def custom_function(self):
        pass

rest1 = Restaurant("A")
rest2 = Restaurant("B")
rest3 = Restaurant("C")

rest1.custom_function()
rest1.name = "McDonalds"
rest2.name = "Burger2"
"""

"""
OOP nin 4 esas prinsipi:

1. Irsilik (inheritance) – Mövcud sinifin xüsusiyyətlərini və metodlarını yeni sinfə ötürmək.
2. Poliforfizm
3. Enkapsulasiya
4. Absktraksiya
"""

"""
inheritance (irsilik)

Parent - child
"""


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_noise(self):
        print("Animal makes noise")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

my_dog = Dog("rex", 5, "Doberman")

my_dog.make_noise()
print(my_dog.name)





class Cat(Animal):
    breed = ""
    def make_noise(self):
        print("Miyav")

class Doberman(Dog):
    ear_size = 0


"""
my_dog = Doberman()
my_dog.make_noise()
print(my_dog.name)

my_cat = Cat()
my_cat.make_noise()
"""

"""
funksiya overwrite
"""

"""
super() funksiyasi

super() funksiyası parent sinfin metodlarını child sinifdə istifadə etməyə imkan yaradır.
mes.: super().__init__()
"""

"""
İrsiliyin Üstünlükləri
 - Kodun təkrar istifadəsini artırır.
 - Miras alınan kodu dəyişmədən yeni funksiyalar əlavə etməyə imkan verir.
 - Siniflər arasında əlaqəni daha səmərəli idarə etməyə kömək edir.
"""
