"""
İstifadəçidən dörd rəqəmli tam ədəd alan və bu ədədin rəqəmlərinin cəmini hesablayıb göstərən proqram yazın
Əgər 4 rəqəmli olmazsa və ya ədəd olmazsa, doğru yazana qədər daxil etməsini istəyin.

Məsələn, əgər istifadəçi 3141 daxil edərsə, proqram belə göstərməlidir:
3 + 1 + 4 + 1 = 9
"""
while True:
    my_number = input("Dörd rəqəmli tam ədəd yazın:")
    if len(my_number) == 4 and my_number.isdigit():
        break
    print("Ədəd 4 rəqəmli olmalıdır")
my_list = list(my_number)
print(my_list)
cem = sum([int(i) for i in my_list])
a = 0
cem = 0
while a < len(my_list):
    a += 1
    cem = cem + int(my_list[a-1])
    print(cem)