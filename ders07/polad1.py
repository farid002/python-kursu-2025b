"""
Bir list yaradın, içində n ədəd tam sayı olsun. Döngü (loop) istifadə edərək hər bir ədədi aşağıdakı qaydada dəyişdirin:

    -Əgər ədəd cütdürsə, onu yarıya bölün
    -Əgər ədəd təkdirsə, onu üç qat artırıb üstünə 1 əlavə edin

Original və dəyişdirilmiş listi çap edin
"""
numbers=[1,2,3,4,5,6,7,8,9]
numbers_2=[i/2 if i%2==0 else i*3+1 for i in numbers]
print(numbers)
print(numbers_2)