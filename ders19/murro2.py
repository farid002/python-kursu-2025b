"""
Proqram:

reqemler.txt faylından rəqəmləri oxusun.
Cəmini hesablasın.
Faylda ədədi olmayan dəyərlər varsa, "Səhv məlumat tapıldı!" yazsın və həmin sətri ötürsün. Amma hər bir halda
ədədlərin cəmini versin.

try-except-else-finally istifadə etməyə çalışın.
"""
cem=0
try:
    with open("reqemler.txt","r") as f:
        for setr in f:
            setr= setr.strip()
            try:
                reqem=int(setr)
                cem+= reqem
            except ValueError:
                print("sehv melumta tapildi")
except FileNotFoundError:
    print("umumi error")

print(cem)

