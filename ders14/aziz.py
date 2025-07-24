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
    def __init__(self,ad,yas,cins):
        self.ad = ad
        self.yas = yas
        self.cins = cins
    def ses_cixar(self):
        print("Bu hevan ses cixarir")
class It(Heyvan):
    def __init__(self,ad,yas,cins,yediyi_sumuk_sayi):
        super().__init__(ad , yas , cins )
        self.yediyi_sumuk_sayi = yediyi_sumuk_sayi
    def ses_cixar(self):
        print("HAW 🐶 HAWWWWW")
    def sumuk_ye(self,sumuk_sayi):
        self.yediyi_sumuk_sayi += sumuk_sayi
        print("Itin umumi yediyi sumuk sayisi",self.yediyi_sumuk_sayi)
class Pisik(Heyvan):
    def __init__(self,ad,yas,cins):
        super().__init__(ad , yas , cins )
    def ses_cixar(self):
        print("MEOWWW 😺")
if __name__=="__main__":
    it=It("Rex",4,"Ekrek",15)
    pisik=Pisik("Mestan",3,"Disi")
    it.ses_cixar()
    pisik.ses_cixar()
    it.sumuk_ye(4)


