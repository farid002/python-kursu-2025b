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

if __name__ == '__main__':
    my_dict = {}
    my_file = open("data.txt", "r")
    lines = my_file.readlines()
    my_file.close()

    header = lines[0].strip().split(', ')

    for line in lines[1:]:
        values = line.strip().split(', ')
        my_dict[values[0]] = {header[1] : int(values[1]), header[2] : values [2]}

    print(my_dict)
