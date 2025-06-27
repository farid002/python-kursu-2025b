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

baby_price_list = []
child_price_list = []
old_price_list = []
normal_price_list = []
while True:
    age = input("Yaslari daxil edin")
    if age == "exit" or age == " ":
        break
    age = int(age)

    if age <= 2:
        baby_price = 0
        baby_price_list.append(baby_price)
    if 3 <= age <= 12:
        child_price = 14.90
        child_price_list.append(child_price)
    if age > 65:
        old_price = 18.90
        baby_price_list.append(old_price)
    else:
        normal_price = 23.90
        normal_price_list.append(normal_price)
a=float(sum(baby_price_list))
b=float(sum(child_price_list))
c=float(sum(old_price_list))
d=float(sum(normal_price_list))
print(f"odemeli oldugunuz mebleg{sum([a, b, c, d])}")