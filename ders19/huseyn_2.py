"""
Proqram:

reqemler.txt faylından rəqəmləri oxusun.
Cəmini hesablasın.
Faylda ədədi olmayan dəyərlər varsa, "Səhv məlumat tapıldı!" yazsın və həmin sətri ötürsün. Amma hər bir halda
ədədlərin cəmini versin.

try-except-else-finally istifadə etməyə çalışın.
"""
if __name__ == '__main__':
    with open ("reqemler.txt", 'r') as my_file:
        my_numbers = my_file.readlines()
    my_sum = 0
    for number in my_numbers:
        try:
            my_num = int(number.strip())
            my_sum += my_num
        except Exception as e:
            print(e, "Səhv məlumat tapıldı!", number.strip())
    print(my_sum)

