# Initialize global variables for tracking the player's trust with the dragon and overall quest success.
dragon_trust = True
all_quests_success = True

def introduction():
    # This function introduces the game and its setting to the player.
    print("Welcome to The Quest for the Starlight Pendant!")
    print("\nIn the attic of your grandmother's house, you discover a mysterious portal glowing with ethereal light.")
    # Leads the player to the next phase of the game after setting up the context.
    enter_lumina()

def enter_lumina():
    # Access global variables to reset their values for a new game session.
    global dragon_trust, all_quests_success
    print("\nAs you step through the portal, you're whisked away to Lumina, a world unlike any you've seen...")
    print("A wise old owl greets you.'Ah, the hero arrives without a moment to lose. Lumina's fate hangs")
    print("in the balance. Seek out the Starlight Pendant pieces by completing 3 quests.'")
    # Resets the dragon's trust at the start of a new game to ensure game state consistency.
    dragon_trust = True
    # A prompt for the player to indicate readiness to start the first quest, enhancing player engagement.
    input("\nPress Enter when you're ready to begin your first quest...")
    # Transition to the first quest, progressing the game forward.
    quest1_candy_forest()

def select_herbs(herbs, target, max_attempts=3):
    # Initialize an empty list to store the selected herbs by the player.
    selected_herbs = []
    # Initialize current_points to track the total points of selected herbs.
    current_points = 0
    # Set attempts_remaining to the maximum number of attempts allowed.
    attempts_remaining = max_attempts
    
    # Inform the player of the game's objective.
    print(f"\nCombine herbs to total {target} points, using each only once.")
    print("Type the herb's name one at a time then hit ENTER.")

    # Continue the loop until the target points are met or attempts run out.
    while current_points < target and attempts_remaining > 0:
        # Display the number of attempts left to the player.
        print(f"Attempts remaining: {attempts_remaining}")
        choice = input(f"Current points: {current_points} / {target}. Choose an herb (or 'done' to finish): ").strip().lower()

        if choice == 'done':
            # Check if the current points match the target; if so, the player has succeeded.
            if current_points == target:
                # Announce the player's success and the reward.
                print("Here's your selection:", ', '.join(selected_herbs))
                print("\nYou've successfully created the cure for the Candy Kingdom!")
                print("The prince exclaims, 'You've done it!' The cure revives the kingdom, bringing back joy and laughter.")
                print("In gratitude, you're awarded a piece of the Starlight Pendant, crucial for your quest.")
                # Prompt the player to proceed to the next quest.
                input("\nPress Enter when you're ready to proceed to the next quest...")
                quest2_misunderstood_creature()
                return selected_herbs
            else:
                # If the target is not met, reduce the attempts and prompt to try again.
                print("Selection incomplete. Target not achieved.")
                attempts_remaining -= 1
                if attempts_remaining == 0:
                    print("You've used up all your attempts. Better luck next time!")
                    return []
                print("Please try again.")
        elif choice not in [herb.lower() for herb in herbs]:
            # Inform the player if an invalid herb is chosen.
            print("Invalid herb. Please choose from the list.")
            continue
        elif choice in [herb.lower() for herb in selected_herbs]:
            # Prevent the player from selecting the same herb more than once.
            print("Herb already selected. Choose another.")
            continue
        else:
            # Add the selected herb to the list and update current points.
            original_herb_name = next((herb for herb in herbs if herb.lower() == choice), None)
            selected_herbs.append(original_herb_name)
            current_points += herbs[original_herb_name]
            print(f"{original_herb_name} added. Total points: {current_points}/{target}")

    # If the loop ends due to reaching the target, announce success and proceed.
    if current_points == target:
        print("Here's your selection:", ', '.join(selected_herbs))
        print("\nYou've successfully created the cure for the Candy Kingdom!")
        print("The prince exclaims, 'You've done it!' The cure revives the kingdom, bringing back joy and laughter.")
        print("In gratitude, you're awarded a piece of the Starlight Pendant, crucial for your quest.")
        input("\nPress Enter when you're ready to proceed to the next quest...")
        quest2_misunderstood_creature()
        return selected_herbs
    else:
        # If all attempts are used without success, inform the player.
        print("You've used up all your attempts. Better luck next time!")
        return []

def quest1_candy_forest():
    # Begin Quest 1: Introduction to the Candy Forest scenario.
    print("\nQuest 1: The Candy Forest")
    print("In the Candy Forest, the Candy Prince reveals an illness is spreading across the kingdom.")
    print("Despite having herbs, the cure remains undiscovered. You step up to help.")

    # Define available herbs and their corresponding point values.
    herbs = {'Sugarroot': 5, 'Mintleaf': 10, 'Cocoa Bean': 15, 'Gumdrop Berry': 7, 'Lollipop Lotus': 8}
    # Set the target point value to successfully create the cure.
    target = 25

    # Display the menu of herbs and their points to the player.
    print("\nHerb Menu:")
    for herb, value in herbs.items():
        print(f"{herb}: {value} points")

    # Call select_herbs function to let the player choose herbs towards meeting the target.
    selected_herbs = select_herbs(herbs, target)

    # Check if the selected herbs meet the target points for the cure.
    if sum(herbs[h] for h in selected_herbs) == target:
        # Success path: player has chosen correctly and created the cure.
        print("With careful thought, you select the herbs. The mixture glows and bubbles.")
        print("You've successfully created the cure for the Candy Kingdom!")
    else:
        # Failure path: incorrect combination, leading to quest failure.
        print("The combination is incorrect. The cure was not created.")
        print("You've failed Quest 1. The adventure ends here.")

        # Offer the player a chance to restart the adventure.
        play_again()

def quest2_misunderstood_creature():
    # Introduce Quest 2, setting the scene with the player encountering a dragon arranging its nest.
    print("\nQuest 2: The Dragon's Nest")
    print("Beneath the twilight sky, you stand in a clearing, watching as a dragon painstakingly arranges its nest.")
    print("You explain how you have been sent to help.")
    print("'The nest needs more for the eggs to endure the night,' the dragon expresses. 'But what can a human do?'")

    # Prompt the player to make a choice on how to assist the dragon with its nest.
    print("How do you respond?")
    while True:
        choice = input("\n1) Gift your hoodie to provide warmth. \n2) Collect large leaves for insulation. \n3) Decline to help and focus on finding the missing Starlight Pendant pieces. \nWhich do you choose? (1, 2, 3): ").strip()
        # Ensure that the player's input is valid.
        if choice in ['1', '2', '3']:
            break
        print("Invalid input. Please enter 1, 2, or 3.")

    # Access the global variable dragon_trust to update it based on the player's choice.
    global dragon_trust
    if choice == '1':
        # If the player chooses to gift their hoodie, reflect this choice in the game narrative and update dragon_trust.
        print("You gift your hoodie to the dragon. It gratefully lines its nest with it, providing warmth and comfort for the eggs.")
        print("The dragon gives you one of the missing Starlight Pendant pieces.")
        dragon_trust = True
    elif choice == '2':
        # If the player chooses to collect leaves, update the narrative and dragon_trust accordingly.
        print("You gather large leaves from the forest floor, adding them to the nest for insulation.")
        print("The dragon nods in approval, its nest now ready for the eggs. The dragon gives you one of the missing Starlight Pendant pieces.")
        dragon_trust = True
    elif choice == '3':
        # Reflect the player's choice to ignore the dragon's need in the narrative and update dragon_trust.
        print("Ignoring the dragon's need, you focus on your quest for the pendant, leaving the nest incomplete.")
        dragon_trust = False

    # Prompt the player to proceed when they are ready, moving forward in the game.
    input("\nPress Enter when you're ready for your final quest...")
    quest3_ancient_ruins()


def quest3_ancient_ruins():
    # Access global variables to reflect changes based on the player's interactions in this quest.
    global dragon_trust, all_quests_success
    
    if dragon_trust:
        # Introduction to Quest 3 with a Sphinx riddle challenge for the player.
        print("\nQuest 3: The Sphinx")
        print("A Sphinx stands in front of 3 doors.")
        print("'Hero, you must solve the riddle and select the correct door to obtain the final piece of the pendant you seek.'")
        # Present the riddle to the player.
        riddle = "I can swim but never get wet. I can fly but I have no wings. I can sing but have no mouth. What am I?"
        print(f"The riddle: '{riddle}'")

        # Define the three doors and their associated images.
        doors = {"1": "a clown", "2": "a fish", "3": "a cloud"}
        print("\nBefore you are three doors, each bearing a different image:")
        for door, image in doors.items():
            print(f"Door {door}: {image}")

        # Loop to ensure valid input from the player.
        while True:
            choice = input("Which door do you choose? (1, 2, 3): ")
            if choice in doors.keys():
                break
            print("Invalid input. Please choose 1, 2, or 3.")

        # The correct door based on the riddle's answer.
        correct_door = "3"
        if choice == correct_door:
            # If the player chooses correctly, they are rewarded and the quest continues.
            print("You've chosen wisely. The door opens to reveal the final piece of the Starlight Pendant.")
        else:
            # Incorrect choice leads to a negative outcome for the quest.
            print("The choice was incorrect. You are led back to the maze's entrance.")
            all_quests_success = False
    else:
        # Alternate path if the player has made choices leading to a lack of trust with the dragon.
        print("\nQuest 3: The Sphinx")
        print("A Sphinx stands in front of 3 doors. 'You should proceed with caution'")
        print("You try to open the first door but it is locked.")
        print("You try the second door but it is locked as well.")
        print("You try to open the third door but it is also locked.")
        print("The Sphinx says 'The you failed the quest due to the choice made earlier'.")
        all_quests_success = False

    # Regardless of outcome, move to the conclusion of the adventure.
    conclude_adventure()


def conclude_adventure():
    # Access the global variable to determine the game's ending based on player success.
    global all_quests_success
    
    if all_quests_success:
        # If all quests were successful, print a message celebrating the player's victory.
        print("\nWith all pieces of the Starlight Pendant united, Lumina's magic is restored. You're hailed as a hero!")
        print("The people of Lumina gather to celebrate, sharing stories of your bravery. The Candy Prince, the dragon, and even the Sphinx join in your honor.")
    else:
        # If any quest was failed, provide feedback that the game has ended but encourage trying different choices.
        print("\nYour journey ends here, but the adventure of Lumina continues.")
        print("Perhaps different choices will lead to a different outcome.")

    # Offer the player the option to play again, reinforcing the game's replayability.
    play_again()

def play_again():
    # Loop to ensure valid input from the player regarding replaying the game.
    while True:
        choice = input("Would you like to play again? (yes/no): ").strip().lower()
        if choice in ['yes', 'no']:
            break
        print("Please enter 'yes' or 'no'.")

    # Reset the game state if the player chooses to play again.
    if choice == 'yes':
        # Access global variables to reset the game's initial conditions.
        global dragon_trust, all_quests_success
        dragon_trust = True  # Resets the player's relationship with the dragon.
        all_quests_success = True  # Resets the success state of the quests.
        introduction()  # Restart the game from the introduction.
    elif choice == 'no':
        # If the player chooses not to play again, thank them for playing and end the game.
        print("Thank you for playing The Quest for the Starlight Pendant. Farewell, brave adventurer!")

# The starting point of the game when the script is executed.
if __name__ == "__main__":
    introduction()  # Call the introduction function to start the game.


