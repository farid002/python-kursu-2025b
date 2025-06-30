"""
Bir list yaradın, içində n ədəd tam sayı olsun. Döngü (loop) istifadə edərək hər bir ədədi aşağıdakı qaydada dəyişdirin:

    -Əgər ədəd cütdürsə, onu yarıya bölün
    -Əgər ədəd təkdirsə, onu üç qat artırıb üstünə 1 əlavə edin

Original və dəyişdirilmiş listi çap edin
"""
numbers = [12,4,9,13,8,7]
deyisdirilmis_siyahi=[]
for num in numbers:
    if num % 2 == 0:
        deyisdirilmis_siyahi.append(num/2)
    else:
        deyisdirilmis_siyahi.append(num*3 +1)
print(numbers)
print(deyisdirilmis_siyahi)

deyisdirilmis_siyahi = [num/2 if num % 2 == 0 else num *3 + 1 for num in numbers]
