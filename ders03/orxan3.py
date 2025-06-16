"""
Valyuta Çevirici

İstifadəçidən valyutanı seçməsini istəyin (məsələn, USD, EUR, TRY).
Müvafiq məzənnəni göstərərək AZN-ə çevirin (kursları əvvəlcədən təyin edin).

Qeyd:
    1 USD = 1.70 AZN
    1 EUR = 1.95 AZN
    1 TRY = 0.04 AZN
"""
valyuta=input("usd,eur,try")
miqdar=int(input("cevirmek istediyiniz pulun miqdari"))
if valyuta== "usd":
    print(miqdar*1.7)
elif valyuta=="eur":
    print(miqdar*1.95)
elif valyuta=="try":
    print(miqdar*0.04)