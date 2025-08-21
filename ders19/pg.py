taxta=[["7", "8", "9"],      ["4", "5", "6"],      ["1", "2", "3"]] #Notbukumda sagdaki numpada uygun qurdum
result=[["", "", ""],      ["", "", ""],      ["", "", ""]]
def taxta_gostermek():
    print(taxta[0])
    print(taxta[1])
    print(taxta[2])
    print("---------------")
    print(result[0])
    print(result[1])
    print(result[2])
taxta_gostermek()
def reset_taxta():
    global taxta,result
    taxta = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]]
    result = [["", "", ""], ["", "", ""], ["", "", ""]]
    taxta_gostermek()
def udani_yoxlamaq():
    if result[0][0]=="X" and result[0][1]=="X" and result[0][2]=="X": #EN
        print("X uddu")
        reset_taxta()
    if result[1][0]=="X" and result[1][1]=="X" and result[1][2]=="X": #EN
        print("X uddu")
        reset_taxta()
    if result[2][0]=="X" and result[2][1]=="X" and result[2][2]=="X": #EN
        print("X uddu")
        reset_taxta()
    if result[0][0]=="X" and result[1][0]=="X" and result[2][0]=="X": #UZUN
        print("X uddu")
        reset_taxta()
    if result[0][1]=="X" and result[1][1]=="X" and result[2][1]=="X": #UZUN
        print("X uddu")
        reset_taxta()
    if result[0][2]=="X" and result[1][2]=="X" and result[2][2]=="X": #UZUN
        print("X uddu")
        reset_taxta()
    if result[0][0]=="X" and result[1][1]=="X" and result[2][2]=="X": #EYRI
        print("X uddu")
        reset_taxta()
    if result[0][2]=="X" and result[1][1]=="X" and result[2][1]=="X": #EYRI
        print("X uddu")
        reset_taxta()
        #----------------------
    if result[0][0] == "O" and result[0][1] == "O" and result[0][2] == "O": #EN
        print("O uddu")
        reset_taxta()
    if result[1][0] == "O" and result[1][1] == "O" and result[1][2] == "O": #EN
        print("O uddu")
        reset_taxta()
    if result[2][0] == "O" and result[2][1] == "O" and result[2][2] == "O": #EN
        print("O uddu")
        reset_taxta()
    if result[0][0] == "O" and result[1][0] == "O" and result[2][0] == "O": #UZUN
        print("O uddu")
        reset_taxta()
    if result[0][1] == "O" and result[1][1] == "O" and result[2][1] == "O": #UZUN
        print("O uddu")
        reset_taxta()
    if result[0][2] == "O" and result[1][2] == "O" and result[2][2] == "O": #UZUN
        print("O uddu")
        reset_taxta()
    if result[0][0] == "O" and result[1][1] == "O" and result[2][2] == "O": #EYRI
        print("O uddu")
        reset_taxta()
    if result[0][2] == "O" and result[1][1] == "O" and result[2][1] == "O": #EYRI
        print("O uddu")
        reset_taxta()
while True:
    while True:
        user_x=input("Sira X-da\nUstdeki taxtadan secmek istediyiniz yerin reqemini yazib enter basin")
        for i in taxta:
            for e in i:
                if user_x==e:
                    if e=="-":
                        continue
                    index=i.index(e)
                    index2=taxta.index(i)
                    i[index]="-"
        if result[index2][index]=="O" or result[index2][index]=="X":
            continue
        else:
            result[index2][index]="X"
            break
    taxta_gostermek()
    udani_yoxlamaq()
    while True:
        user_o = input("Sira O-da\nUstdeki taxtadan secmek istediyiniz yerin reqemini yazib enter basin")
        for i in taxta:
            for e in i:
                if user_o == e:
                    if e=="-":
                        continue
                    index = i.index(e)
                    index2 = taxta.index(i)
                    i[index] = "-"
        if result[index2][index]=="O" or result[index2][index]=="X":
            continue
        else:
            result[index2][index]="O"
            break
    udani_yoxlamaq()
    taxta_gostermek()