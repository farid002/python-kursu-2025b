"""
Problem:
Bir şirkətin işçiləri haqqında məlumatlar verilmişdir.

- Hər bir işçinin adı, yaşı və şöbəsini saxlayan bir dictionary list yaradın.
- İstifadəçiyə bir işçinin adını daxil etməyi istəyin və həmin işçinin məlumatlarını ekrana çıxarın.
    - Əgər işçinin adı siyahıda yoxdursa, "Bu adlı işçi tapılmadı." mesajını göstərin.
- Unikal işçi adlarını çap edin

Dict'də ən az 3 işçi olmalıdır.
"""

my_dict_list = [
    {
        "ad" : "Farid",
        "yaş": 25,
        "şöbə": "IT"
    },
    {
        "ad" : "Huseyn",
        "yaş": 26,
        "şöbə": "İnşaat"
    },
    {
        "ad" : "Oğuz",
        "yaş": 24,
        "şöbə": "Elektrik"
    }
]

my_isci = input("İşçi adı daxil edin: ").capitalize()
isci_siyahisi = set()
for isci in my_dict_list:
    if my_isci == isci["ad"]:
        print(f"İşçinin adı:{isci['ad']} \nYaşı:{isci['yaş']} \nşöbəsi: {isci['şöbə']} ")
        break
    else:
        print("Bu adlı işçi tapılmadı.")