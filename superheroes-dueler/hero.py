import random

from opponent import Opponent
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.armors = list()
        self.abilities = list()

    def add_ability(self, ability):
         self.abilities.append(ability)
    def add_armor(self, armor):
         self.armors.append(armor)

    def defend(self):
         # start our total out at 0
        total_block = 0
        # loop through all of our hero's abilities
        for armor in self.armors:
        # add the damage of each attack to our running total
                total_block += armor.block()
        # return the total damage
        return total_block

    def attack(self):
          # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
        # add the damage of each attack to our running total
                total_damage += ability.attack()
        # return the total damage
        return total_damage
    
    # def take_damage(self, damage):
    
   
    def fight(self, opponent): #no init bc not an object  
        outcome = ['wins','loses','draw']
        result = random.choice(outcome)
        print(f"{self.name} {result} against {opponent.name}")

    # def fight(name, opponent, opponent2):
        
   
# def fight(name_list):
#          return random.choice(name_list)
        
   
     
    

if __name__ == "__main__":
        my_hero = Hero("Mrs Dream",200)
        print ("Introducing our hero...", my_hero.name)
        print ("She currently has a health of", my_hero.starting_health)
    
        opponent = Opponent("Wonder Woman",200)
        print("our fight today will be between...", my_hero.name, "vs", opponent.name)
        my_hero.fight(opponent)
        
        armor = Armor("Bubblegum Shield",20)
        another_armor = Armor("Steel Shield",50)
        ability = Ability("Great Debugging", 50)
        another_ability = Ability("Super Smash",20)
        hero = Hero("Grace Hopper", 200)
        hero.add_ability(ability)
        hero.add_ability(another_ability)
        hero.add_armor(armor)
        hero.add_armor(another_armor)
        print(hero.attack())
        print(hero.defend())
        
        
        
        # hero2 = Hero("Dumbledore")

        # name_list = (hero1.name, hero2.name, my_hero.name)
        
        # print("Our fight of today will be between...", my_hero.name,"vs", hero1.name, "vs", hero2.name)
        # print(".....")
        # print("many hours of battling later")
        # print(".....")
        # print("Our winner of the fight is....",fight(name_list),"!!!!!!")

# print(fight(name_list))






