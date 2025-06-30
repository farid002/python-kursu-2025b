user_num=input("4 reqemli eded daxil edin")
user_num_check=user_num.isnumeric()
a=0
while not user_num_check:
    user_num=input("4 reqemli eded daxil edin")
    user_num_check=user_num.isnumeric()
for i in str(user_num):
    a+=i
print(a)