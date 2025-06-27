
students = ["Ali", "Huseyn", "Oghuz", "Murad", "Zahid", "Farid", "Orxan", "Ahmad"]
notes = [30, 85, 82, 93, 85, 35, 27, 80]
mix_list=[]
for i in enumerate(students):
    mix_list.append(f"Adi :{i[1]}")
    for b in enumerate(notes):
        if i[0]==b[0]:
            mix_list.append(f"Qiymeti :{b[1]}")
            mix_list.append(f"Sirasi :{notes.index(b[1])+1}")
print(mix_list)
_50_plus_list=[students[index] for index ,note in enumerate(notes) if note>=50]
print(f"50-den cox yiganlar{_50_plus_list}")
sum=0
a=0
for c in notes:
    sum=sum+c
    a+=1
print(f"Sinif ortalamasi {sum//a}")
best_note=0
for c in notes:
    if c==max(notes):
        best_note=c
best_note_index=notes.index(best_note)
best_note_name=students[best_note_index]
print(f"En cox bal yigan sagirdin adi-{best_note_name} qiymeti-{best_note} indexi-{best_note_index}")
