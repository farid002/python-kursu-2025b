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
    def __init__(self, ad, yash,cins):
        self.ad = ad
        self.yash = yash
        self.cins = cins


    def ses_chixar(self):
        print("heyvan seslenir")

class It(Heyvan):
    def __init__(self, ad,yash,cins, novu):
        super().__init__(ad,yash,cins)
        self.novu=novu

    def ses_cixarir(self):
        print("hav hav")

    def sumuk_ye(self):
        print("nam nam ne dadlidir")

    def sumuk_sayi(self, ay):
        self.sumuk_sayi += (ay *30 )
        print(self.sumuk_sayi)


class Pisik(Heyvan):
    def __init__(self,ad,yash,cins,rengi,uzunlugu):
        super().__init__(ad,yash,cins)
        self.rengi=rengi
        self.uzunlugu=uzunlugu


    def ses_cixarir(self):
        print("miyav miyav")


toplan=It("asbas",3,"erkek","toy poodle")
sosan=Pisik("mistik",1,"disi","gri")
toplan.sumuk_sayi(3)
toplan.ses_cixarir()
sosan.ses_chixar()
