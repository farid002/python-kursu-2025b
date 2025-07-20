"""
class
"""

"""
import
as
*
from
venv
requirements.txt
"""

# from math import factorial
"""
class Avtomobil:
    # Atrobutelar
    tip = "sedan"
    muherrik_hecmi = 1.5
    hazirki_suret = 0

    def sureti_artir(self, suret_ferqi):
        self.hazirki_suret = self.hazirki_suret + suret_ferqi
    def sureti_azalt(self, suret_ferqi):
        self.hazirki_suret = self.hazirki_suret - suret_ferqi

bmw = Avtomobil()
bmw.sureti_artir(20)
bmw.sureti_artir(20)
bmw.sureti_artir(20)
bmw.sureti_artir(20)
bmw.sureti_azalt(5)
print(bmw.hazirki_suret)
"""

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


"""
snake_case
camelCaseWord  
PascalCase / CapitalCamelCase
"""

"""
attributelar
"""

"""
methodlar
"""

"""
__init__ funksiyası
"""
