from classes.ninja import Ninja, Ninja2
from classes.pirate import Pirate
import random

class battlefield:
    def __init__(self):
        self.field = "Earth"
        self.m = False
        self.f = False
    def btl(self):
        jack_sparrow.show_stats()
        michelangelo.show_stats()
        battlefield.boostedninja_time()
        if michelangelo.health <=0 or jack_sparrow.health <=0:
            if self.m:
                print(f"Game over!!. The winner is {jack_sparrow.name}")
            elif self.j:
                print(f"Game over!!. The winner is {michelangelo.name}")
            return False
        else:
            x = random.randint(0, 1)
            if x == 0:
                jack_sparrow.simple_attack(michelangelo)
                self.m = battlefield.is_death(michelangelo.health,jack_sparrow.strength)
            else:
                michelangelo.simple_attack(jack_sparrow)
                self.j = battlefield.is_death(jack_sparrow.health,michelangelo.strength)
            return True
    
    def btl2(self):
        validator = True
        while validator == True:
            validator = self.btl()
    
    @classmethod
    def boostedninja_time(cls):
        Time_of_day= random.randint(0, 1)
        if Time_of_day == 1:
            michelangelo.strength = 25
            print(f"It is dusk now and {michelangelo.name} strength has been boosted to {michelangelo.strength}")
        else:
            print("It is dawn")
            michelangelo.strength = 10
    
    @staticmethod
    def is_death(health,attacke):
        if (health - attacke) < 0:
            return True
        else:
            return False
        

michelangelo = Ninja2("michelangelo")
jack_sparrow = Pirate("jack Sparrow")
x = battlefield()
x.btl2()


