"""
Tapşırıq:
Sizə tələbə adlarının və onların ballarının olduğu siyahı verilir. Sizdən tələb olunur:

1- enumerate() istifadə edərək: Hər tələbənin adını, balını və siyahıdakı mövqeyini (1-dən başlayaraq) çap edin
- hər tələbə məlumatı 1 sətirdə

2- Siyahı anlayışı (List Comprehension) istifadə edərək: Yalnız 50 və ya daha çox bal toplayan
tələbələrin adlarını və ballarını çap edin.

3- Bütün tələbələrin orta balını hesablayın.

4- Ən çox bal yığan tələbənin adını, balını və list indeksini göstərin (0-dan başlayaraq).
"""

students = ["Ali", "Huseyn", "Oghuz", "Murad", "Zahid", "Farid", "Orxan", "Ahmad"]
notes = [30, 85, 82, 93, 85, 35, 27, 80]

""""""
for index, ad in enumerate(students):
    print(f"{index+1}{ad}:{notes[index]}")
elli_yuxari = [student for index, student in enumerate(students) if notes[index]>50]
print(elli_yuxari)
toplam=sum(notes)
say=len(students)
print(f"orta bal:{toplam/say}")
en_yuksek_bal=max(notes)
en_yuksek_bal_index=notes.index(en_yuksek_bal)
print(f"{students[en_yuksek_bal_index]}:{int(en_yuksek_bal)}")

