"""
Tapşırıq 1: Funksiya və Parametrlər
Bir funksiya yazın salamla(ad), hansı ki, istifadəçidən adını parametr kimi qəbul edir və onu salamlayır (heç nə qaytarmır).
"""
def salamla(ad):
    print("salam",ad)
"""
Tapşırıq 2: İki Ədədin Cəmi
İki ədədi qəbul edib onların cəmini qaytaran bir funksiya yaradın.
"""
def cemi(a,b):
    return a+b
"""
Tapşırıq 3: Faktoriyal Hesablama
Bir funksiya yazın faktoriyal(n), hansı ki, verilmiş n ədədinin faktoriyalını hesablayır və qaytarır.
"""
def faktoriyal(n):
    if n<0:
        print("dogru reqem gir")
    faktorial=1
    for i in range(2,n+1):
        faktorial=faktorial*i
    return faktorial
"""
Tapşırıq 4: main() funksiyası yazın, hansı ki 3 parameter: ad və 2 integer ədəd alıb, istifadəçini salamlayıb, ədədləri
toplayıb faktorialını print edir. Yuxarıda yazdığınız funksiyaların hamısını istifadə edin
"""
if __name__=="__main__":
    ad = input("Adiniz: ")
    a=int(input("a elave et"))
    b=int(input("b elave et"))
    salamla(ad)
    print(faktoriyal(a+b))
