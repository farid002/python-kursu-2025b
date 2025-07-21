"""
class
"""


class Car:
    def __init__(self, teker_sayi=5, brand="sad"):
        self.at_gucu = 150
        self.suret = 15
        self.teker_sayi = teker_sayi
        self.brand = brand
        aa = 5

    def return_all_attributes(self):
        return [self.at_gucu, self.suret, self.brand]

    def qaz_ver(self):
        print(self.brand, "Vinnn Vinnn")

    def eylece_bas(self):
        print("Tormoza basildi")

    def suret_artir(self, suret_ferq: int):
        self.suret += suret_ferq

shamilin_mashini = Car()

shamilin_mashini.suret += 100
print(shamilin_mashini.suret)
shamilin_mashini.suret_artir(50)
print(shamilin_mashini.suret)
print(shamilin_mashini.return_all_attributes())


class Animal:
    def __init__(self, animal_type, feet_count, name, current_position):
        self.animal_type = animal_type
        self.feet_count = feet_count
        self.name = name
        self.current_position = current_position

    def jump(self, distance):
        self.current_position += distance

    def make_noise(self, noise):
        print(noise)

oghuzs_cat = Animal("mammal", 4, "AAAA", 5)
oghuzs_cat.jump(20)
print(oghuzs_cat.current_position)
print(oghuzs_cat.name)
print(oghuzs_cat.make_noise("aa"))


"""
snake_case - deyishkenler, funksiyalar, fayl_adlari (modullar)
camelCaseWord  
PascalCase / CapitalCamelCase - classlar
"""

"""
attributelar - deyishkenler
"""

"""
methodlar - funksiyalar
"""

"""
__init__ funksiyası
"""






#### GELECEK DERSLERDE
"""
import
as
*
from
venv
requirements.txt
"""

# from math import factorial