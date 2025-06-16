"""
Valyuta Çevirici

İstifadəçidən valyutanı seçməsini istəyin (məsələn, USD, EUR, TRY).
Müvafiq məzənnəni göstərərək AZN-ə çevirin (kursları əvvəlcədən təyin edin).

Qeyd:
    1 USD = 1.70 AZN
    1 EUR = 1.95 AZN
    1 TRY = 0.04 AZN
"""
""" METOD 1
valyuta=int(input("Usd üçün 1 yazın \n Eur üçün 2 yazın \n Try üçün 3 yazın \n"))
pul=int(input("Çevirmək istədiyiniz miqdarı yazın"))
if valyuta==1:
    print(f"{pul*1.7} AZN")
elif valyuta==2:
    print(f"{pul*1.95} AZN")
elif valyuta==3:
    print(f"{pul*0.04} AZN")
"""

# METOD 2
pul_ve_valyuta=input("Usd,Eur ve ya Try-den birini secin").split()
pul = int(pul_ve_valyuta[0])
valyuta = pul_ve_valyuta[1]
# pul=float(input("Çevirmək istədiyiniz miqdarı yazın"))
if valyuta.lower()=="usd":
    print(f"{pul * 1.7} AZN")
elif valyuta.lower()=="eur":
    print(f"{pul*1.95} AZN")
elif valyuta.lower()=="try":
    print(f"{pul*0.04} AZN")

