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
data_dict={}
with open('data.txt') as file :
    lines = file.readlines()
for line in lines[1:]:
    name, age, city = line.strip().split(', ')
    data_dict[name]= {
        'yash':int(age),
        'city':city

    }
print(data_dict)