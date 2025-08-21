"""
Proqram:

İstifadəçidən fayl adını istəsin.
Faylı açmağa və oxumağa çalışsın.
Fayl mövcud deyilsə, "Fayl tapılmadı!" yazsın.

İpucu: FileNotFoundError istifadə edin.
"""


try:
    a = input("Faylin adini yazin:")
    my_file = open(f"{a}.txt", "r")
except FileNotFoundError as fnfe:
    print("Fayil tapilmadi: ", fnfe)
else:
    print("Ugurlu emeiliyyat!")
