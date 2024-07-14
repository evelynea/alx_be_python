class BankAccount:
    def __init__(self, account_balance: float):
        self.account_balance = account_balance
        account_balance = 0

    def deposit(self, amount):
        return self.account_balance + amount
        

    def withdraw(self, amount):
        if self.account_balance - amount > 0:
            return True  
        else:
            return False


    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

