class BankAccount:
    def __init__(self, account_balance,bank_account):
        self.account_balance = account_balance
        self.bank_account = 0
    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
    def withdraw(self, amount):
        if amount > self.account_balance:
            return "Insufficient funds."
        self.account_balance -= amount
        return self.account_balance
    def display_balance(self):
        return self.account_balance