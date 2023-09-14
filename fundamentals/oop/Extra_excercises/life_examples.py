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
from typing import Any


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


##############Encapsulation

class CaféM:
    def __init__(self,name):
        self.name = name
        self.temp_agua = 200
    def preparar_ahora(self,granos):
        print(f"Utilizando {granos}!")
        print("¡Preparar ahora, vaca café!")
    def limpiar(self):
        print("¡Limpiando!")

# x = CaféM("Americano")
# print(x.name,x.temp_agua)
# x.preparar_ahora("Arabica")
class CappuccinoM( CaféM ):##########Inheritance & Poliformis
    def __init__(self,name):
        super().__init__(name)##########Inheritance
        self.leche = "entera"
    def hacer_cappuccino(self,granos):
        super().preparar_ahora(granos)
        print("¡Espumoso!")
    def limpiar(self):###Poliformis
        print("¡Limpiando la espuma")

parent = CaféM("Americano")
hijo = CappuccinoM("Americano")

# y.hacer_cappuccino("Arabica")
parent.limpiar()
hijo.limpiar()
print(y.temp_agua)

class Barista: #########Abstraction
    def __init__(self,name):
        self.__name = name ###Private attrb
        self.café = CaféM("Café")
    def hacer_café(self, granos):
        self.café.preparar_ahora(granos)
    def getname(self):
        return "Mi nombre es: " + self.__name####Variable is not gonna be available, just the fucntion. 
    def setname(self,name2):
        self.__name = name2


class barista2(Barista):
    def __init__(self,name):
        super().__init__(name)
        self.baristao = Barista(name)
    def printx(self):
        print(super().getname())

x = barista2("Kevin")

x.printx()

class Persona:
    def pagar_cuenta(self):
        raise NotImplementedError
# Millonario hereda de Persona
class Millonario(Persona):
    def pagar_cuenta(self):
        print("Aquí tienes. Quédate con el cambio.")
# Estudiante de posgrado también hereda de la clase Persona
class EstudiantePosgrado(Persona):
    def pagar_cuenta(self):
        print("¿Puedo deberle diez dólares o lavar los platos?")


x = Persona()
y = Millonario()
y.pagar_cuenta()