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
Tapşırıq 4: main() funksiyası yazın, hansı ki 3 parameter: ad və 2 integer ədəd alıb, istifadəçini salamlayıb, ədədləri
toplayıb faktorialını print edir. Yuxarıda yazdığınız funksiyaların hamısını istifadə edin
"""
""" 1-CI TAPSIRIQ """
def salamla(ad):
    print("Salam",ad)
""" 2-CI TAPSIRIQ """
def sum(a,b):
    return a+b
""" 3-CU TAPSIRIQ """
def factorial(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    return res
""" 4-CU TAPSIRIQ """
if __name__=="__main__":
    salamla(input("Adinizi  yazin"))
    print(factorial(sum(int(input("a: ")),int(input("b: ")))))
