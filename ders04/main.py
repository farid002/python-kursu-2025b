"""
----------------------------------------LİSTLƏR----------------------------------------------
Yeni data tip: list()
Dəyər [] əhatə olunur və elemntlər bir birilə , -lə ayrılır.

Məs.:
empty_list = []
my_int_list = [12, 15, 105, 0, -5]
my_str_list = ["salam", "hello", "hallo"]
my_mixed_list = [15, "hello", True]
"""

empty_list = []
int_list = [2, 4, 6, 8, 10]
str_list = ["salam", "hello", "hallo", 10]
my_mixed_list = [15, "hello", True, 15.5]

# print(type(str_list))

my_str = "salam"
# print(str_list[0])

"""
Hər hansı elementi onun indeksi ilə əldə edə bilərik. 
Məs.: print(my_mixed_list[1])

Həm də istənilən indeksdəki dəyəri dəyişmək mümkündür.
Məs.: my_str_list[1] = "salam"
"""
str_list[2] = "privet"


"""
count()
append()
extend()
pop()                   -> __index attribute-u -> pop(3)
sort()                  -> reverse attribute-u -> sort(reverse=True)
"""
str_list.append("random")
str_list.append("random")
str_list.append("bbb")
str_list.append("ccc")
str_list.append(15)

str_list2= ["ZZ", "yyy", "2"]
# print(str_list.count("hello"))
str_list.extend(str_list2)

#print(str_list.index("random"))
#print(str_list.pop(2))
# str_list.sort()

str_list3 = str_list.copy()
#print(str_list.insert(2, "UUU"))
#print(str_list3)
str_list[0] = "__"
#print(str_list)

a = [
    [1, 2, 3],
    [4, 5, 6, 7, 9],
    [7, 8, 9, 10]
]

#print(a[1].pop())
#print(a)


"""
Pythonda listlər üçün bəzi vacib built-in funksiyalar:
del my_mixed_list[3]
len()
max()
min()
sum()
"""


"""
----------------------------------------FOR DÖNGÜSÜ--------------------------------------------

for <döngü elementi> in <döngü listi, ardıcıllığı>
    <kod bloku>

# step dəyəri həm də mənfi ədəd ola bilər, lakin yalnız o halda ki, start stop-dan böyükdür.
for i in range(0, 10, 2):  # start, stop, step
    print(i)

start default: 0
stop mütləq təyin olunmalıdır
step default: 1
"""


matrix = [[1,2,3],[4,5,6],[7,8,9]]

for row in matrix:
    for value in row:
        print(value ** 2, end=" ")



# print(i, end=" ")


"""
Listlərdə for döngüsü

my_list = ['a', 'b', 'c', 'd']
for item in my_list:
    print(item)


my_list = [12, 15, 1556, 15, -5.14, 323434, 34344]
for element in my_list:
    print(element)
    if element == 15:
        pass
    print("swaqda")

for element in range(15, 0, -1):
    print(element)

my_str = "Salam"

for char in my_str:
    print(char)
"""


"""
string üçün for döngüsü

my_str = 'hello'
for char in my_str:
    print(char)
"""
