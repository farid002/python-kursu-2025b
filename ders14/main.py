"""
OOP nin 4 əsas prinsipi:

1. Irsilik (inheritance) – Mövcud sinifin xüsusiyyətlərini və metodlarını yeni sinfə ötürmək.
2. Polimorfizm
3. Enkapsulasiya
4. Absktraksiya
"""

class Heyvan:
    def __init__(self, ad, yash, cheki, boy):
        self.ad = ad
        self.yash = yash
        self.cheki = cheki
        self.boy = boy

    def ses_chixar(self) -> None:
        print("heyvan ses chixarir")

class Qush(Heyvan):
    def __init__(self, ad, yash, cheki: float, boy, qanad_achiqligi=2):
        super().__init__(ad, yash, cheki, boy)
        self.qanad_achiqligi = qanad_achiqligi

    def fly(self):
        print("Qush uchur", self.cheki, "chekisinde")

    def boyumek(self, il):
        self.cheki += (il * 2)
        print(self.cheki)


class Yumurtaveren(Heyvan):
    def __init__(self, ad, yash, cheki: float, boy, surunendirmi=False):
        super().__init__(ad, yash, cheki, boy)
        self.surunendirmi = surunendirmi

    def surun(self):
        print("Surunur", self.cheki, "chekisinde")

    def boyumek(self, il):
        self.cheki += (il * 1)
        print(self.cheki)

class Toyuq(Qush, Yumurtaveren):
    def __init__(self, ad, yash, cheki, boy):
        super(Yumurtaveren).__init__(ad, yash, cheki, boy, False)
        super(Qush).__init__(ad, yash, cheki, boy)


my_qush = Qush("Rex", 2, 2.5, 50, 8)
my_qush.ses_chixar()
my_qush.boyumek(5)

my_toyuq = Toyuq("adTyo", 1,2,50)
print("--")



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

class Doberman(Dog):
    pass

class Pitbull(Dog):
    pass

my_dog = Dog("rex", 5, "Doberman")

my_dog.make_noise()
print(my_dog.name)


class Cat(Animal):
    breed = ""
    def make_noise(self):
        print("Miyav")



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
 - Kodun təkrar istifadəsinin qarşısını alır.
 - Miras alınan kodu dəyişmədən yeni funksiyalar əlavə etmədən istifadə etməyə imkan verir.
 - Siniflər arasında əlaqəni daha səmərəli idarə etməyə kömək edir.
"""
