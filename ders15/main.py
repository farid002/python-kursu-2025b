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
    def __init__(self, ad):
        self.ad = ad
    def ses_cixar(self):
        print("Her hansi heyvan sesi")

class It(Heyvan):
    def ses_cixar(self):
        print("Hav hav!")

class Pişik(Heyvan):
    def ses_cixar(self):
        print("Miyav miyav!")

class Car:
    def __init__(self, ad):
        self.ad = ad
    def speed(self):
        pass
    def ses_cixar(self):
        print("Vinn")


it = It("rex")
pishik = Pişik("mestan")
car = Car("merco")

# heyvan.ses_cixar()
# it.ses_cixar()
# pishik.ses_cixar()
# car.ses_cixar()


my_objs = [Heyvan("Rex"), It("Rex"), pishik, car]
for obj in my_objs:
    if hasattr(obj, "ad"):
        print("yes attr")
        print(obj.ad, ": ", end=" ")
    if hasattr(obj, "ses_cixar"):
        print("yes func")
        obj.ses_cixar()

"""
hasattr() - obyektin attributeu ve ya methodu oldugunu yoxla
"""

heyvanlar = [It, Pişik()]

for heyvan in heyvanlar:
    print(heyvan.ses_cixar())  # Eyni metod, fərqli nəticələr

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
"""
Getter və Setter

def get_color(self)
def modify_color(self, color)
"""
print("-------------------------------")
class Car:
    def __init__(self, model, color, speed, year, ):
        self.model = model
        self.__color = color     # Protected atribut
        self.__speed = speed   # Private atribute
        self.__id = str(model) + str(year) + str(color)  # C2202025BLaCKDE

    def _set_color_(self, color):
        self.__color = color

    def get_color(self):
        return  self.__color

class Sedan(Car):
    def __init__(self, model, color, speed):
        super().__init__(model, color, speed)


my_bmw = Sedan("7Serie", "Black", 220)


"""
✅ public – Açıq (standart davranış)
İstənilən yerdən istifadə edilə bilər.
Həm sinifin içindən, həm xaricindən.
Python-da heç bir alt xətt (_) işarəsi yoxdursa, atribut/funksiya public sayılır.
"""

"""
⚠️ _protected – Qismən qapalı
Tək alt xəttlə (_attribute) qeyd olunur.
Bu atribut sinifin içindən və alt siniflərdən (inheritance) istifadə üçün nəzərdə tutulub.
Texniki olaraq tam qadağan etmir, sadəcə "daxili istifadə üçündür" mesajı verir.
"""

"""
⛔ __private – Tam gizli
İki alt xəttlə (__attribute) yazılır.
Bu atribut yalnız sinifin içindən istifadə oluna bilər.
Python atributun adını dəyişdirərək (name mangling) onu gizlədir: __speed → _Car__speed

➡️ Diqqət: Çöldən bu cür müraciət etmək mümkün deyil: car.__engine_status
Amma bu mümkündür (qəbul olunmur, amma mümkündür): car._Car__engine_status
"""
