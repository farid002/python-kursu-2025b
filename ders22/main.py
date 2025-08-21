"JSON"
"""
JSON	    Python
=====       ============
object	    dict
array	    list/tuple
string	    str
number	    int/float
true/false	True/False
null	    None
"""

"""
json.dump(obj, file)
json.dumps(obj)
json.load(file)
json.loads(string)
"""

"""
import json

person = {"name": "Oghuz", "age": 25, "student": False, "aa": True}

with open("data_2.json", "w") as f:
    json.dump(person, f)

json_str = json.dumps(person)  # converts to JSON string

with open("data_2.json", "r") as f:
    my_dict = json.load(f)

"""
# Reading from file
# with open("data.json", "r") as f:
    # data = json.load(f)

# Əlavə


"""
import random
print(random.random()) # 0.0 – 1.0 arasında təsadüfi float
print(random.randint(1,10)) # 1 – 10 arasında təsadüfi integer (daxil)
print(random.uniform(5,15)) # 5 – 15 arasında təsadüfi float
"""

"""
import random
fruits = ["apple", "banana", "cherry", "date"]
print(random.choice(fruits)) # 1 təsadüfi element
print(random.sample(fruits, 2)) # 2 fərqli element (unique)
print(random.choices(fruits, k=3)) # 3 element (təkrar ola bilər)
random.shuffle(fruits) # list-i qarışdırır (yerində)
print(fruits)
"""

"""
import secrets
fruits = ["apple", "banana", "cherry", "date"]
print(secrets.choice(fruits)) # təhlükəsiz seçim (random.choice əvəzinə)
"""

"Tokenlər"
"""
import secrets
print(secrets.token_bytes(16)) # təsadüfi byte string (16 byte)
print(secrets.token_hex(16)) # hex string (32 simvol)
print(secrets.token_urlsafe(16)) # URL-də təhlükəsiz istifadə oluna bilən token
"""