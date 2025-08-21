"""
Proqram:

reqemler.txt faylından rəqəmləri oxusun.
Cəmini hesablasın.
Faylda ədədi olmayan dəyərlər varsa, "Səhv məlumat tapıldı!" yazsın və həmin sətri ötürsün. Amma hər bir halda
ədədlərin cəmini versin.

try-except-else-finally istifadə etməyə çalışın.
"""
cem = 0
try:
    my_file=open("reqemler.txt","r")
    for setr in my_file:
        setr=setr.strip()
        value=int(setr)
        cem+=value
except FileNotFoundError:
    print("sehv melumat tapildi")
except ValueError:
    print("Yanlish deyer")

print(cem)




