class BankAccount:
    def __init__(self, account_balance):
        self.current_balance = account_balance
        account_balance = 0

    def deposit(self, amount):
        return self.current_balance + amount
        

    def withdraw(self, amount):
        if self.current_balance - amount > 0:
            return True  
        else:
            return False


    def display_balance(self):
        print(f"The current balance on your account is {self.current_balance}")

