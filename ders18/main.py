"""
Fayllarla işləmə

open() funksiyası
    - r (oxumaq, yoxdursa xəta)
    - a (əlave etmək, yoxdursa yarat)
    - w (yaz, yoxdursa yarat)
    - x (yarat, varsa xəta)

    - t (tekst modu)
    - b (binary modu)
"""
my_file = open("data.txt", "r")
data = my_file.read()
#print(data)
my_file.close()

my_file = open("data2.txt", "w")
data = my_file.write("Aaaaaa")
#print(data)
my_file.close()

"""
read()
readline()
readlines()
write()
close()
"""
my_file = open("data.txt", "r")
data_line_1 = my_file.readline()
data_line_2 = my_file.readline()
print(data_line_1)
print(data_line_2)
my_file.close()


my_file = open("data.txt", "r")
data_line_all = my_file.readlines()
print(data_line_all)
my_file.close()


"""
with:
    with open("data.txt", "r", encoding="utf-8") as file:
"""
with open("data.txt", "r") as my_file:
    data_line_all = my_file.readlines()
    print(data_line_all[5])

# print(my_file.read())
"""
import os
os.remove("file.txt")
os.path.exists("file.txt")
"""

import os
os.remove("data2.txt")

if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("Bele fayl movcud deyil")