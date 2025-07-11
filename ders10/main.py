"""
-----------------------------------FUNKSİYALAR------------------------------------
def açar sözü
"""


"""
Parametrlər
Defolt dəyər
"""

"""
return açar sözü
çoxsaylı return dəyəri
"""

"""
*args - tuple kimi davranış
**kwargs - dict kimi davranış
"""

"""-----------------------args - bir ulduz - list kimi davranir-------------------------"""
def sum_of_numbers(*args):
    return sum(args)

"""----------------------kwargs - iki ulduz - dict kimi davranir------------------------"""
def return_sum(a, b, **kwargs):
    return a + b, kwargs

"""
main funksiyası
"""

"""----------------------lambda funksiyaları (ananonim funksiyalar)--------------------------"""
"""
my_func = lambda b,c: b*c
my_func(1, 2)
"""

"""
global dəyişkənlər
"""