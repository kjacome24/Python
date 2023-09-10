class Usuario:
    bank_name = "First national dojo bank"
    allusers = []
    def __init__(self,name,email_address):
        self.name = name
        self.email_address = email_address
        self.balance = 0
        Usuario.allusers.append(self)

    def deposit(self,amount):
        self.balance += amount
    
    def make_withdrawa(self,amountw):
        xpo = Usuario.puede_retirar(self.balance,amountw)
        if xpo:
            self.balance = self.balance - amountw
        else:
            print("U are still a brokie, so not enough balance")
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance:{self.balance}")
    
    def transfer_money(self,namet,amountt):
        xp = Usuario.puede_retirar(self.balance,amountt)
        xn = Usuario.recipient_exist(namet)
        if xp and xn >= 1:
            self.make_withdrawa(amountt)
            print(f"Transfering {amountt} from {self.name} to {namet}")
            Usuario.Transfer2(namet,amountt)
        else:
            print("Unable to transfer money, the amount requested ovepasses the current balance or the recipient does not exist")
        return self
    
    def extralogin(self):
        aopt = input("Select an option to proceed:" + '\n' "a) Balance" + '\n' + "b) make_withdrawa" + '\n' +  "c) make a dposit" + '\n' + "d) Make a tranfer" + '\n' + "e) all balances" + '\n')
        if aopt=="a":
            self.display_user_balance()
            self.extralogin()
        elif aopt=="b":
            xs = int(input("Ingrese el monto:"))
            self.make_withdrawa(xs)
            self.display_user_balance()
            self.extralogin()
        elif aopt=="c":
            xs = int(input("Ingrese el monto:"))
            self.deposit(xs)
            self.display_user_balance()
            self.extralogin()
        elif aopt=="d":
            namexx = input("Ingrese el nombre del destinatario:")
            amountss = int(input("Ingrese el monto:"))
            self.transfer_money(namexx,amountss)
            self.display_user_balance()
            self.extralogin()
        else:
            Usuario.todas_los_balances()
            self.extralogin()
    
    @classmethod
    def todas_los_balances(cls):
        yy = cls.allusers
        for w in cls.allusers:
            print(f"Usuario {w.name} = {w.balance}")
        return yy
    
    @classmethod
    def Transfer2(cls,recipient,amountw):
        for w in cls.allusers:
            if w.name == recipient:
                w.balance += amountw
    @staticmethod ###Static method
    def puede_retirar(balancel,amountl):
        if (balancel - amountl) < 0:
            return False
        else:
            return True
    @staticmethod ###Static method
    def recipient_exist(recipientxc):
        vart = 0
        for tt in Usuario.allusers:
            if tt.name == recipientxc:
                vart += 1
        return (vart)




guido = Usuario("guido","guido@python.com")
monty = Usuario("monty","monty@python.com")
kevin = Usuario("kevin","kevin@python.com")
kevin.extralogin()
