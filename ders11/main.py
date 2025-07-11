"""--------------------------Built-In Python funksiyaları----------------------------"""

"""
len()
any()
all()
map()
filter()
enumerate()
"""
# print(all([True, True, True, True, True, True, False]))
# from math import factorial


my_list = [1, 2, 4, 5, 3]
# print(all([number%4==0 for number in my_list]))
# print(any([number%4==0 for number in my_list]))
print(my_list)
# factorial_list = list(map(factorial, my_list))
# print(factorial_list)

my_list2 = ["1", "salam", "-4", "5aa", "3"]
print("Filterlənmiş:", list(filter(str.isdigit, my_list2)))

"""
sum()
max()
min()
sorted()
reversed()
"""
print("my max", max(my_list))
print("my min", min(my_list))
print("my sum", sum(my_list))
print("my sorted", sorted(my_list))
print("my reversed", list(reversed(my_list)))

sorted_list = sorted(my_list)

"""
type()
isinstance()
id()
"""
print("===================")
print(type("Hello"))
print(type(my_list))
print(type(False))

print(isinstance(sorted_list, (bool, str, int)))


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


"""
import
as
*
from
venv
requirements.txt
"""
