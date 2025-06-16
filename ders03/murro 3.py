"""
Valyuta Çevirici

İstifadəçidən valyutanı seçməsini istəyin (məsələn, USD, EUR, TRY).
Müvafiq məzənnəni göstərərək AZN-ə çevirin (kursları əvvəlcədən təyin edin).

Qeyd:
    1 USD = 1.70 AZN
    1 EUR = 1.95 AZN
    1 TRY = 0.04 AZN
"""

valyuta = input("mezenneni daxil edin")
para = int(input("cevirmek istediyiniz miqdari yazin"))

if valyuta == "dollar":
    print(f"sizin pulunuz {para * 1.7} manatdir")
if valyuta == "euro":
    print(f"sizin pulunuz {para * 1.95} manatdir")
if valyuta == "try":
    print(f"sizin pulunuz {para * 0.04} manatdir")

#bes verilen para miqdari tam eded olmasaydi? meselen menim elimde 1.4 dollar var onu manata cevirmek isteyirem
