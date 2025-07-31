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
    def __init__(self, ad, muellif, sehife_sayisi):
        self.__ad = ad
        self.__muellif = muellif
        self.__sehife_sayisi = sehife_sayisi

    def get_kitab_məlumatı(self):
        return self.__ad, self.__muellif, self.__sehife_sayisi

    def set_səhifə_sayıni_dəyiş(self, yeni_sayı: int):
        if yeni_sayı > 0:
            self.__sehife_sayisi = yeni_sayı
            return self.__sehife_sayisi
        else:
            print("Yeni sayini yeniden yazin")
            return None

if __name__ == '__main__':
    kitab = Kitab("1984", "George Orwell", 328)
    print(kitab.get_kitab_məlumatı())

    kitab.set_səhifə_sayıni_dəyiş(-50)

    kitab.set_səhifə_sayıni_dəyiş(400)

    print(kitab.get_kitab_məlumatı())



