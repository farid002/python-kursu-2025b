"""
Sətir əməliyyatları:
    - Birləşdirmə: "+" operatorundan istifadə edərək sətirləri birləşdirin.
    - Təkrarlama: "*" operatorundan istifadə edərək sətri təkrarlayın.
    - İndeksləmə: İndeks mövqelərindən istifadə edərək müəyyən hərfləri əldə edin.
    - Dilimləmə: İndekslərdən istifadə edərək sub-sətir çıxarın.
    - Funksiya və metodlar:
        - len() - built in

        - upper()
        - lower()
        - title()
        - capitalize()
        - count()
        - find()
        - replace()
        - split()
        daha ətraflı aşağıda
"""

my_str = "Salam Necesiniz?"
# print(my_str)
# print(my_str.lower())
# print(my_str.upper())
# print(len(my_str))
# print(my_str.capitalize())
# print(my_str.count("393"))
# print(my_str.find("0"))
# print(my_str.replace("Salam", "Hello"))
# print(my_str.split("x"))
my_str_2 = "Haradasiniz?"
# print(my_str_2[5])
# print(my_str_2[5:9])
# print(my_str_2[-2])
# print(my_str_2[::-1])
# print(my_str_2[::2])
# print(my_str, my_str_2)
# print(my_str_2 * 2)

"""
f-string
"""
my_age = 25
my_height = 195.56
# print("Yashiniz: " + str(my_age) + ".")
# print(f"Yashiniz: {my_age}. Hundurluk: {my_height}.")

"""
Tip çevirmədə əsas xətalar: ValueError, TypeError, IndexError
"""
# print(int("salam"))
# print(float("salam"))
my_list = [1, 2, 3]
# print(my_list[0:2])
# print(17 // 3)

# int("5.5")
# int([1,2,3])


"""
METOD / FUNKSIYA	    AÇIQLAMA
------------------------------------------------------------------------------------------
capitalize()	        İlk hərfi böyük hərfə çevirir
casefold()	            Sətiri kiçik hərflərə çevirir
center()	            Sətiri ortada yerləşdirir
count()	                Müəyyən bir dəyərin sətirdə neçə dəfə göründüyünü qaytarır
encode()	            Sətirin kodlaşdırılmış versiyasını qaytarır
endswith()	            Sətirin müəyyən bir dəyər ilə bitib-bitmədiyini yoxlayır
expandtabs()	        Sətirin tab boşluğunu təyin edir
find()	                Müəyyən bir dəyəri axtarır və ilk tapılan mövqeyi qaytarır
format()	            Müəyyən edilmiş dəyərləri sətirdə formatlaşdırır
format_map()	        Müəyyən edilmiş dəyərləri sətirdə formatlaşdırır
index()	                Müəyyən bir dəyəri axtarır və ilk tapılan mövqeyi qaytarır
isalnum()	            Sətirin bütün simvollarının hərf və ya rəqəm olub-olmadığını yoxlayır
isalpha()	            Sətirin bütün simvollarının yalnız hərf olub-olmadığını yoxlayır
isascii()	            Sətirin bütün simvollarının ASCII simvolları olub-olmadığını yoxlayır
isdecimal()	            Sətirin bütün simvollarının onluq rəqəmlər olub-olmadığını yoxlayır
isdigit()	            Sətirin bütün simvollarının rəqəm olub-olmadığını yoxlayır
isidentifier()	        Sətirin identifikator olub-olmadığını yoxlayır
islower()	            Sətirin bütün hərflərinin kiçik olub-olmadığını yoxlayır
isnumeric()	            Sətirin bütün simvollarının rəqəm olub-olmadığını yoxlayır
isprintable()	        Sətirin bütün simvollarının çap edilə bilər olub-olmadığını yoxlayır
isspace()	            Sətirin bütün simvollarının boşluq olub-olmadığını yoxlayır
istitle()	            Sətirin başlıq qaydalarına uyğun olub-olmadığını yoxlayır
isupper()	            Sətirin bütün hərflərinin böyük hərf olub-olmadığını yoxlayır
join()	                Təkrarlanan elementləri sətirə çevirir
ljust()	                Sətirin sola uyğunlaşdırılmış versiyasını qaytarır
lower()	                Sətiri kiçik hərflərə çevirir
lstrip()	            Sol tərəfdən boşluqları silir
maketrans()	            Tərcümə cədvəli qaytarır
partition()	            Sətiri üç hissəyə ayırıb tuple şəklində qaytarır
replace()	            Müəyyən edilmiş dəyəri başqası ilə əvəz edir
rfind()	                Müəyyən bir dəyəri axtarır və son tapılan mövqeyi qaytarır
rindex()	            Müəyyən bir dəyəri axtarır və son tapılan mövqeyi qaytarır
rjust()	                Sətirin sağa uyğunlaşdırılmış versiyasını qaytarır
rpartition()	        Sətiri üç hissəyə ayırıb tuple şəklində qaytarır
rsplit()	            Sətiri verilmiş separator üzrə bölür və siyahı qaytarır
rstrip()	            Sağ tərəfdən boşluqları silir
split()	                Sətiri verilmiş separator üzrə bölür və siyahı qaytarır
splitlines()	        Sətiri sətir qırılmalarına görə bölür və siyahı qaytarır
startswith()	        Sətirin müəyyən bir dəyər ilə başlayıb-başlamadığını yoxlayır
strip()	                Sətirdəki boşluqları silir
swapcase()	            Böyük hərfləri kiçik, kiçikləri isə böyük edir
title()	                Hər sözün ilk hərfini böyük edir
translate()	            Tərcümə edilmiş sətiri qaytarır
upper()	                Sətiri böyük hərflərə çevirir
zfill()	                Sətiri başlanğıcda sıfırlarla doldurur
"""


# GƏLƏN DƏRS
"""
--------------------------------MÜQAYİSƏ OPERATORLARI--------------------------------
Şərt ifadələrində müqayisə operatorlarından istifadə olunur:
`==`, `!=`, `>`, `<`, `>=`, `<=`
"""
a = 5
b = 6
# print(a != b)


"""
--------------------------------MƏNTİQİ OPERATORLAR------------------------------------
and, or, not
"""
a = "salam"
b = "sAlAm"
print(a.upper() == b.upper())