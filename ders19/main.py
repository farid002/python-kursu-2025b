"""
try
except
else - except-ə daxil olmazsa (exceptsiz else yazila bilmez)
finally - hər halda
"""

try:
    a = {2: "16", 5: "b", 15: "c"}
    b = a[2]
    my_list = [1,2,5,6]
    print(my_list[int(b**0.5)])
except Exception as e:
    print(e, "Bolme olmadi")
else:
    print("Ugurlu emeliyyat")
finally:
    print("Her zaman")







"""
while True:
    try:
        my_var = input()
        print(5/my_var)
    except:
        print("Bolme mumkun deyil")
"""

"""
# while True:
    try:
        my_var = int(input())
        print(5/my_var)
    except:
        print("Bolme mumkun deyil")
"""
"""
ZeroDivisionError - 0 a bölmə
TypeError - tip xətası
ValueError - dəyər xətası
FileNotFoundError - fayl tapılmadı xətası
IndexError - İndeks xətası
"""

print("alma" * 2)





try:
    my_var = int(0)
    print(5/my_var)
except ZeroDivisionError as err:
    print("0-a Bolme mumkun deyil: ", err)
except ValueError as e:
    print("Bolme mumkun deyil, deyer xetasi: ", e)
except TypeError as e:
    print("Bolme mumkun deyil, tip xetasi: ", e)
except:
    print("Something went wrong")

"""
raise error
"""

my_var = int(input())
if my_var == 100:
    raise ArithmeticError("Bu deyishkene 100 vermek olmaz")

my_var2 = int(input())
my_var3 = int(input())
my_var4 = int(input())

print(sum([my_var2, my_var3, my_var4]))
