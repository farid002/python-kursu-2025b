"""
----------------------------------------TUPLE----------------------------------------

    - Dəyişdirilə bilməyən (immutable)
    - Siralı
koordinatlar (x, y, z), doğum tarixi və s.
"""

my_tuple = (1, 6, 2, 5, 4, 5)
# print(my_tuple)
# print(my_tuple.index(6))
# print(my_tuple.count(5))

my_str_tuple = ("sada", "213", "salam")
my_mix_tuple = ("Ali", "Aliyev", 25)  # ad soyad, yas

my_coor = ((15, 45), [12,15], 1998, False)
# print(type(my_coor[2]))

""" 
----------------------------------------enumerate()----------------------------------------
"""

for index, ad in enumerate(["Huseyn", "Murad", "Zahid", "Ahmad", "Orxan"]):
    # print(ad)
    pass


"""
----------------------------------------LIST COMPREHENSION----------------------------------------

Tək sətirdə list elementləri üzərində əməliyyat (list comprehension)

my_list = [1, 2, 3]
squares = [my_number**2 for my_number in my_list]
print(squares)


klassik metod:

my_list = [1, 2, 3]
squares = []

for my_number in my_list:
    squares.append(my_number**2)
print(squares)
"""

my_list = [1, 2, 3]
squares = []

for my_number in my_list:
    squares.append(my_number**2)
# print(squares)






my_list = [1, 2, 3]
# squares = [element + (5 if element % 2 == 0 else 0) for element in my_list]

squares = []
for element in my_list:
    if element % 2 == 0:
        squares.append(element + 5)
    else:
        squares.append(element)


print(squares)


"""
Tək və ya cütlüyü yoxlayan proqram

my_list = [1, 2, 3, 4, 5, 6]
result = ['Cüt' if my_number % 2 == 0 else 'Tək' for my_number in my_list]
print(result)

klassik metodla:
my_list = [1, 2, 3, 4, 5, 6]
result = []
for my_number in my_list:
    if my_number % 2 == 0:
        result.append("Cüt")
    else:
        result.append("Tək")
print(result)
"""

my_list = [1, 2, 3, 4, 5, 6]
result = ['Cüt' if my_number % 2 == 0 else 'Tək' for my_number in my_list]
print(result)

result = [element for element in range(100, 49, -1)]
print(result)


# klassik metodla:
my_list = [1, 2, 3, 4, 5, 6]
result = []
for my_number in my_list:
    if my_number % 2 == 0:
        result.append("Cüt")
    else:
        result.append("Tək")
print(result)

"""
Tək sətirdə iç-içə döngüdə list elementləri üzərində əməliyyat (nested loop list comprehension)

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in my_list for item in row]
print(flattened)
"""


# result = [item for row in my_list for item in row]

my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = []
for row in my_list:
    for item in row:
        result.append(item)

print(result)
