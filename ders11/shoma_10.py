"""
Tapşırıq 1: Funksiya və Parametrlər
Bir funksiya yazın salamla(ad), hansı ki, istifadəçidən adını parametr kimi qəbul edir və onu salamlayır (heç nə qaytarmır).
"""

"""
Tapşırıq 2: İki Ədədin Cəmi
İki ədədi qəbul edib onların cəmini qaytaran bir funksiya yaradın.
"""

"""
Tapşırıq 3: Faktoriyal Hesablama
Bir funksiya yazın faktoriyal(n), hansı ki, verilmiş n ədədinin faktoriyalını hesablayır və qaytarır.
"""

"""
Tapşırıq 4: main() funksiyası yazım, hansı ki 3 parameter, ad və 2 integer ədəd alıb, istifadəçini salamlayıb, ədədləri
toplayıb faktorialını print edir. Yuxarıda yazdığınız funksiyaların hamısını istifadə edin
"""
#1

def salamla(ad):
    print(f"Salam {ad}")

def topla(a,b):
    return a + b

def faktoriyal(n):
    fakt=1
    for i in range(1,n + 1):
        fakt *= i
    return fakt

if __name__=="__main__":
    ad = input("adiniz: ")
    a = int(input("birinci eded "))
    b = int(input("ikinci eded "))
    salamla(ad)
    cem = topla(a,b)
    print(cem)
    faktoriyal_cem=faktoriyal(a) + faktoriyal(b)
    print(faktoriyal_cem)


