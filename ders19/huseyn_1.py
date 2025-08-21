"""
Proqram:

İstifadəçidən fayl adını istəsin.
Faylı açmağa və oxumağa çalışsın.
Fayl mövcud deyilsə, "Fayl tapılmadı!" yazsın.

İpucu: FileNotFoundError istifadə edin.
"""

try:
    file_name = input("Fayl adi yazin: ")
    with open (file_name, "r") as my_file:
        my_data = my_file.readline()

except Exception as e:
    print(e,"Fayl tapılmadı!")