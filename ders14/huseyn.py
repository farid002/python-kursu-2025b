"""
Heyvan adlı əsas sinif yaradın (parent class):

ad, yaş, cins (dişi, erkək) atributunu təyin edin.

ses_cixar() adlı metod yaradın və bu metod "Bu heyvan səs çıxarır" mesajını qaytarmalıdır.


İki fərqli törəmə sinif (child classes) yaradın:

İt adlı sinif yaradın və ses_cixar() metodunu “Hav-hav!” qaytaracaq şəkildə yenidən yazın.
Pişik adlı sinif yaradın və ses_cixar() metodunu “Miyov-miyov!” qaytaracaq şəkildə yenidən yazın.

Test edin:
It və Pişik siniflərindən bir neçə obyekt yaradın və onların ses_cixar() metodunu çağıraraq fərqi göstərin.
"""

class Heyvan:
    def __init__(self, ad: str, yash, cins: str):
        self.ad = ad
        self.yash = yash
        self.cins = cins

class It(Heyvan):
    def ses_cixar(self):
        print(f"{self.ad} adli it ses cixardi: Hav-hav!")

    def sumuk_ye(self, sumuk_sayi):
        print(f"{self.ad} adli it {sumuk_sayi} eded sumuk yedi")

class Pisik(Heyvan):
    def ses_cixar(self):
        print(f"{self.ad} adli pisik ses cixardi: Miyov-miyov!")

if __name__ == '__main__':
    toplan = It("toplan", 3, "erkek")
    toplan.ses_cixar()
    toplan.sumuk_ye(5)
    mestan = Pisik("mestan", 2, "dishi")
    mestan.ses_cixar()

