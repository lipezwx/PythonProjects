from weapon import Weapon, fists
from health_bar import HealthBar

class Character:
    char_class = "Wizard"


    def __init__(self,name : str, health: int,):
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = fists
        self.default_weapon = Weapon
        

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} Caused {self.weapon.damage} damage to {target.name} with {self.weapon.name}")
        print("-=" * 40)

class Hero(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name= name, health= health)

        self.health_bar = HealthBar(self, color="green")


    def equip(self, weapon):
        self.weapon = weapon
        print(f"The weapon equipped is actually a: {self.weapon.name}")

    def drop(self) -> None:
        self.weapon = self.default_weapon
        print(f"{self.name} dropped the {self.weapon.name}!")

class Enemy(Character):
    def __init__(self, name: str, health: int, weapon,) -> None:
        super().__init__(name= name, health= health)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color="red")