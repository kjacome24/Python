class Usuario:
    bank_name = "First national dojo bank"

    def __init__(self,name,email_address):
        self.name = name
        self.email_address = email_address
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount
        return self
    def make_withdrawa(self,amountw):
        self.balance = self.balance - amountw
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance:{self.balance}")
        return self
    def transfer_money(self,namet,amountt):
        self.make_withdrawa(amountt)
        print(f"Transfering {amountt} from {self.name} to {namet}")
        if namet=="guido":
            guido.deposit(amountt)
        elif namet=="monty":
            monty.deposit(amountt)
        else:
            kevin.deposit(amountt)
        return self

guido = Usuario("guido","guido@python.com")
monty = Usuario("monty","monty@python.com")
kevin = Usuario("kevin","kevin@python.com")

guido.deposit(5000).deposit(5000).deposit(5000).make_withdrawa(7000).display_user_balance()

monty.deposit(5000).deposit(3500).make_withdrawa(2500).make_withdrawa(2500).display_user_balance()

kevin.deposit(10000).make_withdrawa(1750).make_withdrawa(1750).make_withdrawa(1750).display_user_balance()

###Bonus
print("Bonus")
guido.transfer_money("kevin",3000)
guido.display_user_balance()
kevin.display_user_balance()