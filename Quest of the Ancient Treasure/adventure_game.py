def introduction():
    # Welcome message for the player, setting the stage for the adventure.
    print("Welcome, brave adventurer, to the Quest of the Ancient Treasure!")
    print("You stand at the entrance of the dark cave that is rumored to hold the lost treasure of the ancients.")
    # Loop until a valid input is received.
    while True:
        choice = input("Do you enter the cave? (yes/no): ").strip().lower()
        if choice == "yes":
            main_cave()
            break  # Break the loop if the choice leads to progression.
        elif choice == "no":
            print("You decide not to enter the cave. Perhaps another adventure awaits you. Game Over.")
            play_again()
            break  # End the game or restart based on player's choice.
        else:
            print("Please enter a valid choice (yes/no).")  # Prompt for valid input.

def main_cave():
    # Describes the crossroads inside the cave, offering choices to the player.
    print("As you enter the cave, you find yourself at a crossroads.")
    print("To your left, a narrow passage. To your right, a dark tunnel. Straight ahead, an eerie path filled with silence")
    while True:  # Keep asking until a valid choice is made.
        choice = input("Which way do you go? (left/right/straight):").strip().lower()
        if choice == "left":
            narrow_passage()
            break
        elif choice == "right":
            dark_tunnel()
            break
        elif choice == "straight":
            eerie_path()
            break
        else:
            print("Confused, you wander aimlessly. Please choose a valid direction (left/right/straight).")

def narrow_passage():
    # Path leading to treasure - winning scenario.
    print("The narrow passage leads to a small room filled with gold coins!")
    print("Congratulations! You've found the treasure and completed your quest!")
    play_again()

def dark_tunnel():
    # Path leading to a game over scenario.
    print("As you cautiously move through the dark tunnel, you suddenly fall into a pit!")
    print("Unfortunately, this is where your adventure ends. Game over.")
    play_again()

def eerie_path():
    # Leads to a chamber with choices - mixed outcomes.
    print("The eerie path takes you to a chamber with three doors, each marked with a symbol.")
    while True:  # Ensure valid input is provided.
        choice = input("Which door do you choose? (1, 2, 3):").strip()
        if choice == "1":
            print("You found a room full of ancient artifacts! While not the treasure you sought, it's still a valuable find.")
            play_again()
            break
        elif choice =="2":
            print("This door leads to an empty room. It seems you'll need to choose another adventure.")
            play_again()
            break
        elif choice == "3":
            print("You've walked into a trap! It's the end of your journey.")
            play_again()
            break
        else:
            print("Unable to decide, you eventually leave the cave, perhaps to return another day.")
            play_again()
            break

def play_again():
    # Offers a choice to play again or end the game.
    while True:  # Loop for valid input.
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice == "yes":
            start_game()
            break
        elif choice == "no":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Please enter a valid choice (yes/no).")  # Prompt for valid input.

def start_game():
    # Entry point to start the game.
    introduction()

start_game()
