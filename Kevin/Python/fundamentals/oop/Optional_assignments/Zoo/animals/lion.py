from animals.animal import Animal

class Lion(Animal):
    def __init__(self, name, age):
        self.specie = "Lion"
        self.happiness = 70
        self.health = 60 
        super().__init__(self.specie, name, age, self.health, self.happiness)
        self.aggressiveness = "High"
        self.habitat = "Thorn forest"
    
    def eatingf(self):
        self.eating()
        if self.happiness == 100:
            self.aggressiveness = "Low"

