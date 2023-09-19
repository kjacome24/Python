# from animal import Animal
class Animal:
    def __init__(self,specie,name,age,health,happiness):
        self.specie = specie
        self.name = name
        self.age = age 
        self.health = health
        self.happiness = happiness
        self.aggressiveness = "Medium"
        self.habitat = None
    
    def print_info(self):
        print(f"Name: {self.name}\nHealth: {self.health}\nHappiness:{self.happiness}\nAggressiveness: {self.aggressiveness}")
    
    def eating(self):
        if self.health > 90:
            self.health = 100
        else:
            self.health +=  10
        if self.happiness > 90:
            self.happiness = 100
        else:
            self.happiness += 10


class Tiger(Animal):
    def __init__(self, name, age):
        self.specie = "Tiger"
        self.happiness = 60
        self.health = 80 
        super().__init__(self.specie, name, age, self.health, self.happiness)
        self.aggressiveness = "High"
        self.habitat = "Rain forests"
    def eatingf(self):
        self.eating()
        if self.happiness == 100:
            self.aggressiveness = "Medium"

