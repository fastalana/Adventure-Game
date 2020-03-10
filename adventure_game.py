import time
import random

villian = ['pirate', 'vampire', 'dragon', 'beast', 'monster', 'giant']
bad_guy = random.choice(villian)

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You find yourself standing in an open field.")
    print_pause("Rumor has it that a " + (bad_guy))
    print_pause(" is somewhere around here,")
    print_pause(" and has been terrifying the nearby village")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty")
    print_pause("(but not very effective) dagger.")


def house(items):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens...")
    print_pause(" and out steps a " + (bad_guy) + ".")
    print_pause("Eep! This is the " + (bad_guy) + "'s house.")
    print_pause("The " + (bad_guy) + " attacks you!")
    if "sword" in items:
        fight_or_flight(items)
    elif "dagger" in items:
        print_pause("You feel a bit under-prepared for this, ")
        print_pause("what with only having a tiny dagger.\n")
        fight_or_flight(items)


def cave(items):
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    if "sword" in items:
        print_pause("There is nothing new in the cave.")
    elif "dagger" in items:
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You find a magical sword!")
        print_pause("You discard the silly old dagger...")
        print_pause(" and take the sword with you.")
        items.append("sword")
    print_pause("You walk back to the field")
    choose(items)


def play_again(items):
    again = input("Would you like to play again? (y/n)").lower()
    if again == 'y':
        choose(items)
    elif again == 'n':
        print_pause("Thanks for playing!  Come back soon!")
    else:
        print_pause("Please enter y or n")
        play_again(items)


def fight(items):
    print_pause("You do your best... \n")
    if "sword" in items:
        print_pause("As the " + (bad_guy) + " moves to attack,")
        print_pause("...you unsheath your new sword.")
        print_pause("The magical sword shines brightly in your hand")
        print_pause("as you brace yourself for the attack.")
        print_pause("But the " + (bad_guy) + " takes one look at your shiny new toy")
        print_pause("and runs away!")
        print_pause("You have rid the town of the " + (bad_guy) + ". You are victorious!")
    elif "dagger" in items:
        print_pause("but your dagger is no match for the " + (bad_guy) + ".")
        print_pause("you have been defeated\n")
    play_again(items)


def flight(items):
    print_pause("You run back into the field.")
    print_pause("Luckily, you don't seem to have been followed.")
    choose(items, bad_guy)


def fight_or_flight(items):
    decide = input("Would you like to (1) fight or (2) run away?")
    if decide == '1':
        fight(items)
    elif decide == '2':
        flight(items)
    else:
        print_pause("Please enter 1 or 2")
        fight_or_flight(items)


def choose(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    choice = input("What would you like to do?\n")
    if choice == '1':
        house(items)
    elif choice == '2':
        cave(items)
    else:
        print_pause("Please enter 1 or 2")
        choose(items)


def play_game():
    items = ["dagger"]
    intro()
    choose(items)


play_game()
