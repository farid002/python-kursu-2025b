"""
try
except
else - except-ə daxil olmazsa
finally - hər halda
"""
"""
while True:
    try:
        my_var = int(input())
        print(5/my_var)
    except:
        print("Bolme mumkun deyil")
"""
"""
ZeroDivisionError - 0 a bölmə
ValueError - dəyər xətası
FileNotFoundError - fayl tapılmadı xətası
IndexError - İndeks xətası
"""

try:
    my_var = int([1,23])
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
    raise ValueError("Bu deyishkene 100 vermek olmaz")

my_var2 = int(input())
my_var3 = int(input())
my_var4 = int(input())

print(sum([my_var2, my_var3, my_var4]))