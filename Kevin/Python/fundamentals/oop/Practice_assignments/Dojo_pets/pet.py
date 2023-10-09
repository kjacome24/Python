class pet:
    def __init__(self,name,typex):
        self.name = name
        self.typex = typex
        self.health = 70
        self.energy = 70
    
    def sleep(self):
        if self.energy <= 75:
            self.energy += 25
        else:
            self.energy = 100
        print(self.energy)
        print(f"{self.name}'s energy is now {self.energy} after sleeping")
        return self
    
    def eat(self):
        if self.energy <= 95:
            self.energy += 5
        else:
            self.energy = 100
        if self.health <= 90:
            self.health += 10
        else:
            self.health = 100
        print(f"{self.name}'s health after eating is {self.health} and energy is {self.energy}")
        return self
    
    def play(self):
        if self.health <= 95:
            self.health += 5
        else:
            self.health = 100
        self.energy -= 8
        print(f"{self.name} already played and its health is now {self.health} and energy is {self.energy}")
        return self
    
    def noise(self):
        print("Grrrrrrrr")
        return self



##########Bonus Sensei

class dog(pet):
    def __init__(self, name):
        typex = "Dog"
        super().__init__(name, typex)
    def noise(self):
        print("Woooof")

class cat(pet):
    def __init__(self, name):
        typex = "Cat"
        super().__init__(name, typex)
    def noise(self):
        print("Meeewwwww")


x = cat("Meh")
print(x.typex)