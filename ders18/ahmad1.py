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
my_dict = {}
with open("data.txt", "r") as my_file:
    data_list = my_file.readlines()
    for line in data_list[1:]:
        ad = line.split(", ")[0].strip()
        yash = line.split(", ")[1].strip()
        yer = line.split(", ")[2].strip()
        my_dict[ad]={
            'yaş': int(yash),
            'şəhər': yer
        }
    print(my_dict)