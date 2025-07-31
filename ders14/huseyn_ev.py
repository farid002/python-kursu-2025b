class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner} hesabına {amount} AZN əlavə olundu.")
        else:
            print("Məbləğ sıfırdan böyük olmalıdır.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Balans kifayət etmir.")
        else:
            self.balance -= amount
            print(f"{self.owner} hesabından {amount} AZN çıxarıldı.")

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0.0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Faiz tətbiq olundu: {interest} AZN")

if __name__ == '__main__':
    bank_acc = BankAccount("Huseyn", 300)
    bank_acc.deposit(200)
    bank_acc.withdraw(100)

    print(f"Bank hesabının balansı: {bank_acc.get_balance()} AZN\n")

    savings_acc = SavingsAccount("Huseyn", 800, 0.05)
    savings_acc.deposit(200)
    print(f"Yığım hesabının faizə qədər balansı: {savings_acc.get_balance()} AZN")

    savings_acc.apply_interest()
    print(f"Yığım hesabının faizdən sonra balansı: {savings_acc.get_balance()} AZN")
