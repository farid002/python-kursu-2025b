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
        "ad" : "murad",
        "yas" : 21 ,
        "sobesi": "bekar"
    },
    {
         "ad": "orxan",
         "yas" : 19,
         "sobesi": "fehle"
    },
    {
        "ad": "ehmed",
        "yas": 18,
        "sobesi": "satici"
    }
]

my_input=input("iscinin adini daxil edin")
adam_tapildimi = False
for isci in my_list:
    if my_input == isci["ad"]:
        print(isci)
        adam_tapildimi = True
        break

if not adam_tapildimi:
    print("bu adli isci tapilmadi")

