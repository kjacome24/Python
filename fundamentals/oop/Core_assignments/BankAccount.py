class BankAccount:
    bank_name = "Kevin's bank"
    all_accounts = []

    def __init__(self,balance=0,interest_rate=0.01):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.all_accounts.append(self)
        self.account_number = len(BankAccount.all_accounts)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self,amount):
        if BankAccount.validation_balance(self.balance,amount):
            self.balance = self.balance - amount
        else:
            print("Bro, you are a brokie and there is no balance. As a penalty we are chargin u $5")
            self.balance = self.balance - 5
        return self

    def print_balance(self):
        print(f"Balance: {self.balance}")
        return self
    
    def increase_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.interest_rate
        return self
    
    @staticmethod
    def validation_balance(balance,amount):
        if (balance-amount) <0:
            return False
        else:
            return True
    
    @classmethod
    def show_instances(cls):
        for w in cls.all_accounts:
            print(f"Cuenta #: {w.account_number}, Balance: {w.balance}, interest rate:{w.interest_rate}")

x = BankAccount()
y = BankAccount()


x.deposit(1000).deposit(900).deposit(88).withdraw(1000).increase_interest().print_balance()
y.deposit(700).deposit(300).withdraw(100).withdraw(100).withdraw(100).withdraw(100).increase_interest().print_balance()

BankAccount.show_instances()