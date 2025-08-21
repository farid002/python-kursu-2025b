"""
Proqram:

İstifadəçidən fayl adını istəsin.
Faylı açmağa və oxumağa çalışsın.
Fayl mövcud deyilsə, "Fayl tapılmadı!" yazsın.

İpucu: FileNotFoundError istifadə edin.
"""
try:
    ad=input("fayl adi daxil edin")
    my_file=open(ad,"r")
except FileNotFoundError:
    print("fayl tapilmadi")
else:
    print("tapildi")
