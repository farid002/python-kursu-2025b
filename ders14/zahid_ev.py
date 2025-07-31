class BankAccount:
    def __init__(self,owner=str,balance=float):
        self.owner=owner
        self.balance=balance
    def withdraw(self,amount):
        if amount>=self.balance:
            print("Verdiyiniz miqdar balansdan boyukdur")
        else:
            self.balance-=amount
    def get_balance(self):
        return self.balance
class SavingsAccount(BankAccount):
    def __init__(self,owner, balance,interest_rate=0.05):  #mesel olaraq 5% verilib amma bankdan banka deyisdiyi ucun bele yazdim
        self.interest_rate=interest_rate
        super().__init__(owner, balance)                   #superin yazilisna kecen dersden baxib yazdim, helede yazilisi casdirici gelir biraz
    def apply_rate(self):
        self.balance+=(self.balance*self.interest_rate)
if __name__=="__main__":
    bank_zahid=BankAccount("Zahid",500)
    bank_zahid.withdraw(10)
    print(bank_zahid.get_balance())
    saving_account_zahid=SavingsAccount("Zahid",1000)
    print(saving_account_zahid.get_balance())
    saving_account_zahid.apply_rate()
    print(saving_account_zahid.get_balance())
