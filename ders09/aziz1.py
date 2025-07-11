"""
Problem:
Bir şirkətin işçiləri haqqında məlumatlar verilmişdir.

- Hər bir işçinin adı, yaşı və şöbəsini saxlayan bir dictionary yaradın.
- İstifadəçiyə bir işçinin adını daxil etməyi istəyin və həmin işçinin məlumatlarını ekrana çıxarın.
    - Əgər işçinin adı siyahıda yoxdursa, "Bu adlı işçi tapılmadı." mesajını göstərin.
- Unikal işçi adlarını çap edin

Dict'də ən az 3 işçi olmalıdır.
"""
"""""""""""""""""""""""""""""""""--------- 3 SAATDAN ARTIQ DERSLERE YOX DEYEK ---------"""""""""""""""""""""""""""""""""
my_dicts_list=[
    {
    "ad":"Farid",
    "yas":250,
    "shobe":"A",
    "rutbe":"Stajer",
    "maas":"yol yemek"
     },
    {
    "ad":"Oguz",
    "yas":20,
    "shobe":"B",
    "rutbe":"Isci",
    "maas":"Asgari ucret"
    },
    {
    "ad":"Oguz",    # ORGINAL
    "yas":25,
    "shobe":"D",
    "rutbe":"Mudur",
    "maas":"1.5k dollar"
    },
    {
    "ad":"Zahid",
    "yas":15,
    "shobe":"C",
    "rutbe":"CEO",
    "maas":"15k dollar"   #Vergisiz
    },
]
user_name=input("Isci adini yazin").capitalize()
isci_varmi=False
my_names_list=[]
for i in my_dicts_list:
    if i["ad"]==user_name:
        isci_varmi=True
    my_names_list.append(i["ad"])
print("Yazdiginiz adda isci var")if isci_varmi else print("Yazdiginiz adda isci yoxdur")
print("Unikal isci adlari",set(my_names_list))
"""""""""""""""""""""""""""""""""--------- 3 SAATDAN ARTIQ DERSLERE YOX DEYEK ---------"""""""""""""""""""""""""""""""""