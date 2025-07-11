"""
Problem:
Bir şirkətin işçiləri haqqında məlumatlar verilmişdir.

- Hər bir işçinin adı, yaşı və şöbəsini saxlayan bir dictionary yaradın.
- İstifadəçiyə bir işçinin adını daxil etməyi istəyin və həmin işçinin məlumatlarını ekrana çıxarın.
    - Əgər işçinin adı siyahıda yoxdursa, "Bu adlı işçi tapılmadı." mesajını göstərin.
- Unikal işçi adlarını çap edin

Dict'də ən az 3 işçi olmalıdır.
"""


my_list = [
    {
        "ad":"ehmed",
        "yas":18,
        "şöbe":"programmer"

    },
    {
        "ad":"murad",
        "yas":22,
        "şöbe":"tok"

    },
    {
        "ad":"orxan",
        "yas":19,
        "şöbe":"memar"}

]
ad = input("ad yazin").lower()
for i in my_list:
    if ad == i['ad']:
        print(i)

