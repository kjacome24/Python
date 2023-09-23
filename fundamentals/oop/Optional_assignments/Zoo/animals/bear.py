from animals.animal import Animal

class Bear (Animal):
    def __init__(self, name, age):
        self.specie = "Tiger"
        self.happiness = 80
        self.health = 90 
        super().__init__(self.specie, name, age, self.health, self.happiness)
        self.habitat = "Mountains"
    def eatingf(self):
        self.eating()

