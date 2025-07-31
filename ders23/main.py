"""
pip install numpy

import numpy as np

a = np.array([1, 2, 3])
print(a)


Funksiya            İstifadəsi                          Nümunə
np.array()	        Yeni array yaratmaq	                np.array([1, 2, 3])
np.zeros()	        Sıfırlarla dolu array	            np.zeros((2, 3))
np.ones()	        Birlərlə dolu array	                np.ones((3, 3))
np.arange()	        Ədədi sıra yaratmaq	                np.arange(0, 10, 2)
np.linspace()	    Bərabər intervallarla ədədlər	    np.linspace(0, 1, 5)
np.reshape()	    Ölçünü dəyişmək	                    a.reshape(3, 1)
np.mean()	        Orta tapmaq	                        np.mean(a)
np.max()	        Maksimum dəyər	                    np.max(a)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(b.shape)    # Ölçüsü
print(a + b)      # Toplama
print(a * b)      # Element üzrə vurma
print(a.dot(b))   # Skalyar hasil
print(a[a > 2])   # 2-dən böyük elementlər
"""
import numpy as np

# a1 = np.array([2, 2, 2])
# a2 = np.zeros((0, 0))
# a3 = np.ones((5, 3))
# a4 = np.arange(0, 10, 2)
# a5 = np.linspace(0, 10, 10)

a1 = np.array([2, 2, 2, 1, 3, 5, 8, 9, 10, 11, 12, 0])
a2 = np.array([5, 3, 2, 1, 4, 5, 8, 9, 1, 1, 2, 0])
# print(np.sum(a1))
# print(np.max(a))
# print(np.min(a))
# print(type(a))

a1_list = [2, 2, 2, 1, 3, 5, 8, 9, 10, 11, 12, 6]
a2_list = [5, 3, 2, 1, 4, 5, 8, 9, 1, 1, 2, 0]

# print(a1_list + a2_list)
# print(a1 + a2)

a = a2[a2 != 5]
# print(a)

my_list = [1, "asds", 45]
print(type(my_list[0]), type(my_list[1]), type(my_list[2]))
my_array = np.array([1, "asdsad", 45])
print(type(my_array[0]), type(my_array[1]), type(my_array[2]))
print(int(my_array[0]) * int(my_array[2]))


"""
Numpy vs List

1. SÜRƏT
import numpy as np
import time

# NumPy array
start = time.time()
a = np.arange(1000000)
a = a * 2
end = time.time()
print("NumPy vaxtı:", end - start)

# Python list
start = time.time()
b = list(range(1000000))
b = [x * 2 for x in b]
end = time.time()
print("List vaxtı:", end - start)


2. YADDAŞ
import numpy as np
import sys

lst = list(range(1000))
arr = np.array(lst)

print("List yaddaş:", sys.getsizeof(lst))
print("Array yaddaş:", arr.nbytes)


3. Verilən Tipi (Data Type)
lst = [1, "iki", 3.0]     # Mümkündür
arr = np.array([1, "iki", 3.0])  # Hamısını string-ə çevirəcək
print(arr)  # ['1' 'iki' '3.0']


4. Vektor Əməliyyatları
a = [1, 2, 3]
b = [4, 5, 6]

# List üçün:
# print(a + b)  # [1,2,3,4,5,6]
# print(a * 2)  # [1, 2, 3, 1, 2, 3]

# NumPy üçün:
na = np.array(a)
nb = np.array(b)

print(na + nb)   # [5 7 9]
print(na * 2)    # [2 4 6]
"""

"""
np.random.rand(2, 3)
np.random.randint(0, 10, (3, 3))
a.flatten()
a.T
np.concatenate([a, b])
np.hstack((a, b))
np.vstack((a, b))

np.sum(a)
np.mean(a)
np.median(a)
np.std(a)
np.var(a)
np.min(a), np.max(a)
np.argmin(a), np.argmax(a)
np.sqrt([1, 4, 9])
np.exp([1, 2])
np.log([1, e])
np.sin(np.pi/2) (cos, tan etc.)

a[a > 5]
np.where(a > 0, 1, 0)
np.any(a > 0)
np.all(a > 0)

a.shape
a.ndim
a.size
a.dtype
a.astype(float)

np.sort([3, 1, 2])
np.unique([1, 2, 2, 3])
"""
