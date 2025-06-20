"""
10 ədəd integer elementi olan bir list təyin edin.
    - Listin uzunluğunu çap edin
    - Listi böyükdən kiçiyə sıralayın
    - Ən böyük və kiçik ədədi çap edin
"""

new_list = [3,4,2,34,37,3243,9,5,0,70]
print(f"Listin uzunlugu:{len(new_list)}")
new_list.sort()
print(f"Listi böyükdən kiçiyə:{new_list[::-1]}")
print(max(new_list))
print(min(new_list))