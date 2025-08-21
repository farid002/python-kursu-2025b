"""
data.txt faylını oxuyun və məlumatları dict-də saxlayın və dict-i print edin.
Ad key, qalan melumatlar ise key: value sheklinde hemin key-in altinda olmalidir

Print edilən dict belə görünməlidir:
{
    'Farhad': {
        'yaş': 25,
        'şəhər': 'Bakı'
    },
    'Aygün': {
        'yaş': 30,
        'şəhər': 'Gəncə'
    },
    'Murad': {
        'yaş': 22,
        'şəhər': 'Sumqayıt'
    },
    'Zəhra': {
        'yaş': 28,
        'şəhər': 'Naxçıvan'
    }
}
"""
with open("data.txt", "r") as my_file:
    data_lines = my_file.readlines()

my_dict = {}
for line in data_lines:
    name, age, city = line.strip().split(",")
    my_dict[name]={"yas":int(age),"seher":city}
print(my_dict)
