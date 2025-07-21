"""
  BankHesabi adlı bir sinif yaradın. Bu sinifdə müştərinin adı, email adresi, hesab nömrəsi və balansı saxlanmalıdır. Hesaba pul yatırmaq, çıxarmaq və balans yoxlamaq üçün metodlar yaradın.

  Tapşırıq:

   - BankHesabi sinifini yaradın və ad, email adresi, hesab_nomresi, balans atributlarını əlavə edin.
   - pul_yatir metodunu yaradın ki, müştəri hesabına müəyyən bir məbləğ yatırsın və balans artsın.
   - pul_cixar metodunu yaradın ki, müştəri hesabından müəyyən bir məbləğ çıxarsın və balans azalsın.
   - balans_goster metodunu yaradın ki, müştərinin cari balansını ekrana çap etsin.
   - tam_melumat metodu yaradın ki, müştərinin bütün məlumatlarını ekrana çap etsin
"""
class BankHesabi :
    def __init__(self, ad, email, hesab_nomresi, balans):
        self.ad = ad
        self.email = email
        self.hesab_nomresi = hesab_nomresi
        self.balans = balans

    def pul_yatir(self, mebleg):
        self.balans += mebleg
        print("Sizin cari balansınız", self.balans)

    def pul_cixar(self, mebleg):
        self.balans -= mebleg
        print("Sizin cari balansınız", self.balans)

    def balans_goster(self):
        print("Sizin cari balansınız", self.balans)

    def tam_melumat(self):
        print(f"Sizin adınız: {self.ad} \nEmail adresiniz: {self.email} \nHesab nömrəniz {self.hesab_nomresi} \nBalansınız {self.balans}")

if __name__ == '__main__':
    huseynin_balansi = BankHesabi("Huseyn", "huseyn@", "0101", 1000)

    mebleg = int(input("Məbləğ əlavə edin: "))

    huseynin_balansi.pul_yatir(mebleg)





