"""
10 ədəd integer elementi olan bir list təyin edin.
    - Listin uzunluğunu çap edin
    - Listi böyükdən kiçiyə sıralayın
    - Ən böyük və kiçik ədədi çap edin
"""
int_list=[1,20,3,4544, 4,5,6,7,8,90,0]
print(f"Listin uzunlugu {len(int_list)}")
int_list.sort(reverse=True)
print(int_list)
print(f"En boyuk {max(int_list)},en kiciyi ise {min(int_list)}")