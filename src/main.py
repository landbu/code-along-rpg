from resources import Character, Goblin
import random

def fight(fighter : list, enemies : list):
    while not len(enemies) == 0:
        fighter_target = random.choice(enemies)
        fighter_target.take_damage(fighter.attack())
        if fighter_target.get_health() == 0:
            print("Target has died")
            enemies.remove(fighter_target)
            if len(enemies) == 0: break
    print(f"Fight is over, {fighter.name} won!")


def new_fight(players: list, enemies: list):
    participants = players + enemies #slå ihop alla deltargare till en lista
    random.shuffle(participants)

    for char in participants:
        target = ""
        if char in players:
            target = random.choice(enemies)

        else:
            target = random.choice(players)


        target.take_damage(char.attack())
        if target.get_health() == 0:
            print(f"{char.get_name()} has killed {target.get_name()}!")
            if(type(target) == Goblin):
                enemies.remove(target)
            else:
                players.remove(target)
            participants.remove(target)
        else:
            print(f"{target.get_name()} was attacked by {char.get_name()}")
            print(f"{target.get_name()} has {target.get_health()} healthpoints left.")





def main():
    enemies = []
    players = []

    nick = Character("Nick", 15, 3, 1)
    emy = Character("Emy", 20, 6, 5)

    players.append(nick)
    players.append(emy)

    enemies.append(Goblin(1))
    enemies.append(Goblin(2))

    while len(enemies) != 0 and len(players) != 0:
        new_fight(players, enemies)
    if len(enemies) == 0:
        print("Players won!")
    elif len(players) == 0:
        print("Goblins won!")





    #fight(players, enemies)

main()