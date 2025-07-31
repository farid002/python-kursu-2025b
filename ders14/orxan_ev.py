class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"hesabdan-{amount}yatirildi")
    def withdraw(self,amount):
        self.balance-=amount
        print(f"hesabdan-{amount}cixarildi")
    def get_balance(self):
        return self.balance
class SavingAccount(BankAccount):
    def __init__(self,owner,balance=0,interest_rate=0.05):
        self.interest_rate=interest_rate
        super().__init__(owner,balance)
    def apply_interest(self):
        faiz=self.balance*self.interest_rate
        self.balance+=faiz
        print(f"hesaba faizden-{faiz}elave edildi")

if __name__=="__main__":
    bank_hesabi=BankAccount("orxan",0)
    bank_hesabi.deposit(500)
    bank_hesabi.withdraw(100)
    print(bank_hesabi.get_balance())

    qiragdaki_pul=SavingAccount("murad",0,0.05)
    qiragdaki_pul.deposit(500)
    qiragdaki_pul.withdraw(100)
    qiragdaki_pul.apply_interest()
    print(qiragdaki_pul.get_balance())
