class Ninja:
    Charged_attack = 0
    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
    
    def simple_attack( self , pirate ):
        if self.Charged_attack == 2:
            pirate.health -= self.strength * 2
            Charged_attack = 0
            print(f"Charged attack was executed by {self.name}")
        else:
            pirate.health -= self.strength
            self.Charged_attack +=1
            print(f"simple attack was executed by {self.name}")
        return self
    
class Ninja2(Ninja):
    def __init__(self, name):
        super().__init__(name)
        self.strength = 15