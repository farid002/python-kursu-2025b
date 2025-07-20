"""--------------------------Built-In Python funksiyaları----------------------------"""

"""
len()
any()
all()
map()
filter()
enumerate()
"""

cavab_any = any([True, False, False, True])
print("any", cavab_any)

cavab_all = all([True, False, True, True])
print("all", cavab_all)

ededler = [0, 2, 4, 6, 7, 8, 10, 1]

"""
cavablar = []
for eded in ededler:
    if eded%2==0:
        cavablar.append(True)
    else:
        cavablar.append(False)
"""
print(all(True if i%2==0 else False for i in ededler))

print(all(not i%2 for i in ededler))

str_ededler = ["0", "2","4","6","7", "8","10"]
inte_chevrilmish_ededler = list(map(int, str_ededler))
beshe_vurulmush_ededler = list(map(lambda z:z*5, inte_chevrilmish_ededler))
print(beshe_vurulmush_ededler)


str_ededler_2 = ["0", "2aaa","4dsd","6","7", "8","10"]
print("Filterlənmiş:", list(filter(lambda a:a<5, ededler)))






# print(all([True, True, True, True, True, True, False]))
# my_list = [1, 2, 4, 5, 3]
# print(all([number%4==0 for number in my_list]))
# print(any([number%4==0 for number in my_list]))
# print(my_list)
# factorial_list = list(map(factorial, my_list))
# print(factorial_list)

# my_list2 = ["1", "salam", "-4", "5aa", "3"]
# print("Filterlənmiş:", list(filter(str.isdigit, my_list2)))

"""
sum()
max()
min()
sorted()
reversed()
"""

print(sorted(ededler))
print(list(reversed(ededler)))


"""
print("my max", max(my_list))
print("my min", min(my_list))
print("my sum", sum(my_list))
print("my sorted", sorted(my_list))
print("my reversed", list(reversed(my_list)))

sorted_list = sorted(my_list)
"""

"""
type()
isinstance()
id()
"""

print(type(ededler))
print(isinstance(ededler, list))
print(id(ededler))

"""
print("===================")
print(type("Hello"))
print(type(my_list))
print(type(False))

print(isinstance(sorted_list, (bool, str, int)))
"""

"""
print()
input()
"""

"""
int()
float()
str()
list()
dict()
tuple()
bool()
"""
