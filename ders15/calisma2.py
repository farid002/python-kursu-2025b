"""
Tapşırıq 2: Oyunçu (Gamer) Sinifi
Tələblər:

Oyunçu adlı bir sinif yaradın.
Sinifdə aşağıdakı private (__) atributlar olmalıdır:
    __ad – Oyunçunun adı.
    __səviyyə – Oyunçunun səviyyəsi (default olaraq 1).
    __xal – Oyunçunun qazandığı xal (default olaraq 0).

Aşağıdakı metodları yazın:
    __init__(self, ad) – Oyunçunun adını təyin etsin, səviyyə və xal isə default olaraq təyin olunsun.
    məlumat_göstər(self) – Oyunçunun adını, səviyyəsini və xalını qaytarsın.
    xal_əlavə_et(self, xal) – Yeni xal əlavə etsin və əgər xal 100 və ya daha çox olarsa, oyunçunun səviyyəsini 1 artırıb, xalı 0-a sıfırlasın.

Private atributlara birbaşa giriş olmasın!

---
Nümunə İstifadə:

oyunçu = Oyunçu("Ali")
print(oyunçu.məlumat_göstər())  # Oyunçu: Ali, Səviyyə: 1, Xal: 0
oyunçu.xal_əlavə_et(50)
print(oyunçu.məlumat_göstər())  # Oyunçu: Ali, Səviyyə: 1, Xal: 50
oyunçu.xal_əlavə_et(60)  # Təbriklər! Ali yeni səviyyəyə keçdi!
print(oyunçu.məlumat_göstər())  # Oyunçu: Ali, Səviyyə: 2, Xal: 0
"""