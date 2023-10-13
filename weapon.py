import random
from ability import Ability

class Weapon(Ability):
  def attack(self):
    half_damage = self.max_damage // 2
    # TODO: Use integer division to find half of the max_damage value
    # then return a random integer between half of max_damage and max_damage
    return random.randint(half_damage, self.max_damage)