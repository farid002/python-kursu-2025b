"""
İstifadəçidən adını alın.

- Adın bütün hərflərini əksinə düzülmüş şəkildə çap edin. ([::-1] slicing istifadə edin)
- Adın içində neçə dəfə "a" hərfi keçdiyini tapın.
- Adı ilk hərfi böyük formatında (title()) çap edin.
"""
user_name=input("Adiniz: ")
print(f"Adinizin eksine duzulmus formasi: {user_name[::-1]}.\n Adinizin icinde {user_name.count("a")} defe a islenib. \n Adinizin ilk herfi boyuk olan formasi- {user_name.title()}")

