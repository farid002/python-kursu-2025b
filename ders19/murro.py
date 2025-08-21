"""
Proqram:

İstifadəçidən fayl adını istəsin.
Faylı açmağa və oxumağa çalışsın.
Fayl mövcud deyilsə, "Fayl tapılmadı!" yazsın.

İpucu: FileNotFoundError istifadə edin.
"""
fayladi= input("faylin adini elave et:")
try:
    with open(fayladi,"r") as file:
        mezmun=file.read()
        print(mezmun)


except FileNotFoundError:
    print("fayl tapilmadi")
