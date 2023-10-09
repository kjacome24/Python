class Usuario:
    bank_name = "First national dojo bank"
    user_list = []

    def __init__(self,name,email_address):
        self.name = name
        self.email_address = email_address
        self.balance = 0
        Usuario.user_list.append(self)
    
    def deposit(self,amount):
        self.balance += amount
        return self
    
    def make_withdrawa(self,amountw):
        xpo = Usuario.puede_retirar(self.balance,amountw)
        if xpo:
            self.balance = self.balance - amountw
        else:
            print("U are still a brokie, so not enough balance")
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance:{self.balance}")
        return self
    
    def transfer_money(self,namet,amountt):
        xp = Usuario.puede_retirar(self.balance,amountt)
        xn = Usuario.recipient_exist(namet)
        if xp and xn >= 1:
            self.make_withdrawa(amountt)
            print(f"Transfering {amountt} from {self.name} to {namet}")
            Usuario.transferclass(namet,amountt)
        else:
            print("Unable to transfer money, the amount requested ovepasses the current balance or the recipient does not exist")
        return self
    
    @classmethod #####Class method
    def transferclass(cls,namer,amountr):
        for wr in cls.user_list:
            if wr.name==namer:
                wr.balance += amountr
    
    @staticmethod ###Static method
    def puede_retirar(balancel,amountl):
        if (balancel - amountl) < 0:
            return False
        else:
            return True
        
    @staticmethod ###Static method
    def recipient_exist(recipientxc):
        vart = 0
        for tt in Usuario.user_list:
            if tt.name == recipientxc:
                vart += 1
        return (vart)


guido = Usuario("guido","guido@python.com")
monty = Usuario("monty","monty@python.com")
kevin = Usuario("kevin","kevin@python.com")

guido.deposit(5000).deposit(5000).deposit(5000).make_withdrawa(7000).display_user_balance()

monty.deposit(5000).deposit(3500).make_withdrawa(2500).make_withdrawa(2500).display_user_balance()

kevin.deposit(10000).make_withdrawa(1750).make_withdrawa(1750).make_withdrawa(1750).display_user_balance()

###Bonus
print("Bonus")
guido.transfer_money("kevin",8000).display_user_balance()
kevin.display_user_balance()

