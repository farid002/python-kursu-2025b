"""
Problem:
Bir şirkətin işçiləri haqqında məlumatlar verilmişdir.

- Hər bir işçinin adı, yaşı və şöbəsini saxlayan bir dictionary yaradın.
- İstifadəçiyə bir işçinin adını daxil etməyi istəyin və həmin işçinin məlumatlarını ekrana çıxarın.
    - Əgər işçinin adı siyahıda yoxdursa, "Bu adlı işçi tapılmadı." mesajını göstərin.
- Unikal işçi adlarını çap edin

Dict'də ən az 3 işçi olmalıdır.
"""
from ders09.main import my_set

menim_list=[
    {
        "ad":"orxan",
        "yas":19,
        "shobe":"aa"
    },
    {
        "ad":"murad",
        "yas":21,
        "shobe":"bb"
    },
    {
        "ad":"ehmed",
        "yas":18,
        "shobe":"cc"
    }
]
axtarilan_ad=input("adi daxil et")
for adam in menim_list:
    if axtarilan_ad==adam["ad"]:
        print(adam)
        break
    else:
        print("bele adam yoxdur")
        break

