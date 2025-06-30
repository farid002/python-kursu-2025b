"""
Bir list yaradın, içində n ədəd tam sayı olsun. Döngü (loop) istifadə edərək hər bir ədədi aşağıdakı qaydada dəyişdirin:

    -Əgər ədəd cütdürsə, onu yarıya bölün
    -Əgər ədəd təkdirsə, onu üç qat artırıb üstünə 1 əlavə edin

Original və dəyişdirilmiş listi çap edin
"""

my_list = [1, 2, 3, 4, 5, 25, 46, -58, 96, -525, 0, 4]
new_list = []
for number in my_list:
    if number == 0:
        number = None
        new_list.append(number)
    else:
        if number % 2 == 0:
            number = int(number) / 2
            new_list.append(number)
        else:
            number = (int(number) * 3) + 1
            new_list.append(number)
print(new_list)

#List Comprehension
# new_list = [int(number) / 2 if number == 0 None else (if number % 2 == 0 else (number * 3) + 1)  for number in my_list]

new_list = [None if number == 0 else int(number) / 2 if number % 2 == 0 else (int(number) * 3) + 1 for number in my_list]
print(new_list)