"""
BankAccount adlı sinif yaradın və aşağıdakı atributları və metodları daxil edin:

owner (string), balance (float)
deposit(amount) – Müəyyən edilmiş məbləği balansın üzərinə əlavə edir.
withdraw(amount) – Müəyyən edilmiş məbləği balansdan çıxarır (balansın kifayət etməsini yoxlayın).
get_balance() – Cari balansı qaytarır.


BankAccount sinifindən irsiyyət alaraq SavingsAccount adlı sinif yaradın və əlavə edin:

interest_rate (float, məsələn, 0.05, yəni 5% faiz)
apply_interest() – Balans üzərinə faizi tətbiq edir (faiz, balansın interest_rate ilə vurulmasıyla hesablanır).

Kiçik bir proqram yazın ki:

Bir BankAccount instansı və bir SavingsAccount instansı yaratsın.
Hər iki hesaba məbləğ depozit və çıxarış etsin.
Yığım hesabına faiz tətbiq etsin və yenilənmiş balansı göstərin.
Məs.:Bank hesabının balansı: 500
Yığım hesabının faizə qədər balansı: 1000
Yığım hesabının faizdən sonra balansı: 1050
"""
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount >0:
            self.balance += amount
            print(f"{amount}Azn depozit edildi.Yeni balans:{self.balance}Azn")
        else:
            print("Depozit meblegi musbet olmalidir")
    def withdraw(self, amount):
        if self.balance > amount:
            print("balansda kifayet qeder mebleg yoxdur")
        elif amount < 0:
            print("cixaris meblegi musbet olmalidir")
        elif amount > 0:
            self.balance -= amount
            print(f"{amount} Azn cixarildi. Yeni balans:{self.balance}Azn")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self,owner,balance=0.0,interest_rate=0.05):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        self.balance = self.balance*self.interest_rate
        print(f"Faiz tetbiq edildi. yeni balans: {self.balance}Azn")








