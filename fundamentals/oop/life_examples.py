##OOP
#why do we use it? It allows us to be efficient and avoid being repetitive. 
#Properties== attrributes
    #trun
    #leaves
    #barches
    #roots
#behaviros == methods
    #grow
    #prouce leaves

###Classes (Firs letter should be captilar and the name should be singular)
class User:
    ##declaring a class atribitue
    nombre_banco = "Primer Dojo Nacional"
    #declaring construtor atribute
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance = 0

guido = User()
monty = User()

guido.name = "Guido"
monty.name = "Monty"
monty.nombre_banco = "Kevin's bank"

print(guido.nombre_banco)
print(monty.nombre_banco)
print(guido.name)

########Creacion de ususarios

class Usuario:
    bank_name = "First national dojo bank"
    def __init__(self,name,email_address):
        self.name = name
        self.email_address = email_address
        self.balance = 0
    def deposit(self):
        x = input()
        self.balance += int(x)

guido = Usuario("guido","guido@python.com")
monty = Usuario("monty","monty@python.com")

guido.credit_card()

###########adding function deposit

class Usuario:
    bank_name = "First national dojo bank"
    def __init__(self,name,email_address):
        self.name = name
        self.email_address = email_address
        self.balance = 0
    def deposit(self):
        print("Por favor ingrese el valor a depositar:")
        x = input()
        self.balance += int(x)

guido = Usuario("guido","guido@python.com")
monty = Usuario("monty","monty@python.com")

guido.deposit()
print(guido.balance)
print(monty.balance)