import time
import random
import sys


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
        print("Start game ...")
        pass
    elif options == "quit":
        print("Closing ...")
        sys.exit()


if __name__ == "__main__":
    title_screen_menu()
