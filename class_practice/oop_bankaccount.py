# A tiny "bank account" example that shows what classes are for.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner      # data stored on THIS account object
        self.balance = balance  # data stored on THIS account object

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money.")
            return False
        self.balance -= amount
        return True

    def info(self):
        print(f"{self.owner}: ${self.balance}")

a = BankAccount("Mochi", 10)   # make an account object
b = BankAccount("Kiki")        # another account object (starts at 0)

a.deposit(5)
b.deposit(20)
a.withdraw(50)                 # fails
b.withdraw(7)                  # succeeds

a.info()
b.info()
