number = int(input("0 la 100 arasında tam ədəd daxil et:"))
uce_bolunen = []
bese_bolunen = []
uce_bese_bolunen = []

for element in range(1, number):
    if element % 3 == 0:
        uce_bolunen.append(element)
    if element % 5 == 0:
        bese_bolunen.append(element)
    if element % 5 == 0 and element % 3 == 0:
        uce_bese_bolunen.append(element)

print("3-e bolunen ededler", uce_bolunen)
print("5-e bolunen ededler", bese_bolunen)
print("3-ə və 5-ə bölünən ədədlər", uce_bese_bolunen)