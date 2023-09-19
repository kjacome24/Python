from animals.lion import Lion
from animals.tiger import Tiger
from animals.bear import Bear

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def agregar_león(self, name):
        self.animals.append( Lion(name,20) )
    def agregar_tigre(self, name):
        self.animals.append( Tiger(name,20) )
    def imprimir_toda_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.print_info()
zoo1 = Zoo("El zoo de John")
zoo1.agregar_león("Nala")
zoo1.agregar_león("Simba")
zoo1.agregar_tigre("Rajah")
zoo1.agregar_tigre("Shere Khan")
zoo1.imprimir_toda_info()