"""
month = 5
match month:
    case 1:
        print("January")
    case 5:
        print("February")
    case _:
        print("No Match")
"""
"""
number = int(input("Bilmek istediyiniz ayin reqemini daxil edin"))

match number:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case _:
        print("No Match")
"""

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
json.load(file)
json.loads(string)
json.dump(obj, file)
json.dumps(obj)
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



"Dict"
"lambda"

"""






def print_age_kwargs(age, *args, name="No_Name", **kwargs):
    print(f"Salam {name}, sizin yash {age}")
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

age = int(input("yash 10-99 arasi"))
print_age_kwargs(age, brother_name="Miro", fax_number="+23434", father_name="Firo", phone_number="asdsad")


def print_age_args(age, *args, name="No_Name"):
    print(f"Salam {name}-{age}, sizin yash {args}")

age = int(input("yash 10-99 arasi"))
print_age_args(age,  "+23434", "asd", "sadddd", 132, 2)
"""
def multiple_by_two(x):
    return x * 2

multiple_by_two = lambda x : x * 2

my_list = [1, 2, 3]

map(multiple_by_two, )

print(list(map(lambda x: x*2, my_list)))











"kwargs"
"args"