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