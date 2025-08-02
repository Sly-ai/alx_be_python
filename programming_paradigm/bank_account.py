class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False
    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")
            return True
        else:
            print(f"Attempted withdrawal of ${amount}. Current balance: ${self.account_balance:.2f}")
            return False
    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")
