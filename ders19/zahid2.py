"""
Proqram:

reqemler.txt faylından rəqəmləri oxusun.
Cəmini hesablasın.
Faylda ədədi olmayan dəyərlər varsa, "Səhv məlumat tapıldı!" yazsın və həmin sətri ötürsün. Amma hər bir halda
ədədlərin cəmini versin.

try-except-else-finally istifadə etməyə çalışın.
"""
if __name__ == '__main__':
    with open("reqemler.txt","r") as a:
        my_file_lines=a.readlines()
    lines_sum=0
    for i in my_file_lines:
        try:
            lines_sum+=int(i) #Olmasa int(i[0:-2])
        except ValueError as f:
            print(f, "Səhv məlumat tapıldı!")
        else:
            print("Dogru melumat")
    print(lines_sum)