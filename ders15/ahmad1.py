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
    def __init__(self,ad,muellif,sehifesayi):
        self.__ad = ad
        self.__muellif = muellif
        self.__sehifesayi = sehifesayi

    def kitab_melumati(self):
        return self.__ad, self.__muellif, self.__sehifesayi
    def səhifə_sayıni_dəyiş(self,reqem):
        if reqem <= 0:
            print("ERROR!!!")
        else:
            self.__sehifesayi=reqem

if __name__=="__main__":
    kitab = Kitab("1984", "George Orwell", 328)
    kitab.səhifə_sayıni_dəyiş(-50)
    kitab.səhifə_sayıni_dəyiş(400)
    kitab_info = kitab.kitab_melumati()
    print(f"Kitab:{kitab_info[0]},Yazici:{kitab_info[1]},Sehife sayi:{kitab_info[2]}")