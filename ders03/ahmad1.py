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

score = int(input("Enter your exam score: "))

if score > 100 or score < 0:
    print("Error, Enter your score between 0-100")
elif 100>=score>=90:
    print("Passed exam successfully with A")
elif 89>=score>=80:
    print("Passed exam successfully with B")
elif 79>=score>=70:
    print("Passed exam successfully with C")
elif 69>=score>=60:
    print("Passed exam successfully with D")
else:
    print("You failed exam")
