"""
OOP nin 4 əsas prinsipi:

1. Irsilik (inheritance) – Mövcud sinifin xüsusiyyətlərini və metodlarını yeni sinfə ötürmək.
2. Polimorfizm
3. Enkapsulasiya
4. Absktraksiya
"""
class Canli:
    def __init__(self, yash, boy, cheki):
        self.yash = yash
        self.boy = boy
        self.cheki = cheki

    def nefes_al(self):
        print("Nefes aldi")

    def yashlan(self, yash):
        self.yash += yash

class Heyvan(Canli):
    def __init__(self, yash, boy, cheki, nov):
        super().__init__(yash, boy, cheki)
        self.nov = nov
    def ses_chixar(self, nov):
        if nov == "keci":
            print("meee")
        elif nov == "maaa":
            print("maaa")
        elif nov == "it":
            print("havvv")

class Qush(Heyvan):
    def ses_chixar(self):
        print("chik chik")

my_animal = Heyvan(5,50,25,"keci")
my_animal.ses_chixar("keci")
my_animal.yashlan(5)
my_animal.nefes_al()
print(my_animal.yash)

my_canli = Canli(2500, 0.001, 0.001)

print("----")

my_qush = Qush(2,20,2,"qartal")
my_qush.ses_chixar()
print("----")

"""
inheritance (irsilik)

Parent - child
"""


"""
funksiya overwrite
"""



"""
super() funksiyasi

super() funksiyası parent sinfin metodlarını child sinifdə istifadə etməyə imkan yaradır.
mes.: super().__init__()
"""



"""
İrsiliyin Üstünlükləri
 - Kodun təkrar istifadəsinin qarşısını alır.
 - Miras alınan funksiyalari deyishiklik etmeden istifade ede bilirik
 - Siniflər arasında əlaqəni daha səmərəli idarə etməyə kömək edir.
"""
