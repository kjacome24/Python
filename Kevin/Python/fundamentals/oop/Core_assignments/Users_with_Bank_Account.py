class User:
    bank_name = "First national dojo bank"
    user_list = []
    def __init__(self,name, email):
        self.name = name
        self.email = email 
        # self.account = BankAccount(balance=0,interest_rate=0.02)
        self.account = [BankAccount(balance=0,interest_rate=0.02)] #This is setting the stage about the variable account being a list and the original account[0]
        User.user_list.append(self)
    
    def creationofaccount(self,balance=0,interest_rate=0):##By defoult when u create a user a bank account will be created but u can also add more: 
        self.account.append(BankAccount(balance=0,interest_rate=0.02))
        return self
    
    def checkyouraccounts(self): #############This code will basically helps u to know which accounts do u have.
        print(f"You have {len(self.account)} accounts:")
        for c in range (0,len(self.account)):
            print(f"{c} . {self.account[c].account_number}")
        return self
    
    def deposit(self,amount,cuenta=0):
        self.account[cuenta].balance += amount
        return self
    
    def make_withdrawa(self,amountw,cuenta=0):
        self.account[cuenta].withdraw(amountw)
        return self
    
    def display_user_balance(self,cuenta=0):
        self.account[cuenta].print_balance()
        return self
    
    def transfer_m(self,destination,amount,cuenta_origin=0):
        self.account[cuenta_origin].transfer_money(destination,amount)
        return self
    
    def show_info(self,cuenta=0):
        print("Your information is listed below:" + '\n' + f"Name: {self.name}"+ '\n' +f"Email Address: {self.email}"+ '\n' +f"Balance: {self.account[cuenta].balance}"+ '\n' +f"Interst rate:{self.account[cuenta].interest_rate}")
        return self
    



#####################################BankAccount class
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

guido = User("guido","guido@python.com")
monty = User("monty","monty@python.com")
kevin = User("kevin","kevin@python.com")
Artur = User("Artur","Artur@python.com")

guido.deposit(1000).deposit(900).deposit(88).make_withdrawa(1000).transfer_m(104,100)
monty.deposit(700).make_withdrawa(305).make_withdrawa(100).make_withdrawa(100).make_withdrawa(100).make_withdrawa(100)


###############By defoult when u create a user a bank account will be created but u can also add more: 
guido.creationofaccount()


###############
BankAccount.show_instances()

############If you want to use another account an not the one by default 1. check your accounts.
guido.checkyouraccounts() ###The left column will tell u the orgin number.
#2. To use functions like debit, withdraw and the other ones, please add the orgin number at the end. 
guido.deposit(100,1)
guido.make_withdrawa(50,1)
BankAccount.show_instances()


