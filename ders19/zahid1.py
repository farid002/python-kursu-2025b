"""
Proqram:

İstifadəçidən fayl adını istəsin.
Faylı açmağa və oxumağa çalışsın.
Fayl mövcud deyilsə, "Fayl tapılmadı!" yazsın.

İpucu: FileNotFoundError istifadə edin.
"""
a=input("Fayl adi yazin")
try:
    with open(a,"r"):
        print("Fayl tapildi")
except FileNotFoundError as f:
    print("Fayl tapilmadi")