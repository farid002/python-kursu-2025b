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
qiymet=int(input("Neticenizi yazin"))
if qiymet>100 or qiymet<0:
    print("Yazdiginiz netice sehfdir.")
if 90 <= qiymet <= 100:
    print("A")
elif 80 <= qiymet <= 89:
        print("B")
elif 70 <= qiymet <= 79:
        print("C")
elif 60 <= qiymet <= 69:
        print("D")
else:
        print("F")