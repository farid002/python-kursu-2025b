"""
Almaniyada insanları təkrar emal etməyə təşviq etmək üçün içki qablarına kiçik bir depozit əlavə olunur (Refund).

Şüşə içki qabları üçün 0,08 avro;
Plastik içki qabları üçün isə 0,25 avro depozit var.

Elə proqram yazın ki:
    - İstifadəçidən hər tipdə qabların sayını alsın
    - Həmin qabların qaytarılması üçün alınacaq pulu hesablayıb istfadəçiyə göstərsin.
    - Çıxışı elə formatlayın ki, avro işarəsi əlavə edilsin və məbləğdə həmişə iki onluq yer göstərilsin.

Məsələn:
Şüşə qabların sayı: ...
Plastik qabların sayı: ...

Cəmi qaytarılacaq məbləğ - 2.25 €
"""
suse_qablarin_sayi = input("Suse qablarin sayi")
plastik_qablarin_sayi = input("Plastik qablarin sayi")
adama_qaytarilacaq_pul= int(suse_qablarin_sayi)*0.08 + int(plastik_qablarin_sayi)*0.25
print(str(adama_qaytarilacaq_pul)+" €") #cox sagolun