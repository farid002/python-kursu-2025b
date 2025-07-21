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
    def __init__(self, ad , email , hesab_nomresi , balans=0):
        self.ad=ad
        self.email=email
        self.hesab_nomresi=hesab_nomresi
        self.balans=balans

    def pul_yatir(self, mebleg):
        if mebleg > 0:
            self.balans += mebleg
            print(f"{mebleg} AZN hesabınıza yatırıldı. Yeni balans: {self.balans} AZN")
        else:
            print("Yatırılan məbləğ müsbət olmalıdır.")

    def pul_cixar(self,mebleg):
        if mebleg <= 0:
            print("Çıxarılan məbləğ müsbət olmalıdır.")
        elif mebleg > self.balans:
            print("Balansda kifayət qədər vəsait yoxdur.")
        else:
            self.balans -= mebleg
            print(f"{mebleg} AZN hesabdan çıxarıldı. Yeni balans: {self.balans} AZN")

    def balans_goster(self):
        print(f"Cari balans: {self.balans} AZN")

    def tam_melemat(self):
        print("musteri melematlari:")
        print(f"ad:{self.ad}")
        print(f"email:{self.email}")
        print(f"hesab nomresi: {self.hesab_nomresi}")
        print(f"balans:{self.balans} AZN")

shamilin_hesabi=BankHesabi( "Shamil", "sads" ,123456,678)
print(shamilin_hesabi.tam_melemat())
