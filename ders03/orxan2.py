"""
İstifadəçinin Yaşına Əsasən Mesaj Göstərin

İstifadəçidən yaşını daxil etməsini istəyin.
Yaşa əsasən kateqoriya təyin edin:
    0-12: “Uşaqsınız.”
    13-19: “Gəncsiniz.”
    20-59: “Böyüksünüz.”
    60 və yuxarı: “Ahılsınız.”
"""
yas=int(input("sizin yasiniz"))
if yas<13:
    print("usaqsiniz")
elif yas<20:
    print("gencsiniz")
elif yas<60:
    print("boyuksunuz")
else:
    print("ahilsiniz")

