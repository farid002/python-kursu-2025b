"""
----------------------------------------WHILE DÖNGÜSÜ----------------------------------------

i = 10

while i > 2:
    i = i - 1
    print("Hi")

print("End")
"""
# i = 15
# while i > 10:
    # i = i - 1
    # print(f"{i}-YES")


"""
----------------------------------------break, continue, pass----------------------------------------
"""

a = 100
while True:
    if a == 90:
        a = a - 1
        continue
    print(a)
    if a == 50:
        break
    a = a - 1


"""
----------------------------------------DÖNGÜLƏRDƏ ELSE---------------------------------------

Tək qayda: Loop icində break etdisə (break sətirinə çatdı və işlətdisə), kod else'ə daxil olmayacaq. 
Əks halda, (break kodda yazılmasına baxmayaraq break'i işlətmədisə) else'ə girəcək

BREAK --> NO ELSE
NO BREAK --> ELSE
"""
i = 10
istenilen_eded = 11

while i < 15:
    print(i)
    if i == istenilen_eded:
        print("istenilen eded tapildi")
        break
    i+=1

"""f-stringdə onluq hissənin sayı"""

value = 10.5732134
print(f"{value:.1f}")
