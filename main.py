import questionary
import fire
from random import randrange
from zombie import Zombie


def run():
    money = 0
    # Welcomes the user to the game
    # print("Welcome to Adam's survival game!")
    # declares and initalizes a choice object with a string of choices for the user to chose from.
    choices = ["[Check your balance]",
               "[Go looking for gold]", "[Visit the Store]"]
    # Prompts the user with a CLI with choices and assigns that choice to the variable selection
    selection = questionary.select(
        "Choose one of the followin options.", choices).ask()

    # checks which choise the user chose
    if selection == choices[0]:
        print(f"Your balance is {money}")
    elif selection == choices[1]:
        print("You went looking for gold")
        randomNumber = randrange(0, 9)
        if randomNumber in [0, 1, 2, 3, 4, 5, 6]:
            print("You found gold")
        else:
            print("You ran into zombies o nooo")
            zombie1 = Zombie()


if __name__ == "__main__":
    fire.Fire(run)
