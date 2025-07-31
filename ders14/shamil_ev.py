class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} AZN depozit edildi.")
        else:
            print("Depozit məbləgi musbet olmalıdır.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Balansda kifayet qeder vesait yoxdu.")
        elif amount <= 0:
            print("Cixarilacaq mebleg musbət olmalıdır.")
        else:
            self.balance -= amount
            print(f"{amount} AZN cixarildi.")

    def get_balance(self):
        return self.balance



class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0.0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Faiz tetbiq edildi: {interest} AZN")


if __name__=="__main__":
    bank_account = BankAccount("Ali", 300)
    bank_account.deposit(200)        # balans: 500
    bank_account.withdraw(100)       # balans: 400
    print(f"Bank hesabinin balansi: {bank_account.get_balance()} AZN")

    print()


    savings_account = SavingsAccount("Aysel", 800, 0.05)
    savings_account.deposit(200)     # balans: 1000
    savings_account.withdraw(50)     # balans: 950
    print(f"Yigim hesabinin faize qeder balansi: {savings_account.get_balance()} AZN")
    savings_account.apply_interest() # faiz tətbiqi
    print(f"Yigimm hesabinin faizden sonra balansi: {savings_account.get_balance()} AZN")
