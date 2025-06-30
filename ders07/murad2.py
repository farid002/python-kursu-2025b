"""
İstifadəçidən dörd rəqəmli tam ədəd alan və bu ədədin rəqəmlərinin cəmini hesablayıb göstərən proqram yazın
Əgər 4 rəqəmli olmazsa və ya ədəd olmazsa, doğru yazana qədər daxil etməsini istəyin.

Məsələn, əgər istifadəçi 3141 daxil edərsə, proqram belə göstərməlidir:
3 + 1 + 4 + 1 = 9
"""

while True:
    user_input = input("dord reqemli bir tam eded daxil edin")
    if user_input.isdigit() and len(user_input) == 4:
        digits = [int(d) for d in user_input]
        total = sum(digits)
    print(total)