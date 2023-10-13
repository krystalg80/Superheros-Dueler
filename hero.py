import random

# from opponent import Opponent


from weapon import Weapon
from ability import Ability
from armor import Armor
from team import Team

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.armors = list()
        self.abilities = list()
        self.deaths = 0
        self.kills = 0


    def add_ability(self, ability):
         self.abilities.append(ability)
    def add_armor(self, armor):
         self.armors.append(armor)
    def add_weapon(self, weapon):
         self.abilities.append(weapon)

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
        
    
    def take_damage(self, damage):
        defense = self.defend()
        damage -= defense
        self.current_health -= damage
    
    def has_abilities(self):
        return len(self.abilities) > 0
    
    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
         self.deaths += num_deaths
         pass
   
    def is_alive(self):
         return self.current_health > 0


    def fight(self, opponent): 
        if not (self.has_abilities() or opponent.has_abilities()):
            print("Draw")
            return
        
        while self.is_alive() and opponent.is_alive():
            # Step 2: The hero (self) and their opponent must attack each other
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())


            if self.is_alive():
                self.kills += 1
                opponent.deaths += 1
                
        
            else:
               opponent.kills += 1
               self.deaths += 1

            # if self.is_alive():
            #     print(f"{opponent.name} won!")
            #     return
            # elif opponent.is_alive():
            #     print(f"{self.name} won!")
            #     return
        #no init bc not an object  
        # outcome = ['wins','loses','draw']
        # result = random.choice(outcome)
        # print(f"{self.name} {result} against {opponent.name}")


if __name__ == "__main__":
        my_hero = Hero("Mrs Dream",200)
        print ("Introducing our hero...", my_hero.name)
        print ("She currently has a health of", my_hero.starting_health)
    
       
        
        
        hero1 = Hero("Wonder Woman",200)
        hero2 = Hero("Dumbledore",200)
        ability1 = Ability("Super Speed", 300)
        ability2 = Ability("Super Eyes", 130)
        ability3 = Ability("Wizard Wand", 80)
        ability4 = Ability("Wizard Beard", 20)
        weapon = Weapon("Lasso of Truth", 90)
        hero1.add_ability(ability1)
        hero1.add_ability(ability2)
        hero2.add_ability(ability3)
        hero2.add_ability(ability4)
        hero1.add_weapon(weapon)
        hero2.add_weapon(weapon)

        print("our fight today will be between...", hero1.name, "vs", hero2.name)
        
        hero1.fight(hero2)
            

        print(f"{hero1.name}: Kills={hero1.kills}, Deaths={hero1.deaths}")
        print(f"{hero2.name}: Kills={hero2.kills}, Deaths={hero2.deaths}")  
        
        
        
        
        
        # armor = Armor("Bubblegum Shield",20)
        # another_armor = Armor("Steel Shield",50)
        # ability = Ability("Great Debugging", 50)
        # another_ability = Ability("Super Smash",20)
        # hero = Hero("Grace Hopper", 200)
        # hero.add_ability(ability)
        # hero.add_ability(another_ability)
        # hero.add_armor(armor)
        # hero.add_armor(another_armor)
        # hero.take_damage(50)
        # print(hero.attack())
        # print(hero.defend())
        # print(hero.current_health)
        # print(hero.is_alive())
        
        
        
        # hero2 = Hero("Dumbledore")

        # name_list = (hero1.name, hero2.name, my_hero.name)
        
        # print("Our fight of today will be between...", my_hero.name,"vs", hero1.name, "vs", hero2.name)
        # print(".....")
        # print("many hours of battling later")
        # print(".....")
        # print("Our winner of the fight is....",fight(name_list),"!!!!!!")

# print(fight(name_list))






