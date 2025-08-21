"""
Fayllarla işləmə

open() funksiyası
    - r (oxumaq, yoxdursa xəta)
    - a (var olan contenti deyishmeden əlave etmək, fayl yoxdursa yarat)
    - w (contenti sifirla ve fayla yaz, fayl yoxdursa yarat)
    - x (yarat, varsa xəta)

    - t (tekst modu)
    - b (binary modu)
"""
"""
my_file = open("ders18/data100.txt", "r")
data_r = my_file.read()
my_file.close()

my_file = open("ders18/data100.txt", "a")
data_a = my_file.write("Aaaaaa")
my_file.close()

my_file = open("ders18/data100.txt", "w")
data_w = my_file.write("Aaaaaa")
my_file.close()
"""
"""
read()
readline()
readlines()
write()
close()
"""

my_file = open("ders18/data.txt", "r")
data_header = my_file.readline().strip().split(", ")
data_all = my_file.readlines()
# data_rls = my_file.read()
my_file.close()




"""
my_file = open("data.txt", "r")
data_line_1 = my_file.readline()
data_line_2 = my_file.readline()
print(data_line_1)
print(data_line_2)
my_file.close()
"""
"""
my_file = open("data.txt", "r")
data_line_all = my_file.readlines()
print(data_line_all)
my_file.close()
"""

"""
with:
    with open("data.txt", "r", encoding="utf-8") as file:
"""

with open("ders18/data.txt", "r") as my_file:
    my_files_rls = my_file.readlines()

# print(my_file.read())
"""

"""
"""
import os
os.remove("data2.txt")

if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("Bele fayl movcud deyil")
    """

import os

if os.path.exists("ders18/data/data2.txt"):
    os.remove("ders18/data/data2.txt")


if not os.path.exists("ders18/data/data4.txt"):
    open("ders18/data/data4.txt", "x")

print("----")

"""
with open('data.txt', 'r') as my_file:
    data_line_all = my_file.readlines()
    print(data_line_all[5])
import os
os.remove('file.txt')
os.path.exists('file.txt')
"""
