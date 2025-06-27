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


umumi_qiymet = 0
while True:
    age = input("Enter your age:")
    age = int(age)
    if age == " ":
        break
    if age <=2:
        umumi_qiymet +=0
    if 3<=age<=12:
        umumi_qiymet+=14.90
    if age>=65:
        umumi_qiymet+=18.90
    else:
        umumi_qiymet+=23.90



print(f"umumi qiymet:{umumi_qiymet:.2f}")