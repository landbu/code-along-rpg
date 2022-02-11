from resources import Character, Goblin
import random

def fight(fighter : Character, enemies : list):

    while not len(enemies) == 0:
        fighter_target = random.choice(enemies)
        fighter_target.take_damage(fighter.attack())
        if fighter_target.get_health() == 0:
            print("Target has died")
            enemies.remove(fighter_target)
            if len(enemies) == 0: break
        

    print(f"Fight is over, {fighter.name} won!")


def main():
    enemies = []

    nick = Character("Nick", 15, 3, 1)
    emy = Character("Emy", 20, 6, 5)

    print(nick,"\n")
    print(emy,"\n")

    enemies.append(Goblin(1))
    print(enemies[0])

    fight(emy, enemies)

main()