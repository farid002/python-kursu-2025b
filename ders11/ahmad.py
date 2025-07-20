"""
Tapşırıq 1: Funksiya və Parametrlər
Bir funksiya yazın salamla(ad), hansı ki, istifadəçidən adını parametr kimi qəbul edir və onu salamlayır (heç nə qaytarmır).
"""
def salamla(ad):
    print("Salam", ad)
#salamla(input("ad yazin:"))

"""
Tapşırıq 2: İki Ədədin Cəmi
İki ədədi qəbul edib onların cəmini qaytaran bir funksiya yaradın.
"""
def cem(a,b):
    return a+b
#print(cem(int(input("1ci eded:")),int(input("2ci eded:"))))
"""
Tapşırıq 3: Faktoriyal Hesablama
Bir funksiya yazın faktoriyal(n), hansı ki, verilmiş n ədədinin faktoriyalını hesablayır və qaytarır.
"""
from math import factorial
#print(factorial(int(input())))

def fak(n):
    if n<0:
        print("dogru eded gir")
    else:
        faktorial = 1
        while n > 0:
            faktorial*=n
            n-=1
        return faktorial
#print("faktorial:" , fak(int(input())))
"""
Tapşırıq 4: main() funksiyası yazım, hansı ki 3 parameter, ad və 2 integer ədəd alıb, istifadəçini salamlayıb, ədədləri
toplayıb faktorialını print edir. Yuxarıda yazdığınız funksiyaların hamısını istifadə edin
"""
if __name__=="__main__":
    ad = input("Adiniz:").upper()
    a = int(input("Toplamaq istediyiniz ededleri girin:"))
    b = int(input("Toplamaq istediyiniz ededleri girin:"))
    salamla(ad)
    print(cem(a,b))
    print("Faktorial:",fak(a+b))