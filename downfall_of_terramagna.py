"""
Name: Adore S.
Date: 2025 Apr 2
Title: Downfall of Terramagna
Description: An interactive choose-your-own adventure story about overthrowing the evil dictator emperor Heiltur I to save the empire of Terramagna from demise.
"""

# Essential packages

import time
import sys
import os
import art
import random as rand
import textwrap

# Main function

def main():
    # Print fancy title (out of main menu function, to prevent repetition)

    art.tprint("DOWNFALL OF TERRAMAGNA", "doom")

    # Bring main menu and let user change settings

    user_option = 0

    while user_option != 1:
        user_option = main_menu()

        # Quit game
        if user_option == 2:
            sys.exit() # quits program and does not allow program to continue
        # Invalid option
        elif user_option == -1:
            print("Invalid option\n")

    # Let user know they can quit anytime -- Ctrl + C normally used to force quit program.

    print("You can press Ctrl + C to quit program anytime.\n")
    
    # Begin story through an introduction, main pathway

    introduction()

    print() # New line
    
    pathway = ""

    # Prompt user to select correct option while they do not

    while pathway not in {"a", "b", "c"}:
        pathway = main_pathway()

        if pathway == "x":
            print("Invalid option")
        
        print()
     
    # Assassination
    if pathway == "a": 
        assassination()
    # Wage battle
    elif pathway == "b":
        wage_battle()
    # Enrage public
    else:
        enrage_public()

# Word wrap, shortcut

def wrap(text: str) -> str:
    return textwrap.fill(text, 100)

# Print text word by word

def print_each_word(text: str, delay: float = 0.1):
    """
    Split the text into array of words, then print each word individually with a time delay
    :param text: Text to print out
    :param delay: Delay before printing next word (seconds)
    """

    # Split text and loop through each word

    for word in text.split(" "):
        # Print word

        print(word, end=" ", flush=True)

        # Time delay

        time.sleep(delay)
    
    # Newline print

    print()

# Main menu

def main_menu() -> int:
    # List options

    print("1. Play story / game")
    print("2. Quit\n")

    # Ask user to select

    try:
        option = int(input("Select an option [1-2]: "))
        print() # newline for better formatting
    except ValueError:
        # if user enters a value that can't be a number, value is invalid
        return -1

    # Return input if input is valid, otherwise return -1

    if 1 <= option <= 2:
        return option
    else:
        return -1

# The introduction

def introduction():
    # Print out lines
    # For each line, user presses enter to continue or types SKIP to skip

    print_each_word(wrap("In the region now known as Terramagna, seven kingdoms fought violent wars until the founder, Emperor Terramagna I, reunited the kingdoms to form the Empire of Terramagna in 1207 YAE (Years After Enlightenment)."))

    skip_intro = input("\nPress ENTER to continue or type SKIP to skip intro: ")

    if skip_intro.upper().strip() == "SKIP":
        return
    
    print()
    
    print_each_word(wrap("For a while, conditions in Terramagna improved. During Terramagna I's rule, Terramagna experienced significant economic growth, the creation of new art and machinery, prosperity, and most importantly, peace."))

    skip_intro = input("\nPress ENTER to continue or type SKIP to skip intro: ")

    if skip_intro.upper().strip() == "SKIP":
        return
    
    print()

    print_each_word(wrap("Good things must always come to an end, though. In 1220 YAE, Terramagna I died from an unknown cause without an heir. The most powerful of noblemen, Heiltur Dictatorus, took over the throne as Heiltur I."))

    skip_intro = input("\nPress ENTER to continue or type SKIP to skip intro: ")

    if skip_intro.upper().strip() == "SKIP":
        return
    
    print()
    
    print_each_word(wrap("His reign brought terror. High tax rates for the common person brought poverty and famine. Those that did not obey his rules, or dared to protest or say anything against him or his rules, would be forced to leave this world. Terramagnians would live in fear and misery."))

    skip_intro = input("\nPress ENTER to continue or type SKIP to skip intro: ")

    if skip_intro.upper().strip() == "SKIP":
        return
    
    print()
    
    print_each_word(wrap("There is only one hope, and that is you. You are the current leader of the Terramagnian Liberation Front (TLF), as of 1230 YAE."))

    skip_intro = input("\nPress ENTER to continue or type SKIP to skip intro: ")

    if skip_intro.upper().strip() == "SKIP":
        return
    
    print()

    print_each_word(wrap("You spent a lot of time rebelling against various of Heiltur's forces to provide justice to Terramagnian's receiving injustice. You gave them the opportunity to flee from danger."))

    skip_intro = input("\nPress ENTER to continue or type SKIP to skip intro: ")

    if skip_intro.upper().strip() == "SKIP":
        return
    
    print()

    print_each_word(wrap("After many quests and battles with Heiltur's forces, the time has come to end Heiltur's rule. The three ways to restore Terramagna's former glory are to assassinate Heiltur I, wage a battle with his forces, or enrage the public."))

# Choose pathway to end Heiltur I's rule. The main pathway.

def main_pathway():
    # List options for the main pathway

    print("Choose your plan:\n")
    print("a) assisinate Heiltur I")
    print("b) wage a battle with Heiltur's forces")
    print("c) enrange the public")

    # Select option and return it, otherwise return x

    option = input("\nSelect your option: ")

    if option.lower().strip() in {"a", "b", "c"}:
        return option.lower().strip()
    else:
        return "x"

# Pathway A: Assassination

def assassination():
    # Print lines

    print_each_word(wrap("You start planning on how to assassinate Heiltur I. However, when will it be the right time? Not when Heiltur I is in his palace, because it is guarded with high security."))

    print()

    input("Press ENTER to continue\n")

    print_each_word(wrap("Fortunately, you hear about Heiltur's plans to do a parade next week. You realize the kill must be delivered secretly."))

    print()

    input("Press ENTER to continue\n")

    print_each_word(wrap("You find that a poisoned needle launcher is the best way to do that. So, you and your rebels go to gather wood."))

    print()

    input("Press ENTER to continue\n")

    # Gather wood after swinging axe 8 times

    print_each_word("You approach a tree. You have to swing your axe to gather a piece of bark.")

    print()

    swings_needed = 8 # Swings needed to chop tree

    for swings_left in range(swings_needed, 0, -1):
        # User swings their axe by pressing enter until there are no more swings

        print("You have %d swings left" % swings_left)
        input("Press ENTER to chop wood ")
        print()
 
    print("You chopped out a piece of wood!\n")

    # Continue lines

    print_each_word(wrap("Then, you catch a poison dart frog. You tip some of your needles with its poison. You are now ready to end the reign of terror."))

    print()
    input("Press ENTER to continue\n")

    print_each_word(wrap("On the day of the parade, you and your rebels disguise yourselves in the crowd, and you ready yourself to fire your poison needle. The emperor is moving toward the crowd on a chariot."))

    print()

    # Poison needle assassination
    
    print("When do you shoot?")

    shoot_time = input("Do you shoot when he is [far], [halfway], or [close]? ")

    print("\nHow high do you shoot?")

    shoot_height = input("Do you shoot [high], [middle-high], [middle], [middle-low], or [low]? ")

    print()

    # Situations

    # Assassination successful
    if shoot_time.lower().strip() == "close" and shoot_height.lower().strip() == "middle-high":
        # Continue lines

        print_each_word(wrap("You have succeeded in killing emperor Heiltur I. Everyone looks in surprise."))

        print()
        input("Press ENTER to continue\n")

        print_each_word(wrap("You reveal yourself and face everyone. The Terramagnian soldiers run at you, but they are stopped by your arousing speech."))

        print()
        input("Press ENTER to continue\n")

        print_each_word(wrap("\"Dear my fellow Terramagnians, you have lived many years under oppression.\""))

        print()

        print_each_word(wrap("\"For many years, our nation and our people suffered through the dictratous rule of the evil Heiltur. This ends TODAY!\""))

        print()

        print_each_word(wrap("\"It will be an honour to serve as your emperor and make Terramagna great again!\""))

        print()
        input("Press ENTER to continue\n")

        print_each_word(wrap("Your speech moves the audience so much that they cheer and happily accept you as their new emperor. The Terramagnian soldiers have no choice, but to submit to you."))

        print()
        input("Press ENTER to continue\n")

        ending_2()
    # Deal with invalid input
    elif shoot_time.lower().strip() not in {"far", "halfway", "close"} or shoot_height.lower().strip() not in {"high", "middle-high", "middle", "middle-low", "low"}:
        # Continue lines

        print("Consequences of invalid input: \n")

        print_each_word(wrap("You failed to make the right judgement on time. A Terramagnian soldier notices you aiming your poison needle towards the emperor."))

        print()

        print_each_word("Terramagnian soldiers come and arrest you and your rebels.")

        print()
        input("Press ENTER to continue\n")

        ending_1()
    # Wrong choice
    else:
        # Continue

        print_each_word(wrap("You attempt to shoot your needle towards the emperor, but you miss."))

        print()
        input("Press ENTER to continue\n")

        print_each_word(wrap("The emperor Heiltur I is furious. Terramagnian soldiers come and arrest you and your rebels."))

        print()
        input("Press ENTER to continue\n")

        ending_1()

# Pathway B: Wage a Battle

def wage_battle():
    # Print lines

    print_each_word(wrap("You decide to wage a battle with Heiltur I. Before waging the battle, you find and recruit more soldiers from various villages to go to battle."))

    print()
    input("Press ENTER to continue\n")

    print_each_word(wrap("You hear about Heiltur's plans to do a parade next week. That would be the best time to start a battle since the emperor will be caught off-guard."))

    print()
    input("Press ENTER to continue\n")

    print_each_word(wrap("On the day of the parade, you bring your forces to the parade. Surprisingly, the soldiers are quickly able to form a sudden defence, and a battle ensues."))

    print()
    input("Press ENTER to continue\n")

    print_each_word(wrap("In order for victory, you must fight your way to the emperor. Your rebels are unable to since they are too busy fighting the emperor's soldiers."))

    print()
    input("Press ENTER to continue\n")

    # Fight soldiers (random number before you get to emperor)

    print_each_word(wrap("Each soldier has a duel pattern that you have to recognize to win."))

    print()
    input("Press ENTER to continue\n")

    print_each_word(wrap("The fights will progressively get harder. The emperor has the hardest duel pattern. Good luck!"))

    print()

    min_soldiers, max_soldiers = 5, 7

    num_of_soldiers = rand.randint(min_soldiers, max_soldiers)

    your_health = 100

    print("%d soldiers stand in your way to the emperor.\n" % num_of_soldiers)

    for i in range(num_of_soldiers):
        # Fighting game

        # First quarter of soldiers 
        if i < num_of_soldiers // 4:
            your_health = fight_soldier(1, your_health)
        # Second quarter of soldiers
        elif i < num_of_soldiers // 2:
            your_health = fight_soldier(2, your_health)
        # Third quarter of soldiers
        elif i < 3 * num_of_soldiers // 4:
            your_health = fight_soldier(3, your_health)
        # Final quarter of soldiers
        else:
            your_health = fight_soldier(4, your_health)
        
        # Did you die in battle? 
        if your_health <= 0:
            print_each_word(wrap("You have been killed in battle and the rest of your group is arrested for treason."))

            print()
            input("Press ENTER to continue\n")

            ending_1()

            return
    
    # Fight the emperor
    
    print_each_word("You now stand face-to-face with Emperor Heiltur I.")

    print()
    input("Press ENTER to continue\n")

    your_health = fight_emperor(your_health)

    # Did you die in battle? Check for the emperor's battle
 
    if your_health <= 0:
        print_each_word(wrap("You have been killed in battle and the rest of your group is arrested for treason."))

        print()
        input("Press ENTER to continue\n")

        ending_1()

        return
    
    # Victory in battle

    print_each_word(wrap("Your defeat of Emperor Heiltur I brought shockwaves throughout the empire."))

    print()
    input("Press ENTER to continue\n")

    print_each_word(wrap("You are crowned the new emperor of Terramagna after the battle. Soldiers give you their loyalty since you proved you are more worthy than Heiltur."))

    print()
    input("Press ENTER to continue\n")

    ending_2()

# Sub-function of Pathway B --- Soldier Combat, returns health

def fight_soldier(pattern: int, your_health: int) -> int:
    # Initialize duel pattern, pattern repeats if at end of list
    # Patterns stored in tuples: (duel_option, direction)

    duel_pattern = []

    # Determine attack pattern of soldier
    if pattern == 1:
        # Both blocks, then attacks the legs, body, and head in order. Alternates between left and right
        duel_pattern = [(4, 1), (1, 1), (5, 2), (2, 2), (6, 1), (3, 1), (4, 2), (1, 2), (5, 1), (2, 1), (6, 2), (3, 2)]
    elif pattern == 2:
        # Attacks the leg twice, then blocks the body, then alternates between jumping or ducking.
        # Weirdly, the soldier attacks / defends left when jumping or right when ducking
        duel_pattern = [(1, 1), (1, 1), (5, 1), (7, 0), (1, 2), (1, 2), (5, 2), (8, 0)]
    elif pattern == 3:
        # Attacks conservatively. Blocks the body either left or right, jumps, ducks, then attacks the body from the opposite direction of the block.
        # Every second attack, soldier also attacks head (same dir.).
        duel_pattern = [(5, 1), (7, 0), (8, 0), (2, 2), (5, 2), (7, 0), (8, 0), (2, 1), (3, 1)]
    elif pattern == 4:
        # Attacks more aggresively than 3. Attacks the body either left or right, jumps, attacks head (opp. dir. of body attack), blocks head of same dir. of head attack, ducks, attacks legs (opp. dir. of head attack)
        duel_pattern = [(2, 1), (7, 0), (3, 2), (6, 2), (8, 0), (1, 1), (2, 2), (7, 0), (3, 1), (6, 1), (8, 0), (1, 2)]
    else:
        raise ValueError("Invalid soldier pattern")
    
    # Duel with soldier. Continues until one dies.

    enemy_health = 100
    enemy_index = 0 # index of duel pattern of enemy

    print("You face a Terramangian soldier to duel.\n")

    while your_health > 0 and enemy_health > 0:
        # Present duel options, and health of both you and enemy.

        print("Choose your duel move:\n")

        print("1. ATTACK: Swing sword toward legs")
        print("2. ATTACK: Swing sword towards body")
        print("3. ATTACK: Swing sword towards head")
        print("4. BLOCK: Block attack toward legs")
        print("5. BLOCK: Block attack towards body")
        print("6. BLOCK: Block attack towards head")
        print("7. DODGE: Jump")
        print("8. DODGE: Duck")

        print()
        print("Your health: %d" % your_health)
        print("Enemy health: %d" % enemy_health)
        print()

        # User input and validation

        try:
            duel_option = int(input("Select your choice: "))

            # Swing left or right? Ignore if 7 and 8 is selected. Validate duel option answers

            if 1 <= duel_option <= 6:
                direction = int(input("Swing / block (1) left or (2) right? "))
            elif 1 <= duel_option <= 8:
                direction = 0
            else:
                # Punish the user for invalid input. They get 12 damage from enemy if they attack.
                duel_option = 0
                direction = 0
            
            # Validate direction answers if they have been given.
            # If direction option is invalid, punish the user. They get 12 damage from enemy if they attack.

            if not (0 <= direction <= 2):
                duel_option = 0
                direction = 0
            elif 1 <= duel_option <= 6 and not (1 <= direction <= 2):
                duel_option = 0
                direction = 0
            elif 7 <= duel_option <= 8 and direction != 0:
                duel_option = 0
                direction = 0
            
            # Print attacks made from both sides
            
        except ValueError:
            # Punish the user for invalid input. They get 12 damage from enemy if they attack.
            duel_option = 0
            direction = 0
        
        # Decide outcome and print your and enemy attacks

        # Damage point system
        # -20 health if one side attacks and attack isn't blocked
        # -10 health if attacks come from both sides
        # no health loss if attack is blocked

        print()
        print_duel_msg((duel_option, direction), 0)
        time.sleep(0.5)
        print_duel_msg(duel_pattern[enemy_index], 1)
        print()
        time.sleep(0.5)

        your_damage, enemy_damage = calc_damage((duel_option, direction), duel_pattern[enemy_index])

        if your_health - your_damage < 0:
            your_health = 0
        else:
            your_health -= your_damage
        
        if enemy_health - enemy_damage < 0:
            enemy_health = 0
        else:
            enemy_health -= enemy_damage

        # Print health loss
        print("You lost %d health" % your_damage)
        print("The enemy lost %d health" % enemy_damage)
        print()
        time.sleep(0.5)

        # Go to next move in duel pattern of enemy. Repeat if at end of duel pattern list.

        if enemy_index + 1 > len(duel_pattern) - 1:
            enemy_index = 0
        else:
            enemy_index += 1
    
    # Message if battle is won. Losing message in battle waged.

    if enemy_health <= 0 and your_health > 0:
        print("You have defeated the soldier.\n")
        time.sleep(0.5)
    
    return your_health

# Sub-function of Pathway C --- Fight with Heiltur I, almost the same as fight_soldier()

def fight_emperor(your_health: int) -> int:
    # Duel pattern for Heiltur I - The Emperor
    # Always on the offensive due to his dictatorous nature.
    # Attack body left, attack leg left, attack head right, jump, attack head left, attack head left, attack leg right, block body right, duck, attack body right

    duel_pattern = [(2, 1), (1, 1), (3, 2), (7, 0), (3, 1), (3, 1), (1, 2), (5, 2), (8, 0), (2, 2)]

    # Duel with Heiltur I. Continues until one dies.

    enemy_health = 100
    enemy_index = 0 # index of duel pattern of enemy

    while your_health > 0 and enemy_health > 0:
        # Present duel options, and health of both you and enemy.

        print("Choose your duel move:\n")

        print("1. ATTACK: Swing sword toward legs")
        print("2. ATTACK: Swing sword towards body")
        print("3. ATTACK: Swing sword towards head")
        print("4. BLOCK: Block attack toward legs")
        print("5. BLOCK: Block attack towards body")
        print("6. BLOCK: Block attack towards head")
        print("7. DODGE: Jump")
        print("8. DODGE: Duck")

        print()
        print("Your health: %d" % your_health)
        print("Enemy health: %d" % enemy_health)
        print()

        # User input and validation

        try:
            duel_option = int(input("Select your choice: "))

            # Swing left or right? Ignore if 7 and 8 is selected. Validate duel option answers

            if 1 <= duel_option <= 6:
                direction = int(input("Swing / block (1) left or (2) right? "))
            elif 1 <= duel_option <= 8:
                direction = 0
            else:
                # Punish the user for invalid input. They get 12 damage from enemy if they attack.
                duel_option = 0
                direction = 0
            
            # Validate direction answers if they have been given.
            # If direction option is invalid, punish the user. They get 12 damage from enemy if they attack.

            if not (0 <= direction <= 2):
                duel_option = 0
                direction = 0
            elif 1 <= duel_option <= 6 and not (1 <= direction <= 2):
                duel_option = 0
                direction = 0
            elif 7 <= duel_option <= 8 and direction != 0:
                duel_option = 0
                direction = 0
            
            # Print attacks made from both sides
            
        except ValueError:
            # Punish the user for invalid input. They get 12 damage from enemy if they attack.
            duel_option = 0
            direction = 0
        
        # Decide outcome and print your and enemy attacks

        # Damage point system
        # -20 health if one side attacks and attack isn't blocked
        # -10 health if attacks come from both sides
        # no health loss if attack is blocked

        print()
        print_duel_msg((duel_option, direction), 0)
        time.sleep(0.5)
        print_duel_msg(duel_pattern[enemy_index], 2)
        print()
        time.sleep(0.5)

        your_damage, enemy_damage = calc_damage((duel_option, direction), duel_pattern[enemy_index])

        if your_health - your_damage < 0:
            your_health = 0
        else:
            your_health -= your_damage
        
        if enemy_health - enemy_damage < 0:
            enemy_health = 0
        else:
            enemy_health -= enemy_damage

        # Print health loss
        print("You lost %d health" % your_damage)
        print("Heiltur I lost %d health" % enemy_damage)
        print()
        time.sleep(0.5)

        # Go to next move in duel pattern of enemy. Repeat if at end of duel pattern list.

        if enemy_index + 1 > len(duel_pattern) - 1:
            enemy_index = 0
        else:
            enemy_index += 1
    
    # Message if battle is won. Losing message in battle waged.

    if enemy_health <= 0 and your_health > 0:
        print("You have defeated Heiltur I. Long live Terramagna!\n")
        time.sleep(0.5)
    
    return your_health

# Print duel move message based on move tuple given: (duel_option, direction) for both sides

def print_duel_msg(move: tuple[int, int], who: int):
    # If who = 0, it's you, if who = 1, it's a soldier, if who = 2, its the emperor
    if who not in {0, 1, 2}:
        raise ValueError("Invalid 'who' value")
    
    # Face the consequences of invalid input
    if move == (0, 0):
        if who != 0: raise ValueError("Invalid move")
        else: print("Invalid input given. You make no move. You will face the consequences.")
    # Attack messages
    elif move == (1, 1):
        if who == 1: print("The enemy soldier swings his sword towards your left leg.")
        elif who == 2: print("The emperor swings his sword towards your left leg.")
        else: print("You swing your sword toward the enemy's left leg.")
    elif move == (1, 2):
        if who == 1: print("The enemy soldier swings his sword towards your right leg.")
        elif who == 2: print("The emperor swings his sword towards your right leg.")
        else: print("You swing your sword toward the enemy's right leg.")
    elif move == (2, 1):
        if who == 1: print("The enemy soldier swings his sword towards the left of your body.")
        elif who == 2: print("The emperor swings his sword towards the left of your body.")
        else: print("You swing your sword towards the left of the enemy's body.")
    elif move == (2, 2):
        if who == 1: print("The enemy soldier swings his sword towards the right of your body.")
        elif who == 2: print("The emperor swings his sword towards the right of your body.")
        else: print("You swing your sword towards the right of the enemy's body.")
    elif move == (3, 1):
        if who == 1: print("The enemy soldier swings his sword towards the left of your head.")
        elif who == 2: print("The emperor swings his sword towards the left of your head.")
        else: print("You swing your sword towards the left of the enemy's head.")
    elif move == (3, 2):
        if who == 1: print("The enemy soldier swings his sword towards the right of your head.")
        elif who == 2: print("The emperor swings his sword towards the right of your head.")
        else: print("You swing your sword towards the right of the enemy's head.")
    # Block messages
    elif move == (4, 1):
        if who == 1: print("The enemy soldier blocks a sword attack towards his left leg.")
        elif who == 2: print("The emperor blocks a sword attack towards his left leg.")
        else: print("You block a sword attack towards your left leg.")
    elif move == (4, 2):
        if who == 1: print("The enemy soldier blocks a sword attack towards his right leg.")
        elif who == 2: print("The emperor blocks a sword attack towards his right leg.")
        else: print("You block a sword attack towards your right leg.")
    elif move == (5, 1):
        if who == 1: print("The enemy soldier blocks a sword attack towards the left of his body.")
        elif who == 2: print("The emperor blocks a sword attack towards the left of his body.")
        else: print("You block a sword attack towards the left of your body.")
    elif move == (5, 2):
        if who == 1: print("The enemy soldier blocks a sword attack towards the right of his body.")
        elif who == 2: print("The emperor blocks a sword attack towards the right of his body.")
        else: print("You block a sword attack towards the right of your body.")
    elif move == (6, 1):
        if who == 1: print("The enemy soldier blocks a sword attack towards the left of his head.")
        elif who == 2: print("The emperor blocks a sword attack towards the left of his head.")
        else: print("You block a sword attack towards the left of your head.")
    elif move == (6, 2):
        if who == 1: print("The enemy soldier blocks a sword attack towards the right of his head.")
        elif who == 2: print("The emperor blocks a sword attack towards the right of his head.")
        else: print("You block a sword attack towards the right of your head.")
    # Dodge messages
    elif move == (7, 0):
        if who == 1: print("The enemy soldier jumps.")
        elif who == 2: print("The emperor jumps.")
        else: print("You jump.")
    elif move == (8, 0):
        if who == 1: print("The enemy soldier ducks.")
        elif who == 2: print("The emperor ducks.")
        else: print("You duck.")
    # Error
    else:
        raise ValueError("Invalid move given")

# Calculate damage in fights with soldiers and emperor, returns a tuple: (your_damage, enemy_damage)

def calc_damage(your_move: tuple[int, int], enemy_move: tuple[int, int]):
    # Raise error if invalid input given
    valid_inputs = {(0, 0), (1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1), (4, 2), (5, 1), (5, 2), (6, 1), (6, 2), (7, 0), (8, 0)}

    if your_move not in valid_inputs or enemy_move not in valid_inputs:
        raise ValueError("Invalid move given")

    # -10 damage to both sides, both sides attack
    
    # You do any attack and enemy does any attack
    if your_move[0] in {1, 2, 3} and enemy_move[0] in {1, 2, 3}:
        return 10, 10
    
    # -20 damage to you for invalid input if enemy attacks
    
    elif your_move == (0, 0) and enemy_move[0] in {1, 2, 3}:
        return 20, 0
    
    # -20 damage to enemy, one-side attack from you

    # You do leg attack and enemy does not block leg attack or jump
    elif your_move == (1, 1) and (enemy_move != (4, 1) and enemy_move != (7, 0)): # LEFT
        return 0, 20
    elif your_move == (1, 2) and (enemy_move != (4, 2) and enemy_move != (7, 0)): # RIGHT
        return 0, 20
    # You do body attack and enemy does not block body attack
    elif your_move == (2, 1) and enemy_move != (5, 1): # LEFT
        return 0, 20
    elif your_move == (2, 2) and enemy_move != (5, 2): # RIGHT
        return 0, 20
    # You do head attack and enemy does not block head attack and duck
    elif your_move == (3, 1) and (enemy_move != (6, 1) and enemy_move != (8, 0)): # LEFT
        return 0, 20
    elif your_move == (3, 2) and (enemy_move != (6, 2) and enemy_move != (8, 0)): # RIGHT
        return 0, 20
    
    # -20 damage to you, one-side attack from enemy

    # Enemy does leg attack and you do not block leg attack and jump
    elif enemy_move == (1, 1) and (your_move != (4, 1) and your_move != (7, 0)): # LEFT
        return 20, 0
    elif enemy_move == (1, 2) and (your_move != (4, 2) and your_move != (7, 0)): # RIGHT
        return 20, 0
    # Enemy does body attack and you do not block body attack
    elif enemy_move == (2, 1) and your_move != (5, 1): # LEFT
        return 20, 0
    elif enemy_move == (2, 2) and your_move != (5, 2): # RIGHT
        return 20, 0
    # Enemy does head attack and you do not block head attack and duck
    elif enemy_move == (3, 1) and (your_move != (6, 1) and your_move != (8, 0)): # LEFT
        return 20, 0
    elif enemy_move == (3, 2) and (your_move != (6, 2) and your_move != (8, 0)): # RIGHT
        return 20, 0
    
    # No damage, means attack was blocked or no attack was made
    
    else:
        return 0, 0

# Pathway C: Enrage the public

def enrage_public():
    # Print lines

    print_each_word(wrap("Sometimes, the best revolutions are started by the common person. However, the average Terramagnian lives in fear. Your solution to this is sending enraging books to Terramagnians in the night."))

    print()
    input("Press ENTER to continue\n")

    chapters_per_book = 5
    pages_per_chapter = 5

    print_each_word(wrap("You draft your book and write %d chapters to encourage Terramagnians to revolt. Each chapter has %d pages." % (chapters_per_book, pages_per_chapter)))

    print()
    input("Press ENTER to continue\n")

    print_each_word(wrap("However, you have to decide how many copies to make. Using your rebels, you can make 10,000, 30,000, or 50,000 copies."))

    print()

    # Make copies of book

    num_of_copies = 0

    while num_of_copies not in {10000, 30000, 50000}:
        try:
            print("Do not include comma or space seperators in your answer")
            num_of_copies = int(input("Do you want to make [10000], [30000], or [50000] copies? "))

            if num_of_copies not in {10000, 30000, 50000}:
                print("Enter 10000, 30000, or 50000 for the number of copies")
            
            print()
        except ValueError:
            print("Enter 10000, 30000, or 50000 for the number of copies")
            print()
    
    for _ in range(num_of_copies // 1000):
        for _ in range(1000 // 50):
            print("📕" * 50)
            time.sleep(0.001)
            
    print("\n")
    
    # Determine outcome based on # of copies

    if num_of_copies == 10000:
        print_each_word(wrap("Unfortunately, you have not printed enough copies for Terramagnians to spread the word and start a rebellion fearlessly."))
        
        print()
        input("Press ENTER to continue\n")

        ending_4()
    elif num_of_copies == 30000:
        print_each_word(wrap("You send your 30,000 copies to many Terramagnians. They feel the rage of revolution from these books."))

        print()
        input("Press ENTER to continue\n")

        print_each_word(wrap("You sent enough copies until the word of revolution spreads to almost every Terramagnian."))

        print()
        input("Press ENTER to continue\n")

        ending_3()
    else: # 50,000 copies
        print_each_word(wrap("There is no way that 50,000 copies of your enraging material won't spread the word of revolution."))

        print()
        input("Press ENTER to continue\n")

        print_each_word(wrap("However, while spreading the messages, one of your rebels is caught and punished horribly. Eventually, he gives in and reveals the location of your hideout."))

        print()
        input("Press ENTER to continue\n")

        ending_1()

# The ENDINGS

# Ending 1

def ending_1():
    print_each_word(wrap("Your entire rebellious group is caught and is unable to defend themselves. The emperor convicts the entire Terramagnian Liberation Front with treason."))

    print()
    input("Press ENTER to continue\n")

    print_each_word(wrap("One by one, every member of the TLF is prematurely sent to heaven by sword."))

    print()
    input("Press ENTER to continue\n")

    print_each_word(wrap("Dreams of another rebellion in Terramagna become crushed as Heiltur I strictens his rule and tightens his patrol of the empire."))

    print()
    input("Press ENTER to continue\n")

    print_each_word(wrap("After your passing, 'ALL HEIL THE MIGHTY HEILTUR' becomes the new greeting of Terramagna. How could the Ultimate Being allow this?"))

    print()
    print_each_word("THE END", 0.5) # delay between each word is 0.5 s

    print()
    input("Press ENTER to end story")
    sys.exit()

# Ending 2

def ending_2():
    print_each_word(wrap("You become the new emperor of Terramagna. Despite your rebels causing harm to the Terramagnian Army, they submit to your rule and allow your rebels to join the army."))

    print()
    input("Press ENTER to continue\n")

    print_each_word(wrap("The general of the Terramagnian army in fact even praises your rebels since throughout your battles against Heiltur's rule, your rebels fought bravely and with skill."))

    print()
    input("Press ENTER to continue\n")

    print_each_word(wrap("However, you are not the solution to Terramagna's emperor problem. As time goes on, you find yourself becoming the very Heiltur that you swore to destroy."))

    print()
    print_each_word("THE END", 0.5)

    print()
    input("Press ENTER to end story")
    sys.exit()

# Ending 3

def ending_3():
    print_each_word(wrap("You are able to enrage the public enough to start a rebellion. They fight the Terramagnian Army fearlessly."))

    print()
    input("Press ENTER to continue\n")

    print_each_word(wrap("Despite many attempts by the army to break the unity of the crowd, the public has had enough."))

    print()
    input("Press ENTER to continue\n")

    print_each_word(wrap("They won't be ruled by another dictator again, and they make sure that happens by eventually overthrowing Heiltur I."))

    print()
    input("Press ENTER to continue\n")

    print_each_word(wrap("After the overthrow, educated members of the common people find that the best way to prevent Terramagna from downfall and misery is by establishing a democratic republic, an idea they noticed from the ancient Athlons."))

    print()
    input("Press ENTER to continue\n")

    print_each_word(wrap("You are elected to be the first elected leader of Terramagna, and you are not given the chance to be a corrupt leader."))

    print()
    print_each_word("THE END", 0.5)

    print()
    input("Press ENTER to end story")
    sys.exit()

# Ending 4

def ending_4():
    print_each_word(wrap("Your plan to cause a public rebellion fails. Eventually, one of your rebels warns your front that soldiers from the Terramagnian army are heading towards your hideout."))

    print()
    input("Press ENTER to continue\n")

    print_each_word(wrap("Your group moves from place to place, and it will be years before another opportunity to dethrone Heiltur I arrives."))

    print()
    print_each_word("THE END", 0.5)

    print()
    input("Press ENTER to end story")
    sys.exit()

# Run the main function. Allow user to exit program anytime without crashing it using Ctrl + C.

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nQuitting program...")

        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)