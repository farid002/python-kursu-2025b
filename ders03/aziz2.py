"""
İstifadəçinin Yaşına Əsasən Mesaj Göstərin

İstifadəçidən yaşını daxil etməsini istəyin.
Yaşa əsasən kateqoriya təyin edin:
    0-12: “Uşaqsınız.”
    13-19: “Gəncsiniz.”
    20-59: “Böyüksünüz.”
    60 və yuxarı: “Ahılsınız.”
"""
user_age=int(input("Yasinizi yazin"))
if user_age<0:
    print("Yazdiginiz sehfdir.")
if user_age >= 60 :
    print("Ahılsınız")
elif  59 > user_age >=20:
    print("Böyüksünüz")
elif 19 >= user_age >=13:
    print("Gəncsiniz")
elif 12>= user_age >0:
    print("Uşaqsınız")