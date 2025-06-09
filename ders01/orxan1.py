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

suse_qablar = input("Şüşə qabların sayı: ")
plastik_qablar = input("Plastik qabların sayı: ")
umumi_qablar=int(suse_qablar)+int(plastik_qablar)
print(umumi_qablar)
umumi_depozit=int(suse_qablar)*0.08 + int(plastik_qablar)*0.25
print("Cəmi qaytarılacaq məbləğ " + str(umumi_depozit))
