class BankAccount:
    bank_name = "Kevin's bank"
    all_accounts = []
    def __init__(self,balance=0,interest_rate=0.01):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.all_accounts.append(self)
        self.account_number = len(BankAccount.all_accounts) + 100
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self,amount):
        if BankAccount.validation_balance(self.balance,amount):
            self.balance = self.balance - amount
        else:
            print("Bro, you are a brokie and there is not enough balance. As a penalty we are chargin u $5")
            self.balance = self.balance - 5
        return self
    
    def print_balance(self):
        print(f"THe account {self.account_number} has a Balance: {self.balance}")
        return self
    
    def increase_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.interest_rate
        return self
    
    def transfer_money(self,Account_destination,amount):
        val1 = BankAccount.recipient_exist(Account_destination)
        if val1>=1 and self.validation_balance(self.balance,amount):
            self.withdraw(amount)
            for tt in BankAccount.all_accounts:
                if tt.account_number == Account_destination:
                    tt.deposit(amount)
        else:
            print("The origin/destination account does not exist OR there is not enough balance ")
    
    @staticmethod ###Static method to check if the recipient exists
    def recipient_exist(recipientxc):
        vart = 0
        for tt in BankAccount.all_accounts:
            if tt.account_number == recipientxc:
                vart += 1
        return (vart)
    
    @staticmethod#########Static method to make sure the balance is not lower that the amount.
    def validation_balance(balance,amount):
        if (balance-amount) <0:
            return False
        else:
            return True
    
    @classmethod###############This will basically show all the accounts and balances
    def show_instances(cls):
        for w in cls.all_accounts:
            print(f"Cuenta #: {w.account_number}, Balance: {w.balance}, interest rate:{w.interest_rate}")