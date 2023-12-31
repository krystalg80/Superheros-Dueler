import random

class Team:
  def __init__(self, name):
        self.name = name
        self.heroes = list()

  def remove_hero(self, name):
        foundHero = False
 
        for hero in self.heroes:    
         if hero.name == name:
            self.heroes.remove(hero)
      # set our indicator to True
        foundHero = True
        if not foundHero:
            return 0
  def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # Loop over the list of heroes and print their names to the terminal one by one.
        for hero in self.heroes:
            print(hero.name)

  def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        # Add the Hero object that is passed in to the list of heroes in self.heroes
        self.heroes.append(hero)
  def stats(self):
            '''Print team statistics'''
            for hero in self.heroes:
                  kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")

  def revive_heroes(self, health=100):
        '''Reset all heroes' health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

  def attack(self, other_team):
    ''' Battle each team against each other.'''

    living_heroes = list()
    living_opponents = list()

    for hero in self.heroes:
      living_heroes.append(hero)

    for hero in other_team.heroes:
      living_opponents.append(hero)

    while len(living_heroes) > 0 and len(living_opponents)> 0:
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            # Have the heroes fight each other
            hero.fight(opponent)

            # Update the lists of living heroes and living opponents
            if hero.current_health <= 0:
                living_heroes.remove(hero)
                living_opponents.remove(opponent)
            elif opponent.current_health <= 0:
                living_heroes.remove(opponent)
                living_opponents.remove(hero)