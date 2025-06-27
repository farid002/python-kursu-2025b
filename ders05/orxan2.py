"""
Müəyyən bir zoopark qonağın yaşına əsasən biletin qiymətini müəyyən edir.

 - 2 yaş və daha kiçik qonaqlar ödənişsiz qəbul edilir.
 - 3-12 yaş arası uşaqlar 14.90 dollara başa gəlir.
 - 65 yaşdan yuxarı yaşlılar üçün 18.90 dollara başa gəlir.
 - Bütün digər qonaqlar üçün giriş 23.90 dollardır.

Hər sətirdə bir yaş daxil edilməklə, istifadəçidən qrupdakı bütün qonaqların yaşlarını oxumaqla başlayan proqram yaradın.
İstifadəçi qrupda artıq qonaq olmadığını bildirmək üçün boş sətir (enter və ya space) daxil edəcək.

Sonra proqramınız müvafiq mesajla qrup üçün biletlərin ümumi qiymətini göstərməlidir.
Son qiymət nöqtədən sonra iki onluq rəqəmdən istifadə etməklə göstərilməlidir (Məs. 89.70)

Qaynaq: The Python Workbook, Ben Stephenson
"""
total_qiymet = 0
while True:
    yas = input("yasinizi daxil edin")
    if yas == "exit":
        break

    yas= int(yas)

    if yas <= 2:
        qiymet = 0
    elif 3<= yas <= 12:
        qiymet = 14.90
    elif  yas >=65:
        qiymet = 18.90
    else:
        qiymet =23.90

    total_qiymet += qiymet

print(f"total_qiymet:{total_qiymet:.2f}")








