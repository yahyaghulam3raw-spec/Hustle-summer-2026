import random
from ability import Ability
from armor import Armor


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def add_armor(self, armor):
        self.armors.append(armor)
    
    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block


    def battle(self, opponent):
        print(random.choice([self.name, opponent.name]))


 

if __name__ == "__main__":
    my_hero = Hero("Venom", 150)
    print(my_hero.name)
    print(my_hero.current_health)
    my_opponent = Hero("Spider_man", 999)
    my_hero.battle(my_opponent)

    my_hero.add_ability(Ability("Fire", 80))
    print("Attack damage:", my_hero.attack())

    my_hero.add_armor(Armor("Shield", 30))
    print("Defend amount", my_hero.defend())