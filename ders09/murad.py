from ders06.main import result

metn=input("metin daxil edin").lower()
my_dict={
    "a":2,"b":22,"c":22,"d":3,"e":33,"f":333,"g":4,"h":44,"i":444,"j":5,"k":55,"l":555,"m":6,"n":66,"o":666,"p":7,"q":77,"r":777,"s":7777,"t":8,"u":88,"v":888,"w":9,"x":99,"y":999,"z":9999," ":0
}

"""
Ali
netice: 2 555 444
"""
netice=[]
for i in metn:
    if i in my_dict.keys():
        netice.append(my_dict[i])
print(netice)



