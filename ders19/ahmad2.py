"""
Proqram:

reqemler.txt faylından rəqəmləri oxusun.
Cəmini hesablasın.
Faylda ədədi olmayan dəyərlər varsa, "Səhv məlumat tapıldı!" yazsın və həmin sətri ötürsün. Amma hər bir halda
ədədlərin cəmini versin.

try-except-else-finally istifadə etməyə çalışın.
"""

with open("reqemler.txt", "r") as my_file:
    cem = 0
    for i in my_file:
        try:
            i=i.strip()
            cem+=int(i)
        except ValueError as ve:
            print("Səhv məlumat tapıldı!", ve)

    print(cem)