"""
Valyuta Çevirici

İstifadəçidən valyutanı seçməsini istəyin (məsələn, USD, EUR, TRY).
Müvafiq məzənnəni göstərərək AZN-ə çevirin (kursları əvvəlcədən təyin edin).

Qeyd:
    1 USD = 1.70 AZN
    1 EUR = 1.95 AZN
    1 TRY = 0.04 AZN
"""
valyuta = input("Valyutani secin (usd,eur,try): ")
pul = float(input("Ne qeder pulunuz var: "))

if valyuta == "usd":
    print(f"bu qeder pulunuz var: {pul*1.70}manat")
elif valyuta == "eur":
    print(f"bu qeder pulunuz var: {pul*1.95}manat")
elif valyuta == "try":
    print(f"bu qeder pulunuz var: {pul*0.04}manat")