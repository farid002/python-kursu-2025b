"""
İstifadəçinin Yaşına Əsasən Mesaj Göstərin

İstifadəçidən yaşını daxil etməsini istəyin.
Yaşa əsasən kateqoriya təyin edin:
    0-12: “Uşaqsınız.”
    13-19: “Gəncsiniz.”
    20-59: “Böyüksünüz.”
    60 və yuxarı: “Ahılsınız.”
"""

yas = int(input("Yasinizi daxil edin:"))
if yas < 0:
    print("Yasinizi duzgun daxil edin")
elif yas >= 60:
    print("Ahılsınız.")
elif yas >= 20:
    print("Böyüksünüz.")
elif yas >= 13:
    print("Gəncsiniz.")
else:
    print("Uşaqsınız")


