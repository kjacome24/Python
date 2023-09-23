from animals.animal import Animal

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

