"""
  BankHesabi adlı bir sinif yaradın. Bu sinifdə müştərinin adı, email adresi, hesab nömrəsi və
  balansı saxlanmalıdır.
  Hesaba pul yatırmaq, çıxarmaq və balans yoxlamaq üçün metodlar yaradın.

  Tapşırıq:

   - BankHesabi sinifini yaradın və ad, email adresi, hesab_nomresi, balans atributlarını əlavə edin.
   - pul_yatir metodunu yaradın ki, müştəri hesabına müəyyən bir məbləğ yatırsın və balans artsın.
   - pul_cixar metodunu yaradın ki, müştəri hesabından müəyyən bir məbləğ çıxarsın və balans azalsın.
   - balans_goster metodunu yaradın ki, müştərinin cari balansını ekrana çap etsin.
   - tam_melumat metodu yaradın ki, müştərinin bütün məlumatlarını ekrana çap etsin
"""
class BankHesabi:
    def __init__(self,ad,email_adress,hesap_nomresi,balans):
        self.ad=ad
        self.email_adress=email_adress
        self.hesap_nomresi=hesap_nomresi
        self.balans=balans
    def pul_yatir(self,yatirilacaq_pul=0):
        self.balans+=yatirilacaq_pul
    def pul_cixar(self,cixarilacaq_pul=0):
        self.balans-=cixarilacaq_pul
    def balans_goster(self):
        print("Balans:  ",self.balans)
        return self.balans
    def tam_muelumat(self):
        print({
            "ad":self.ad,
            "email_adress":self.email_adress,
            "hesap_nomresi":self.hesap_nomresi,
            "balans":self.balans
        })                                    #metod 1
        print(f"""      
Ad                {self.ad}
Email             {self.email_adress}
Hesap Nomresi     {self.hesap_nomresi}
Balans            {self.balans} \n""")      #metod 2
        return {
            "ad":self.ad,
            "email_adress":self.email_adress,
            "hesap_nomresi":self.hesap_nomresi,
            "balans":self.balans
        }
if __name__=="__main__":
    zahid_hesabi = BankHesabi("zahid","asd@gmail.com","123123123", 1000000)
    zahid_hesabi.pul_cixar(int(input("Yatirmaq istediyiniz miqdar")))
    zahid_hesabi.tam_muelumat()
    zahid_hesabi.pul_yatir(int(input("Cixarmaq istediyiniz miqdar")))
    zahid_hesabi.balans_goster()
