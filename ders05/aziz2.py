qiymet=0
while True:
    age=input("Hər sətirdə bir yaş daxil edilməklə, qrupdakı bütün qonaqların yaşlarını yazın")
    if str(age).lower=="exit":
        print(f"Ödəniş {qiymet} Usd olacaq.")
        break
    if age=="0":
        print("Duzgun deyer girin")
    if int(age):
        if int(age)<=2:
            print("2 yaş və daha kiçik qonaqlar ödənişsiz qəbul edilir.")
            print(f"{qiymet} Usd")
            print("Əgər bitirmək istəsəniz exit yazın, dəvam eləmək istəsəniz yenidən rəqəm daxil eləyip Enter butonuna basın")
        elif int(age)<12:
            print("3-12 yaş arası uşaqlar 14.90 dollara başa gəlir.")
            qiymet+=14.90
            print(f"{qiymet} Usd")
            print("Əgər bitirmək istəsəniz exit yazın, dəvam eləmək istəsəniz yenidən rəqəm daxil eləyip Enter butonuna basın")
        elif int(age)<65:
            print("12-65 yaş aralığına daxil bütün müştərilərə 23.90 dollardır")
            qiymet+=23.90
            print(f"{qiymet} Usd")
            print("Əgər bitirmək istəsəniz exit yazın, dəvam eləmək istəsəniz yenidən rəqəm daxil eləyip Enter butonuna basın")

        elif int(age)>=65:
            print("65 yaşdan yuxarı yaşlılar üçün 18.90 dollara başa gəlir.")
            qiymet+=18.90
            print(f"{qiymet} Usd")
            print("Əgər bitirmək istəsəniz exit yazın, dəvam eləmək istəsəniz yenidən rəqəm daxil eləyip Enter butonuna basın")
