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


user_number = int(input("Enter a number 0-100: "))
uce_bolunenler=[]
bes = []
her_ikisi = []
for number in range(1,user_number):
    if number % 3 == 0:
        uce_bolunenler.append(number)
    if number % 5 == 0:
        bes.append(number)
    if number % 3 == 0 and number % 5 == 0:
        her_ikisi.append(number)

print(f"5-ə bölünən ədədlər:{bes}")
print(f"3-ə və 5-ə bölünən ədədlər:{her_ikisi}")

