"""
İstifadəçinin Yaşına Əsasən Mesaj Göstərin

İstifadəçidən yaşını daxil etməsini istəyin.
Yaşa əsasən kateqoriya təyin edin:
    0-12: “Uşaqsınız.”
    13-19: “Gəncsiniz.”
    20-59: “Böyüksünüz.”
    60 və yuxarı: “Ahılsınız.”
"""

age = int(input("Nece yasiniz var: "))
if age<0:
    print("Xəta yasinizi dogru daxil edin")
elif 12>=age>=0:
    print("Hele usaqsan")
elif 19>=age>=13:
    print("Cavansan kef ele")
elif 59>=age>=20:
    print("Boyuksuz")
else:
    print("Ahilsiniz")