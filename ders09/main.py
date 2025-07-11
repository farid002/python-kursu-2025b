"""
----------------------------------------SET-----------------------------------------------
- Unikal (təkrarlanmayan dəyərlər)
- Dəyişdirilə bilən (mutable)
Hesablama əməliyyatları: kəsişmə, birləşmə
"""
from traceback import print_tb

my_list = [1,2,3]
my_tuple = (1,2,3)
my_set = {1,3,5}
my_set_2 = {3,5}
my_set_3 = {3,5}
print(my_set.issubset(my_set_2))

if 4 in my_set:
    print("4 setde var")
print(my_set)
for i, element in enumerate(my_set):
    print(element)

print("------")
"""
----------------------------------SET FUNKSIYALARI----------------------------------------
METOD / FUNKSIYA	            AÇIQLAMA  

add()	                        Set-ə yeni element əlavə edir  
clear()	                        Set-in bütün elementlərini silir  
copy()	                        Set-in surətini çıxarır  
difference()	                İki və ya daha çox set arasındakı fərqi qaytarır  
difference_update()	            Fərqi hesablayır və ilkin set-i yeniləyir  
discard()	                    Verilmiş elementi set-dən silir (əgər varsa)  
intersection()	                İki və ya daha çox set arasında ortaq elementləri qaytarır  
intersection_update()	        Ortaq elementləri hesablayır və ilkin set-i yeniləyir  
isdisjoint()	                İki set-in ortaq elementi olub-olmadığını yoxlayır  
issubset()	                    Bir set-in digərinin alt toplusu olub-olmadığını yoxlayır  
issuperset()	                Bir set-in digərini tam əhatə edib-etmədiyini yoxlayır  
pop()	                        Set-dən təsadüfi bir elementi çıxarır  
remove()	                    Verilmiş elementi set-dən silir (əgər yoxdursa, səhv verir)  
symmetric_difference()	        İki set arasında yalnız birində olan elementləri qaytarır  
symmetric_difference_update()	Simetrik fərqi hesablayır və ilkin set-i yeniləyir  
union()	                        İki və ya daha çox set-in birləşməsini qaytarır  
update()	                    Digər set-in elementlərini mövcud set-ə əlavə edir  
"""



my_set.add(100)
print(my_set)
my_set.remove(3)
print(my_set.pop())
print(my_set.pop())
my_set.clear()
print("--------")
my_set1 = {1,2,3,4}
my_set2 = {3,4}

print("my_set1 - myset2", my_set1.difference(my_set2))
#my_set1.difference_update(my_set2)
#my_set1 = my_set1.difference(my_set2)
print(my_set2.issuperset(my_set1))
print("my_set1", my_set1)
print("my_set2", my_set2)

print(my_set2.difference(my_set1))
print(my_set2.symmetric_difference(my_set1))
print(my_set1.union(my_set2))

print(my_set1.difference(my_set2).union(my_set2.difference(my_set1)))
print(my_set1.intersection(my_set2))

"""
-----------------------------------------DICT-----------------------------------------------
- Çox geniş istifadə yerləri
- Böyük datalarda sürətli proses (açarlarla indeks)
- Dəyişdirilə bilən (mutable)
"""

print("--------------")
my_dict = {
    "a": None,
    "b": [1,2,4],
    "c": 45.5
}
print(my_dict["b"][2])


my_dict = {
    "900524623": {
        "ad": "huseyn",
        "soyad": "a",
        "tel": {
            "dasd": 5
        }
    },
    "900524624": {
        "ad": "murad",
        "soyad": "b",
        "tel": 456
    },
    "9005245624": {
        "ad": "b",
        "soyad": "b",
        "tel": 456
    },
    "9005584624": {
        "ad": "ehmed",
        "900524623": 45654654,
        "aile":{
            "ad1": "f",
            "ad2": "a"
        }
    }
}

my_dict_keys = list(my_dict.keys())
print(type(my_dict_keys))
my_dict_keys.sort()
print(my_dict_keys)
print("+++++++++++++++++")





["Huseyn", "Murad", "Zahid"]

my_dict["ferid"] = {"soyad": "Huseynov"}
#my_dict["ferid"]["soyad"] = "Huseynov"

if "ferid" not in my_dict:
    my_dict["ferid"] = {}
my_dict["ferid"]["soyad"] = "Huseynov"





my_tuple = (3,4,5)
my_dict["500"] = my_dict["900524624"]


#print(my_dict["zahid"])
print("--------")
#my_dict["aaa"] = my_dict["murad"]
my_str = "ad"
#my_dict.pop(f"mur{my_str}")
print(my_dict)
print("--------------------")
print(my_dict.items())

print("-----------")

for key in my_dict:
    print(key)

for key, value in my_dict.items():
    print(key)

for key in my_dict.keys():
    print(key)

#for value in my_dict["zahid"].values():
    #print(value)

print("--------------------")
print(my_dict.get("hh"))


for key, value in my_dict.items():
    print(key, value)

"""
---------------------------------------None data tipi-------------------------------------------
"""
print("-----")
a = list()


ab = [90,80,50,45,55,50,70,85]   # 0x8000 - 0x8064
ab_raw = ab.copy()
ab.sort()
b = ab.copy()
ab = ab_raw
print(ab)


b = 5
if b > 6:
    a = " "

if a:
    print(a)
else:
    pass



"""
Hansı vəziyyətlərdə hansını seçməliyik?

Tuple:
    Məlumatlar dəyişməz olmalı və sırası önəmli olduğu zaman. 
    Məsələn, koordinatlar, tarixlər, funksiya nəticələrinin qruplaşdırılması.
Set: 
    Təkrarlanmayan unikal elementlərin saxlanılması və ya hesablama əməliyyatlarının edilməsi lazım olduqda. 
    Məsələn, unikal qiymətlər, verilənlər üzərində kəsişmə əməliyyatı.
Dictionary: 
    Açar-dəyər cütləri ilə verilənlərin saxlanılması və tez bir şəkildə verilənlərə daxil olmaq lazım olduğunda. 
    Məsələn, istifadəçi məlumatları, məhsul kataloqu.
NoneType: 
    Heç bir dəyər göstərilmədikdə və ya funksiyaların heç bir nəticə qaytarmadığı zaman istifadə olunur. 
    Məsələn, funksiyaların geri dönüş növü yoxdur və ya başlanğıc dəyər olaraq None təyin edilir.
"""


"""
indiyə qədər öyrəndiyimiz data tipləri:

int
float
str
bool
list
+
set
tuple
dict
None
"""

"""
Mutable (dəyişdirilə bilən), Immutable (dəyişdirilə bilməyən) Data tipləri

Mutable:
    - list
    - dict
    - set

Immutable:
    - int
    - float
    - str
    - bool
    - tuple

Dict'lərin keyləri mütləq immutable olmalıdır!
"""