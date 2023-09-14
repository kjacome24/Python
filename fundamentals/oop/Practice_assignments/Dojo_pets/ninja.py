import pet
class ninja:
    def __init__(self,first_name,last_name,rewards,pet_food,pet):
        self.first_name = first_name
        self.last_name = last_name
        self.rewards = rewards
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        print(f"Taking {self.pet.name} out for a walk")
        self.pet.play()
        print("------------------------------")
        return self
    
    def feed(self):
        print(f"Feeding Mr.{self.pet.name} with {self.pet_food} ")
        self.pet.eat()
        print("------------------------------")
        return self
    
    def shower(self):
        print(f"Showering Mr.{self.pet.name} and does seem happy")
        self.pet.noise()
        print("------------------------------")
        return self
    
x = ninja("Kevin","Jacome","bones","chiecken legs",pet.pet("firulais"))

x.walk()
x.feed()
x.shower()
