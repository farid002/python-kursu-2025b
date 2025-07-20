"""
-----------------------------------FUNKSİYALAR------------------------------------
def açar sözü
"""

def salamla(ad, soyad="aa", yas=18):
    print("salam", ad, soyad)
    if yas:
        print("dogum tarixiniz: ", 2025-yas)

salamla("shamil")

"""
Parametrlər
Defolt dəyər
"""
print("---------")
def dogum_tarixini_hesabla(yash):
    dogum_tarixi = 2025 - yash
    yuzillik = int(dogum_tarixi / 100) + 1

    return dogum_tarixi, yuzillik, "salam"


dt = dogum_tarixini_hesabla(48)
print(dt)
#print("yuzilik", yz)

"""
return açar sözü
çoxsaylı return dəyəri
"""

"""
*args - tuple kimi davranış
**kwargs - dict kimi davranış
"""
print("---------")
"""-----------------------args - bir ulduz - tuple kimi davranir-------------------------"""
def sum_of_numbers(ad, soyad, *args):
    my_sum = sum(args)
    print(ad, soyad, "in yigdigi toplam bal", my_sum)

sum_of_numbers("farid","huseynov",6,5,8,56549,5)

#print("a", "b", "c", "d")

#def print(value1, value2, value3, value4):
    # print eliyir
    #pass

"""----------------------kwargs - iki ulduz - dict kimi davranir------------------------"""
def return_sum(a, b, **kwargs):
    return a + b, kwargs

print(return_sum(1, 2, ad="farid", soyad="hus", age=25))

def send_email(ad, soyad, mesaj, **kwargs):
    for k,v in kwargs.items():
        print(k, "--", v)
    if kwargs:
        print(ad, soyad, mesaj, kwargs)
    else:
        print(ad, soyad, mesaj)

    return ["asdasd"]

# send_email("Farid", "Hus", "sadsasd", tel=54646, yash=45, peshe="adsd")

"""
main funksiyası
"""

if __name__=="__main__":
    a = 5
    b = 7
    print(a + b)
    send_email("asd", "sadsa", "assda")
    return_sum(23, 123, ad="wqedsa")


"""----------------------lambda funksiyaları (ananonim funksiyalar)--------------------------"""
"""
my_func = lambda b,c: b*c
my_func(1, 2)
"""
def vurma_normal(b,c):
    return b*c

vurma = lambda b,c: b*c

print("-------------")

cutleri_tap = lambda eded_list: [eded for eded in eded_list if eded % 2 == 0]
print(cutleri_tap([1,2,5,9,8,36,45,2]))


# vurma(1, 2)

"""
global dəyişkənlər
"""

print("---------")

def func():
    abc.append(4)
    print(abc)

if __name__ == "__main__":
    abc = [1,2,3]
    func()
    print(abc)

