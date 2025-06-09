"""
---------------------------------KOMMENTLƏR------------------------------------------
təksətirli və çoxsətirli
"""
# Bu teksetirli kommentdir

"""
Bu choxsetirli kommentdir
bura da
bura da
"""

'''
Bu choxsetirli kommentdir
bura da
bura da
'''

"""
----------------------------------DƏYİŞKƏNLƏR----------------------------------------

Dəyişkən adları qayda:
    - Hərf və ya alt xətt ilə başlamalıdır.
    - Hərflər, rəqəmlər və alt xəttlərdən ibarət ola bilər (xüsusi simvol və ya boşluq yoxdur).
    - Böyük hərfə həssasdır (myVar və myvar fərqlidir).

Dəyişkənlərin təyini
    - Dəyişkənlər "=" operatorundan istifadə etməklə təyin edilir.
    - Daha sonra dəyişənin dəyərini dəyişə bilərsiniz.
    - Python eyni anda çoxlu təyinata imkan verir:

Dəyişkən adları
    - Dəyişkəndə saxlanan dəyəri əks etdirən mənalı adlar seçin.
    - Dəyişən adları üçün snake_case istifadə edin (məsələn, first_name, total_price).
    - if, else, while, for kimi açar sözlərdən istifadə etməyin.
"""

var1 = 5  # var1 = 5
var2 = var1 # var1 = 5, var2 = 5
var1 = 3 # var1 = 3, var2 = 5
var2 = var1 # var1 = 3, var2 = 3


# menali deyishken adlari sechmek

weight = 85
height = 185


"""
Dəyişkən dəyərini yazdırmaq: print()
"""



"""
-----------------------------------SABİTLƏR-----------------------------------------
"""

CONSTANT = 100
BIR_GUNDE_SAAT = 24



"""
----------------------------------DATA TİPLƏRİ--------------------------------------
Ümumi data tipləri: 
    - int (tam sayı)
    - float (onluq sayı)
    - str (sətir)
    - bool (boolean: doğru və yanlış) - True, False

    - list, tuple, dict, set (bunlar haqqında daha sonrakı dərslərdə)
"""
age = 25  # tam sayi - integer
number_of_students = 5 # tam sayi - integer
PI = 3.14  # kesrli saylar - float

ad = "55"
soyad = "Huseynov"
did_student_pass_exam = False

# print(ad)


"""
------------Riyazi operatorlar-----------
    - Toplama:      +   2 + 3   (=5)      
    - Çıxma:        -   5 - 3   (=2)
    - Vurma:        *   2 * 3   (=6)
    - Bölmə:        /   7 / 2   (=3.5)
    - Qalıq:        %   11 % 4  (=3)   
    - Üst:          **  2 ** 3  (=8)
    - Tam qismət:   //  14 // 3 (=4)
"""
a = 5
b = 3
c = a ** b
# print(c)

a2 = "5.8"
b2 = "3"
c2 = a2 + b2

# print(type(c2))
# print(c2)

"""
type() funksiyası
int()
float() və round()
str()
bool()
"""
c2 = int(float(a2)) + int(b2)

a5 = 5.5
a5 = round(a5)
a_str = str(a5)

print(a_str)
