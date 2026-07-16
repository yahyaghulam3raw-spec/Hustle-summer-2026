import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, self.max_damage)
        
    if __name__ == "__main__":
        ability_1 = Ability ("super_strength", 500)
        print(ability_1.name)
        print(ability_1.max_damage)