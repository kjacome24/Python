class Usuario:
    bank_name = "First national dojo bank"

    def __init__(self,name,email_address):
        self.name = name
        self.email_address = email_address
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount
    
    def make_withdrawa(self,amountw):
        self.balance = self.balance - amountw
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance:{self.balance}")
    
    def transfer_money(self,namet,amountt):
        self.make_withdrawa(amountt)
        print(f"Transferin {amountt} from {self.name} to {namet}")
        if namet=="guido":
            guido.deposit(amountt)
        elif namet=="monty":
            monty.deposit(amountt)
        else:
            kevin.deposit(amountt)
        # self.deposit(amountt)
        # self.name = namet
        # print(self.name)
        # self.deposit(amountt)

guido = Usuario("guido","guido@python.com")
monty = Usuario("monty","monty@python.com")
kevin = Usuario("kevin","kevin@python.com")

guido.deposit(5000)
guido.deposit(5000)
guido.deposit(5000)
guido.make_withdrawa(7000)
guido.display_user_balance()

monty.deposit(5000)
monty.deposit(3500)
monty.make_withdrawa(2500)
monty.make_withdrawa(2500)
monty.display_user_balance()

kevin.deposit(10000)
kevin.make_withdrawa(1750)
kevin.make_withdrawa(1750)
kevin.make_withdrawa(1750)
kevin.display_user_balance()

print("-----------------------------------")

monty.transfer_money("kevin",3000)
kevin.display_user_balance()
guido.display_user_balance()
monty.display_user_balance()

