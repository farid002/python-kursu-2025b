class Isci:
    def __init__(self,ad,emek_haqqi):
        self.__ad=ad
        self.__emek_haqqi=emek_haqqi
    def melumat_goster(self):
        return self.__ad, self.__emek_haqqi
    def maas_artir(self,faiz):
        self.__emek_haqqi+=self.__emek_haqqi*faiz/100
    def status(self):
        return "umumi isci"
class Mudir(Isci):
    def __init__(self,ad, emek_haqqi, department):
        super().__init__(ad,emek_haqqi)
        self.__department=department
    def status(self):
      return "Müdir – şöbə: {departament}"
    def department_deyis(self,yeni_ad):
       self.__department=yeni_ad
class Muhendis(Isci):
    def __init__(self,ad,emek_haqqi,ixtisas):
        super().__init__(ad,emek_haqqi)
        self.__ixtisas=ixtisas
        self.__sertifaktlar=[]
    def status(self):
        return "Mühəndis – ixtisas: {ixtisas}"
    def sertifakt_elave_et(self,sertifakt):
        self.__sertifaktlar.append(sertifakt)
    def sertifaklar(self):
        return self.__sertifaktlar
class Praktikant(Isci):
    def __init__(self,ad,emek_haqqi=0):
        super().__init__(ad,0)
    def status(self):
        return "Praktikant – təcrübə dövründədir"
    def maas_artir(self,faiz):
        pass

def statuslari_yoxla(self,isci_siyahisi):
    for isci in isci_siyahisi:
        print(isci.status())
if __name__=="__main__":
    mudir = Mudir("Aygün", 5000, "IT")
    muhendis = Muhendis("Kamran", 3500, "Elektronika")
    praktikant = Praktikant("Rauf")

    mudir.maas_artir(10)
    muhendis.sertifakt_elave_et("ISO 9001")
    praktikant.maas_artir(100)  # Heç bir təsiri olmamalıdır

    print(mudir.melumat_goster())  # Ad: Aygün, Vəzifə: Müdir, Əmək haqqı: ...
    print(muhendis.melumat_goster())  # Ad: Kamran, Vəzifə: Mühəndis, Əmək haqqı: ...
    print(praktikant.melumat_goster())  # Ad: Rauf, Vəzifə: Praktikant, Əmək haqqı: 0
    statuslari_yoxla[mudir,muhendis,praktikant]