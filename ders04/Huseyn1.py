"""
10 ədəd integer elementi olan bir list təyin edin.
    - Listin uzunluğunu çap edin
    - Listi böyükdən kiçiyə sıralayın
    - Ən böyük və kiçik ədədi çap edin
"""

my_list = list(range(5,100,5))
print(len(my_list))
my_list.sort()
print(my_list[::-1])
print(max(my_list))
print(min(my_list))