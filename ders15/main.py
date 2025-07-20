"""
Polimorfizm

1. Sinif (class) səviyyəsində
2. Funksiya səviyyəsində

Məs.:
    def heyvan_sesi(heyvan):
        print(heyvan.ses_cixar())
    class Heyvan:
        def ses_cixar(self):
            pass  # Boş metod, alt siniflər bunu dəyişdirəcək

    class It(Heyvan):
        def ses_cixar(self):
            return "Hav hav!"

    class Pişik(Heyvan):
        def ses_cixar(self):
            return "Miyav miyav!"

    # Obyektlər yaradaq və polimorfizmi test edək
    heyvanlar = [It(), Pişik()]

    for heyvan in heyvanlar:
        print(heyvan.ses_cixar())  # Eyni metod, fərqli nəticələr

"""


def heyvan_sesi(a):
    a.ses_cixar()

class Heyvan:
    def ses_cixar(self):
        print("Her hansi heyvan sesi")

class It(Heyvan):
    def ses_cixar(self):
        print("Hav hav!")

class Pişik(Heyvan):
    def ses_cixar(self):
        print("Miyav miyav!")

class Car:
    def speed(self):
        pass
    def ses_cixar(self):
        print("Vinn")

#menim_heyvanim = Heyvan()
#menim_heyvanim.ses_cixar()

mestan = Pişik()
toplan = It()
random_heyvan = Heyvan()
my_car = Car()

heyvan_sesi(toplan)
heyvan_sesi(mestan)
heyvan_sesi(random_heyvan)
heyvan_sesi(my_car)

"""
# Obyektlər yaradaq və polimorfizmi test edək
heyvanlar = [It(), Pişik()]

for heyvan in heyvanlar:
    print(heyvan.ses_cixar())  # Eyni metod, fərqli nəticələr
"""



"""
Enkapsulyasiya (qapalılıq)

public
_protected
__private
"""
print("-------------------------------")
class Car:
    def __init__(self, model, color, speed):
        self.model = model
        self._color = color     # Protected atribut
        self.__speed = speed   # Private atribut

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

class Sedan(Car):
    def __init__(self, model, color, speed):
        super().__init__(model, color, speed)
        print(self._color)


my_bmw = Sedan("7Serie", "Black", 220)

my_str = "aas"


my_car = Car("Mercedes", "White", 220)
print(my_car.model)
print(my_car._color)   # Çox tövsiyə edilmir (Ancaq mümkündür)
my_car._color = "Black" # Dəyişmək mümkündür, amma qorunan olduğu üçün ehtiyatlı olmaq lazımdır
print(my_car._color)

# print(my_car.__speed)  # Private atributları birbaşa dəyişdirmək və ya birbaşa dəyərlərini almaq mümkün deyil, ancaq sinif daxilindəki metodlarla onları idarə edə bilərik.
print("Getter Speed", my_car.get_speed())
my_car.set_speed(100)
print("Getter Speed After Setter", my_car.get_speed())
print(my_car._Car__speed)  # Amma bu, tövsiyə edilmir! Çünki bu, enkapsulyasiyanı pozur və kodun etibarlılığını azaldır.


"""
Getter və Setter

def get_color(self)
def modify_color(self, color)
"""