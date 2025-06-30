"""
İstifadəçidən dörd rəqəmli tam ədəd alan və bu ədədin rəqəmlərinin cəmini hesablayıb göstərən proqram yazın
Əgər 4 rəqəmli olmazsa və ya ədəd olmazsa, doğru yazana qədər daxil etməsini istəyin.

Məsələn, əgər istifadəçi 3141 daxil edərsə, proqram belə göstərməlidir:
3 + 1 + 4 + 1 = 9
"""

while True:
    n = int(input("4 reqemli eded yazin"))
    if n<1000 or n>9999:
        print("dogru yaz")
    else:
        break
cem=0
for reqem in str(n):
    cem+=int(reqem)
print(f"reqemlerin cemi:{cem}")