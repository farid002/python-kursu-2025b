"""
Proqram:

İstifadəçidən fayl adını istəsin.
Faylı açmağa və oxumağa çalışsın.
Fayl mövcud deyilsə, "Fayl tapılmadı!" yazsın.

İpucu: FileNotFoundError istifadə edin.
"""
fayl_name=input("fayl adi:")
try :
    file= open(fayl_name,"r")
    print(file.readline())

except Exception as FileNotFoundError:
    print("fayl not found")