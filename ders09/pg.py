"""
Problem:
Bir şirkətin işçiləri haqqında məlumatlar verilmişdir.

- Hər bir işçinin adı, yaşı və şöbəsini saxlayan bir dictionary list yaradın.
- İstifadəçiyə bir işçinin adını daxil etməyi istəyin və həmin işçinin məlumatlarını ekrana çıxarın.
    - Əgər işçinin adı siyahıda yoxdursa, "Bu adlı işçi tapılmadı." mesajını göstərin.
- Unikal işçi adlarını çap edin

Dict'də ən az 3 işçi olmalıdır.
"""
# Bu Kod əgər eyni adda 1 dən çox işçi varsa səndən işçinin şöbəsini yazmanı istəyir. və işçini ona görə tapır.

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
    },
    {
        "ad" : "Oğuz",
        "yaş": 30,
        "şöbə": "Mühəndis"
    }
]
my_set = set()
my_isci = input("İşçi adı daxil edin: ").capitalize()
is_exist = None
adlar = []
for isci in my_dict_list:
    if my_isci == isci["ad"]:
        adlar.append(isci["ad"])

if adlar.count(my_isci) == 1:
    print(f"İşçinin adı:{(my_dict_list[adlar.index(my_isci)]["ad"])} \nYaşı:{(my_dict_list[adlar.index(my_isci)]["yaş"])} "
          f"\nşöbəsi: {(my_dict_list[adlar.index(my_isci)]["şöbə"])} ")

elif adlar.count(my_isci) == 0:
    print("Bu adlı işçi tapılmadı.")
    for isci in my_dict_list:
        my_set.add(isci["ad"])
    print("______________________________ \nUnikal işçi adları: ", my_set)

elif adlar.count(my_isci) > 1:
    my_sobe = input("Bu adda birdən çox işçi var. Şöbəni yazın: ").capitalize()
    for sobe in my_dict_list:
        if my_isci == sobe["ad"] and my_sobe == sobe["şöbə"]:
            print(f"İşçinin adı:{sobe['ad']} \nYaşı:{sobe['yaş']} \nşöbəsi: {sobe['şöbə']} ")
            break
    else:
        print("Bu adda şöbə yoxdur")