"""
Istifadəçidən 0 la 100 arasında tam ədəd daxil etməsini istəyin.

Alınan dəyərə qədər olan bütün 3-ə, 5-ə, 3-ə və 5-ə tam bölünən ədədləri ayrı ayrı göstərin. Yəni əvvəlcə
3ə bölünən, sonra 5ə, sonra hər ikisinə bölünən ədədlər.

Təqribi çıxış belə olmalıdır:
0-100 arasında:
    3-ə bölünən ədədlər: 3, 6, 9, 12 ...
    5-ə bölünən ədədlər: 5, 10, 15, 20, 25 ...
    3-ə və 5-ə bölünən ədədlər: 15, 30, 45 ...
"""
user_number=int(input("0-dan 100-e qeder reqem daxil edin"))
a_3=[]
a_5=[]
a_3_5=[]
for i in range(user_number):
    if i%3==0:
        a_3.append(i)
    if i%5==0:
        a_5.append(i)
    if i%5==0 and i%3==0:
        a_3_5.append(i)
print(f"3-ə bölünən ədədlər: {a_3}\n5-ə bölünən ədədlər: {a_5}\n3-ə və 5-ə bölünən ədədlər: {a_3_5}\n")