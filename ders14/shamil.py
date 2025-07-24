"""
Heyvan adlı əsas sinif yaradın (parent class):

ad, yaş, cins (dişi, erkək) atributunu təyin edin.

ses_cixar() adlı metod yaradın və bu metod "Bu heyvan səs çıxarır" mesajını qaytarmalıdır.


İki fərqli törəmə sinif (child classes) yaradın:

İt adlı sinif yaradın və ses_cixar() metodunu “Hav-hav!” qaytaracaq şəkildə yenidən yazın.
Pişik adlı sinif yaradın və ses_cixar() metodunu “Miyov-miyov!” qaytaracaq şəkildə yenidən yazın.

It classi uchun indiye qeder yediyi sumuk_sayi
It class uchun sumuk_ye(sumuk_sayi) funksiyasi yarat
"""
class Heyvan:
    def __init__(self, ad, yas, cins):
        self.ad = ad
        self.yas = yas
        self.cins = cins

    def ses_cixar(self):
        print( "Bu heyvan səs çıxarır" )

class It(Heyvan):
    def __init__(self, ad, yas, cins,yediyi_sumuk_sayi):
     super().__init__(ad, yas, cins)
     self.yediyi_sumuk_sayi=yediyi_sumuk_sayi

    def ses_cixar(self):
        print("Hav-hav!🐶")
    def sumuk_ye(self, sumuk_sayi=5):
        self.yediyi_sumuk_sayi += sumuk_sayi

class Pisik(Heyvan):
    def __init__(self, ad, yas, cins,big_uzunlugu):
        super().__init__(ad, yas, cins)
        self.big_uzunlugu=big_uzunlugu

    def ses_cixar(self):
        print("Miyov-miyov!😺")
it = It("Toplan", 3, "erkək")
pisik = Pisik("Mestan", 2, "dişi")

print(f"{it.ad} səs çıxarır: {it.ses_cixar()}")
print(f"{pisik.ad} səs çıxarır: {pisik.ses_cixar()}")


