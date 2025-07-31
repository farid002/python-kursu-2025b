

class BankAcc:
    def __init__(self, ad:str, mail, accnum:float, ballance):
        self.name = ad
        self.mail = mail
        self.accnum = accnum
        self.ballance = ballance

    def pul_yatir(self, mebleg):
        self.ballance+=mebleg
    def pul_cixar(self, money):
        self.ballance-=money
    def balans_goster(self):
        print(self.ballance)
    def tam_mellumat(self):
        print(self.name, self.mail, self.accnum, self.ballance)

if __name__=="__main__":
    muellimin_pulu = BankAcc("Farid", "faridhuseyinov@gmail.com", 1212332, 10000)
    muellimin_pulu.pul_cixar(100)
    muellimin_pulu.balans_goster()
    muellimin_pulu.tam_mellumat()
