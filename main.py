import time
import random
import sys


class Player():
    def __init__(self):
        self.name = ""
        self.hp = 10
        self.dmg = 3


class Goblin():
    def __init__(self, hp=0, dmg=0):
        self.name = "Goblin"
        self.hp = hp
        self.dmg = dmg


def title_screen_menu():
    print("################")
    print("##  Welcome  ###")
    print("################")
    print("#              #")
    print("#   - play -   #")
    print("#   - quit -   #")
    print("#              #")
    print("################")

    # Main menu
    options = True
    while options != "play" and options != "quit":
        options = input("> ")

    if options == "play":
        return

    elif options == "quit":
        print("Closing ...")
        sys.exit()

def set_name():
    player_name = ""
    while player_name == "":
        print("What's your name?")
        player_name = input("> ")
    setattr(player, "name", player_name)


def fight(enemy):
    player_hp = getattr(player, "hp")
    player_dmg = getattr(player, "dmg")
    enemy_name = getattr(enemy, "name")
    enemy_hp = getattr(enemy, "hp")
    enemy_dmg = getattr(enemy, "dmg")

    while player_hp > 0 or enemy_hp > 0:
        print()
        print("Your HP:", player_hp)
        print("Enemy HP:", enemy_hp)
        print("Do you want to attack? (yes/no)")
        choice = ""
        while choice != "yes" and choice != "no":
            choice = input("> ")

        if choice == "yes":
            enemy_hp = enemy_hp - player_dmg
            print("You hit", enemy_name, "and did", player_dmg, "damage!")

            player_hp = player_hp - enemy_dmg
            print("You've got hit and took", enemy_dmg, "damage!")

            if enemy_hp <= 0:
                print("You've won!", enemy_name, "died.")
                return True

            elif player_hp <= 0:
                print("You've lost to", enemy_name, ".")
                return False

        else:
            print("You ran away like a little bitch.")
            return False

def scene1_intro():
    print()
    print("You open your eyes ...")
    time.sleep(2)
    print("You hear someone talking: ")
    time.sleep(0.5)
    print("\"Ah... you're finally awake.\"")
    time.sleep(0.5)
    print("But it's only the voice in your head.")
    print()
    scene1()

def scene1():
    while True:
        print("You are in a room with 2 doors.")
        print("Which door should you open? (1 or 2)")
        door = ""
        while door != "1" and door != "2":
            door = input("> ")
        if door == "1":
            scene1_1()
        else:
            print("There is a sign that says \"DO NOT ENTER\"")
            print("Do you really want to enter? This room is buggy as shit.")
            choice = ""
            while choice != "yes" and choice != "no":
                input("> ")
            if choice == "yes":
                print("Okay. Not my problem.")
                scene1_2()
            else:
                print("Wise choice.")


def scene1_1():
    print("You see a GOBLIN!")
    print("Do you want to FIGHT or RUN?")
    choice = ""
    while choice != "fight" and choice != "run":
        choice = input("> ")
    if choice == "run":
        print("You ran away like a little coward.")
        title_screen_menu()
    else:
        goblin = Goblin(5, 2)
        if fight(goblin) == True:
            return
        else:
            print("Want to try again? (yes/no)")
            choice = ""
            while choice!="yes" and choice!="no":
                choice = input("> ")
            if choice == "yes":
                scene1_1()
            else:
                title_screen_menu()


def scene1_2():
    while True:
        print("You are in a room.")
        print("It's empty.")
        time.sleep(1)
        print("Do you want to go back? (yes/no)")
        choice = ""
        while choice!= "yes" and choice!="no":
            choice = input("> ")
        if choice == "yes":
            scene1()
        else:
            scene1_2()


if __name__ == "__main__":
    title_screen_menu()
    player = Player()
    set_name()
    print("Welcome", getattr(player, "name") + ".")
    scene1_intro()
