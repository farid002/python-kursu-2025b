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
def salamla(ad):
    print(f"salam {ad}")

def ededlerin_cemi(a,b):
    my_sum = a + b
    return my_sum

def faktoriyal(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

if __name__=="__main__":
    my_name = input()
    my_num1 = int(input())
    my_num2 = int(input())

    salamla(my_name)
    my_sum = ededlerin_cemi(my_num1,my_num2)
    print(my_sum)
    print(faktoriyal(my_sum))



