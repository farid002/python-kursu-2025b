"""
Bir list yaradın, içində n ədəd tam sayı olsun. Döngü (loop) istifadə edərək hər bir ədədi aşağıdakı qaydada dəyişdirin:

    -Əgər ədəd cütdürsə, onu yarıya bölün
    -Əgər ədəd təkdirsə, onu üç qat artırıb üstünə 1 əlavə edin

Original və dəyişdirilmiş listi çap edin
"""
n=[2,4,5,6,7,8,9]
for i in n:
    if i%2==0:
        print(int(i/2))
    else:
        print(int(i*3+1))
""""""""
new_list=[int(x/2 )if x%2==0 else x*3+1 for x in n]
print(new_list)


