students = ["Ali", "Huseyn", "Oghuz", "Murad", "Zahid", "Farid", "Orxan", "Ahmad"]
notes = [30, 85, 82, 93, 85, 35, 27, 80]
for index, ad in enumerate(students):
    print(f"{index+1} {ad}: {notes[index]}")
print([f"{students[indexx]}: {notes[indexx]}" for indexx, bal in enumerate(notes) if bal >= 50])
print(f"Bütün tələbələrin orta balı: {sum(notes) / len(notes)}")
print(f"Ən çox bal yığan tələbə: {students[notes.index(max(notes))]},{max(notes)} bal")
