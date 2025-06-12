"""
İstifadəçidən adını alın.

- Adın bütün hərflərini əksinə düzülmüş şəkildə çap edin. ([::-1] slicing istifadə edin)
- Adın içində neçə dəfə "a" hərfi keçdiyini tapın.
- Adı ilk hərfi böyük formatında (title()) çap edin.
"""

ad= input("Adınızı Qeyd Edin: ")
print(f"Adınız tərs formada {ad[::-1]} şəklindədir\n"
f"Adinizda {ad.count("a")} eded a herfi var\n"
f"Adiniz {ad.title()} seklinde yazilir")


