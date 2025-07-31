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
    def send_amount(self, receiver, amount: int):
        self.balance -= amount
        receiver.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Balans kifayət etmir.")
        else:
            self.balance -= amount
            print(f"{self.owner} hesabından {amount} AZN çıxarıldı.")

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Faiz tətbiq olundu: {interest} AZN")

def transfer_money(acc1, acc2, amount):
    acc1.balance -= amount
    acc2.balance += amount
    print("successful")

if __name__ == '__main__':
    bank_acc = BankAccount("Huseyn", 500)
    savings_acc = SavingsAccount("Huseyn", 1000, 0.05)
    bank_acc.send_amount(savings_acc, 200)
    print("Bank", bank_acc.balance)
    print("Savings", savings_acc.balance)

    while True:
        print("\n=== Ana Menyu ===")
        print("1. BankAccount əməliyyatları")
        print("2. SavingsAccount əməliyyatları")
        print("X. Çıxış")
        choice = input("Seçiminizi daxil edin: ").strip().lower()

        if choice == '1':
            while True:
                print("\n--- BankAccount ---")
                print("1. Balansa bax")
                print("2. Balansa əlavə et")
                print("3. Balansdan çıxar")
                print("0. Ana menyuya qayıt")
                sub_choice = input("Seçiminizi daxil edin: ")

                if sub_choice == '1':
                    print(f"Bank hesabının balansı: {bank_acc.get_balance()} AZN")
                elif sub_choice == '2':
                    amount = float(input("Əlavə etmək istədiyiniz məbləği daxil edin: "))
                    bank_acc.deposit(amount)
                elif sub_choice == '3':
                    amount = float(input("Çıxarmaq istədiyiniz məbləği daxil edin: "))
                    bank_acc.withdraw(amount)
                elif sub_choice == '0':
                    break
                else:
                    print("Yanlış seçim!")

        elif choice == '2':
            while True:
                print("\n--- SavingsAccount ---")
                print("1. Balansa bax")
                print("2. Balansa əlavə et")
                print("3. Balansdan çıxar")
                print("4. Faiz tətbiq et")
                print("0. Ana menyuya qayıt")
                sub_choice = input("Seçiminizi daxil edin: ")

                if sub_choice == '1':
                    print(f"Yığım hesabının balansı: {savings_acc.get_balance()} AZN")
                elif sub_choice == '2':
                    amount = float(input("Əlavə etmək istədiyiniz məbləği daxil edin: "))
                    savings_acc.deposit(amount)
                elif sub_choice == '3':
                    amount = float(input("Çıxarmaq istədiyiniz məbləği daxil edin: "))
                    savings_acc.withdraw(amount)
                elif sub_choice == '4':
                    savings_acc.apply_interest()
                elif sub_choice == '0':
                    break
                else:
                    print("Yanlış seçim!")

        elif choice == 'x':
            print("Proqramdan çıxılır...")
            break

        else:
            print("Yanlış seçim! Yenidən cəhd edin.")