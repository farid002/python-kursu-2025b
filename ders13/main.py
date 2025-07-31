"""
class
"""

class Car:
    def __init__(self, brand: str, model: str, speed: int):  # constructor
        self.speed = speed
        self.brand = brand
        self.model = model

    def print_all_attr(self):
        a = 5
        b = 7
        print(self.speed, self.brand, self.model, a+b)

    def accel(self, speed_diff):
        self.speed += speed_diff
    
    def brake(self):
        self.speed = 0



ahmads_car = Car(input("Ahmad's Car Brand"), "C220", 120)
ahmads_car.print_all_attr()
ahmads_car.accel(150)
ahmads_car.print_all_attr()
ahmads_car.brake()
ahmads_car.print_all_attr()

"""
farids_car = Car("BMW", "X3", 80)
farids_car.print_all_attr()
print("--")
"""



"""
kebap-case
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