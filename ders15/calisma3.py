"""
Tapşırıq: Şirkət İşçi Sistemi (Enkapsulyasiya və Polimorfizm)

Tələblər:

1. 'Isci' (İşçi) adlı əsas sinif yaradın.
   Sinifdə aşağıdakı private (__) atributlar olmalıdır:
       __ad – İşçinin adı
       __vezife – Vəzifəsi (yalnız daxilində təyin olunur)
       __emek_haqqi – Əmək haqqı (birbaşa giriş qadağandır)

   Aşağıdakı metodları yazın:
       __init__(self, ad, emek_haqqi) – Ad və əmək haqqını təyin etsin. Vəzifə subclass tərəfindən verilsin.
       melumat_goster(self) – İşçi haqqında məlumat qaytarsın: Ad, vəzifə, əmək haqqı
       maas_artir(self, faiz) – Əmək haqqını faizlə artırsın
       status(self) – "Ümumi işçi" mesajı qaytarsın

2. Aşağıdakı sinifləri 'Isci' sinifindən törədin:

   a) Mudir sinifi:
       - Əlavə atribut: __departament
       - status() metodunu override edin: "Müdir – şöbə: {departament}"
       - departament_deyis(self, yeni_ad) – şöbəni dəyişmək üçün metod

   b) Muhendis sinifi:
       - Əlavə atribut: __ixtisas
       - status() metodunu override edin: "Mühəndis – ixtisas: {ixtisas}"
       - sertifikat_elave_et(self, sertifikat) – Sertifikat siyahısına yeni sertifikat əlavə etsin

   c) Praktikant sinifi:
       - Əmək haqqı default olaraq 0 olsun
       - status() metodunu override edin: "Praktikant – təcrübə dövründədir"
       - maas_artir() metodunu override edib heç bir dəyişiklik etməsin

3. Aşağıdakı funksiyanı yaradın:
    def statuslari_yoxla(isci_siyahisi):
        # Siyahıdakı bütün işçilərin status() metodunu çağırın

---

Nümunə İstifadə:

mudir = Mudir("Aygün", 5000, "IT")
muhendis = Muhendis("Kamran", 3500, "Elektronika")
praktikant = Praktikant("Rauf")

mudir.maas_artir(10)
muhendis.sertifikat_elave_et("ISO 9001")
praktikant.maas_artir(100)  # Heç bir təsiri olmamalıdır

print(mudir.melumat_goster())       # Ad: Aygün, Vəzifə: Müdir, Əmək haqqı: ...
print(muhendis.melumat_goster())    # Ad: Kamran, Vəzifə: Mühəndis, Əmək haqqı: ...
print(praktikant.melumat_goster())  # Ad: Rauf, Vəzifə: Praktikant, Əmək haqqı: 0

statuslari_yoxla([mudir, muhendis, praktikant])
# Çıxış:
# Müdir – şöbə: IT
# Mühəndis – ixtisas: Elektronika
# Praktikant – təcrübə dövründədir
"""
