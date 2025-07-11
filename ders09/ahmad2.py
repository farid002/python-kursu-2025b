"""
Bəzi köhnə sadə mobil telefonlarda mətn mesajları rəqəmli klaviaturadan istifadə edilərək göndərilir.
Hər düyməyə bir neçə hərf uyğun gəldiyi üçün əksər hərfləri yazmaq üçün düyməyə bir neçə dəfə basmaq lazımdır.
Bir rəqəmə bir dəfə basmaq həmin düymədəki ilk hərfi yaradır.
Rəqəmə 2, 3, 4 və ya 5 dəfə basmaqla həmin düymədə olan ikinci, üçüncü, dördüncü və ya beşinci simvol daxil edilir.

Düymə Simvolları
1 .,?!:
2 A B C
3 D E F
4 G H I
5 J K L
6 M N O
7 P Q R S
8 T U V
9 W X Y Z
0 boşluq

İstifadəçidən oxunan mətn mesajını daxil etmək üçün tələb olunan düymə sırasını göstərən bir proqram yazın.
Hər hərfi və ya simvolu müvafiq düymə sırasına uyğunlaşdıran bir lüğət yaradın.

Sonra bu lüğətdən istifadə edərək istifadəçinin mesajını daxil etmək üçün tələb olunan düymələri yaradın və göstərin.

Məsələn, əgər istifadəçi "Hello, World!" daxil edərsə, proqram aşağıdakı nəticəni qaytarmalıdır:

44 33 555 555 666 11 0 9 666 777 555 3 1111

Proqram həm böyük, həm də kiçik hərfləri dəstəkləməlidir.
Cədvəldə göstərilməyən simvolları (məsələn, _, (, |) nəzərə almayın.
"""

word = input("Bir soz yazin: ").upper()

my_dict = {
    1:".,?!:",
    2:"ABC",
    3:"DEF",
    4:"GHI",
    5:"JKL",
    6:"MNO",
    7:"PQRS",
    8:"TUV",
    9:"WXYZ",
    0:" "
}
netice = ""

"""
ALI
2 555 444   
"""
for char in word:
    for key,value in my_dict.items():
        if char in value:
            netice += (str(key) * (value.index(char) + 1))
            netice += " "

print(netice)
