"""
Qiymətlərin Kateqoriyalaşdırılması (hərf qiyməti)

İstifadəçidən imtahan balını daxil etməsini istəyin.
Qiymətləri kateqoriyalara ayırın:
90-100: “A”
80-89: “B”
70-79: “C”
60-69: “D”
0-59: “F”
"""
toplanan_bal=int(input("balinizi daxil edin"))
if toplanan_bal>90:
    print("A ile kecdiniz")
elif toplanan_bal>80:
    print("B ile kecdiniz")
elif toplanan_bal>70:
    print("C ile kecdiniz")
elif toplanan_bal>60:
    print("D ile kecdiniz")
elif toplanan_bal>50:
    print("F ile kecdiniz")
else:
    print("kesildiniz")
