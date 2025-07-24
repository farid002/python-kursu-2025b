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
"""
Əlavə:

It classi uchun indiye qeder yediyi sumuk_sayi
It class uchun sumuk_ye(sumuk_sayi) funksiyasi yarat

Pishik classi uchun big
"""

class Heyvan:
    def __init__(self,ad,yas,cins):
        self.ad=ad
        self.yas=yas
        self.cins=cins
    def ses_cixar(self):
        print( "bu heyvan ses cixarir")
class It(Heyvan):
    def __init__(self,ad,yas,cins):
        super().__init__(ad,yas,cins)
        self.yediyi_sumuy_sayi=0
    def ses_cixar(self):
        print( "hav-hav")
    def sumuy_ye(self,sumuy_sayi):
        self.yediyi_sumuy_sayi+=sumuy_sayi
        print(sumuy_sayi)

class Pisiy(Heyvan):
    def __init__(self,ad,yas,cins,big):
        super().__init__(ad,yas,cins)
        self.big=big
    def ses_cixar(self):
        print( "miyov_miyov")
toplan=It("it",2,"erkek")
mesi=Pisiy("pisiy",1,"disi",1)
toplan.ses_cixar()
mesi.ses_cixar()
toplan.sumuy_ye(5)


