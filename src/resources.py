class Character:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor


    def __str__(self) -> str:
        return f"Name : {self.name}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}"

    def take_damage(self, dmg):
            actual_damage = dmg - self.armor
            if (self.health - actual_damage) < self.health: self.health = 0
            else: self.health -= actual_damage

    def attack(self):
        return self.damage
    
class Goblin:

    def __init__(self, id):
        self.id = id
        self.health = 10
        self.damage = 3
        self.armor = 2

    def take_damage(self, dmg):
        actual_damage = dmg - self.armor
        if (self.health - actual_damage) < self.health: self.health = 0
        else: self.health -= actual_damage



    def __str__(self) -> str:
        return f"Goblin Id : {self.id}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}"
    
    def attack(self):
        return self.damage

    def get_health(self):
        return self.health