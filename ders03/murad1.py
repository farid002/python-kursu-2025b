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

bal = int(input("kecdiyin bali daxil edin"))
if bal<0 or bal>100:
    print("duzgun daxil edin balinizi")
if bal >= 90:
    print("sizin herf notunuz A dir")
elif bal >= 80:
    print("sizin herf notunuz B dir")
elif bal >= 70:
    print("sizin herf notunuz C dir")
elif bal >= 60:
    print("sizin herf notunuz D dir")
else:
    print("kesildiniz")


