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

bal = int(input("Imtahan balınızi daxil edin:"))
if bal < 0 or bal > 100:
    print("Balinizi duzgun daxil edin")
elif bal > 89:
    print("A ile kecdiniz")
elif bal > 79:
    print("B ile kecdiniz")
elif bal > 69:
    print("C ile kecdiniz")
elif bal > 59:
    print("D ile kecdiniz")
else:
    print("F kesildiniz")
