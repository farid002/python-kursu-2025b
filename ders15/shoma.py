"""
Kitabxana Sistemi
Tələblər:

 - Kitab adlı bir sinif yaradın.

Sinifdə aşağıdakı private (__) atributlar olmalıdır:
    __ad – Kitabın adı.
    __müəllif – Kitabın müəllifi.
    __səhifə_sayı – Kitabın səhifə sayı.

Aşağıdakı metodları yazın:
    __init__(self, ad, müəllif, səhifə_sayı) – Kitabın atributlarını təyin etsin.
    kitab_məlumatı(self) – Kitabın adını, müəllifini və səhifə sayını qaytarsın.
    səhifə_sayıni_dəyiş(self, yeni_sayı) – Yeni səhifə sayı təyin etsin, amma əgər səhifə sayı 0 və ya mənfidirsə, dəyişməsin və xəbərdarlıq versin.

Private atributlara birbaşa giriş olmasın!

Həmin class bu cür işlədilib comment hissəsindəki kimi output alacaq şəkildə yazılmalıdır.

kitab = Kitab("1984", "George Orwell", 328)
print(kitab.kitab_məlumatı())  # Kitab: 1984, Müəllif: George Orwell, Səhifələr: 328
kitab.səhifə_sayıni_dəyiş(-50)  # Səhifə sayı 0 və ya mənfi ola bilməz!
kitab.səhifə_sayıni_dəyiş(400)
print(kitab.kitab_məlumatı())  # Kitab: 1984, Müəllif: George Orwell, Səhifələr: 400

"""

class Kitab:

    def __init__(self,ad, mellif,sehfe_sayi ):
        self.__ad = ad
        self.__mellif = mellif
        self.__sehfe_sayi = sehfe_sayi

    def kitab_inf(self):
        return f"book:{self.__ad},author:{self.__mellif},pages:{self.__sehfe_sayi}"

    def page_num_deyis(self,new_page_num):
        if new_page_num <=0:
            print("eleme 0nuu")
        else:
            self.__sehfe_sayi = new_page_num

    def add_pages(self,extra_pages):
        if extra_pages <=0:
            print("eleme onuu")
        else:
            self.__sehfe_sayi +=extra_pages

    def get_ad(self):
        return self.__ad

    def get_mellif(self):
        return self.__mellif

    def get_page_nums(self):
        return self.__sehfe_sayi

if __name__=="__main__":
    kitab = Kitab("1984", "George Orwell", 328)
    print(kitab.kitab_inf())  # Kitab: 1984, Müəllif: George Orwell, Səhifələr: 328
    kitab.page_num_deyis(-50)  # Səhifə sayı 0 və ya mənfi ola bilməz!
    kitab.page_num_deyis(400)
    print(kitab.kitab_inf())  # Kitab: 1984, Müəllif: George Orwell, Səhifələr: 400
