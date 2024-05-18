from character import Hero, Enemy
from weapon import short_bow, iron_sword

hero = Hero(name="Hero", health=100)
enemy = Enemy(name="Villain", health=100, weapon=short_bow)
hero.equip(iron_sword)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"The health of {hero.name} is now {hero.health}")
    print(f"The health of {enemy.name} is now {enemy.health}")
    print("-=" * 40)
    print("Press enter to next move: ")

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()