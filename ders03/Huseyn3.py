"""
Valyuta Çevirici

İstifadəçidən valyutanı seçməsini istəyin (məsələn, USD, EUR, TRY).
Müvafiq məzənnəni göstərərək AZN-ə çevirin (kursları əvvəlcədən təyin edin).

Qeyd:
    1 USD = 1.70 AZN
    1 EUR = 1.95 AZN
    1 TRY = 0.04 AZN
"""
mebleg = float(input("Mebleg yazin:"))
mezenne = input("Valyuta secin:")

# Dollar Kursu
dollar = 1.7
# Euro Kursu
euro = 1.95
# Try Kursu
tl = 0.04
if mezenne != "USD" or mezenne != "EUR" or mezenne != "TRY":
    print("Valyutani duzgun secin")
elif mezenne == "USD":
    azn = mebleg * dollar
    print(f"Sizin balansiniz {azn}AZN-dir")
elif mezenne == "EUR":
    azn = mebleg * euro
    print(f"Sizin balansiniz {azn}AZN-dir")
elif mezenne == "TRY":
    azn = mebleg * tl
    print(f"Sizin balansiniz {azn}AZN-dir")