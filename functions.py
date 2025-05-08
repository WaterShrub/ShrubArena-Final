#function file for Shrub Arena
import logging
logging.basicConfig(filename='ShrubArena.log', 
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
from time import sleep
from random import randint

#Clears the terminal of text
def clearScreen():
    print("\n" * 60)
    return

#Prints text buffer.
def printBuffer():
    print("*-" * 16 + "*") 
    return

#Allows for sleep to be skipped by setting awake flag to True
awake = False
def doSleep(length):
    global awake
    if not awake:
        doSleep(length)

#Asks if player would like to read the manual.
# Prints game manual if requested. 
def printManual():
    choice = input("Would you like to read the manual? y/n: ").lower().strip()

    if choice == 'y':
        manual = """
This is the manual for Shrub Arena
__________________________________

1) Overview
    The goal of the game is to defeat your opponent in combat.
    To do this, you will both select a weapon and fight each other.
    While fighting, you may choose to either attack your opponent 
        or ready your shield to block. 

2) Weapons
    You have four choices for weaponry:
    The sword deals a moderate amount of damage (5) but is fast.
    The axe deals a substansial amount of damage (7) but takes more time to swing. 
    The dagger deals a small amount of damage (3) but is very fast. When attacking, 1/5 chance
        to hit twice. The second hit is not blocked by shields.
    The greataxe deals a large amount of damage (10) but is very slow. After attacking, your next turn
        must block.

3) Attacking
    When attacking, your weapon speed decides who goes first. 
    If a weapon is faster than the opponents, they will always attack first.
    If both opponents have the same weapon speed, a random draw determines 
        who goes first. If opponent two is a bot, this draw favors the player.
    There is a 1/20 chance to deal critical damage when attacking.

4) Blocking
    When you block an attack, 1 of 3 things can happen.
    1)You have a slight chance to block all damage
    2)You have an increased chance to block half of the damage (rounded to the nearest whole number)
    3)You have a chance to parry the attack, dealing a 1-3 damage to the attacker and healing 2-4 health
        *Your health cannot go above 1.2 times your starting health

5) Poison
    You can chose to poison your opponent. This will deal 1-3 damage to them each turn for two turns.
    If your opponent blocks when you apply poison, there is a 1/10 chance that they do not get poisoned.
    Poison cannot "stack". Applying poison again resets the counter to 2 turns.
    Drinking a potion has a 1/4 chance to cure poison. 
    You cannot die from poison damage, but you can be dimished to 1 health.

6) Potions
    You can chose to drink a health potion. This will heal you 2-6 health.
    If you are poisoned, there is a 1/4 chance that the potion will cure the poison.
        This check occurs BEFORE damage from poison is applied in a turn.

7) Bot fight
    Name player 1 "PLAYER1-BOT" to simulate a battle between two bots.
                """
        clearScreen()
        print(manual) 
        logging.debug("Manual printed")      
        doSleep(2)

    printBuffer() 
    return

#Determines outcomes of player move choices and resets move flags
stringCount = False
def move(player1, player2):
    logging.debug("Starting attack sequence")
    global stringCount
    print()

    #Players chose to poison
    stringCount = False
    player1.isPoisoning(player2)
    player2.isPoisoning(player1)
    if stringCount: 
        print()

    #Players chose health potions
    stringCount = False
    player1.isDrinkingPotion()
    player2.isDrinkingPotion()
    if stringCount: 
        print()

    #Poison damage is applied
    stringCount = False
    player1.poisonDamage()
    player2.poisonDamage()
    if stringCount: 
        print()

    #Both platers attack
    if player1.attacking and player2.attacking:
        print(f"{player1.name} and {player2.name} attacked each other!")
        determineOrder(player1, player2)

    #Player1 attacks, player2 blocks/heals
    elif player1.attacking:
        print(f"{player1.name} attacked {player2.name}!")
        attack(player1, player2)

    #Only enemy attacks
    elif player2.attacking:
        print(f"{player2.name} attacked {player1.name}!")
        attack(player2, player1)

    #Both block
    else:
        print(f"Neither {player1.name} or {player2.name} attacked.\n") 

    doSleep(2)
    if not player1.isDead() and not player2.isDead():
        print(f"\n{player1.name}'s health is: {player1.health}")
        print(f"{player2.name}'s health is: {player2.health}")
    printBuffer() 
    doSleep(1)

    #Reset move flags
    player1.resetPlayerFlags()
    player2.resetPlayerFlags()
    return

#Determines the order of attack based on weapon speed and calls attack
def determineOrder(player1, player2):
    if player1.weapon['speed'] == player2.weapon['speed']:
        chance = randint(0,9)
        if player2.bot:
            if chance < 6:
                first = player1
                second = player2
            else:
                first = player2
                second = player1
        else:
            if chance < 5:
                first = player1
                second = player2
            else:
                first = player2
                second = player1
    elif player1.weapon['speed'] > player2.weapon['speed']:
        first = player1
        second = player2
    else:
        first = player2
        second = player1

    attack(first, second)
    print()
    attack(second, first)
    print()

#Deals damage to defender based on attackers weapon and defenders blocking state
def attack(attacker, defender):
    if not defender.isDead():
        blockChance = randint(1,5)
        logging.debug(f"{attacker.name} is attacking {defender.name}")
        logging.debug(f"Block chance: {blockChance}")

        #40% chance for block to parry
        if defender.blocking and blockChance >= 4:
            attacker.damage()
            print(f"{defender.name} parried the attack! Careful, {attacker.name}!")
            defender.heal()
        
        #20% chance for block to block full damage
        elif defender.blocking and blockChance >=2:
            print(f"{defender.name} fully blocked the attack!")

        #40% chance for block to block partial damage
        elif defender.blocking:
            print(f"{defender.name} partially blocked the attack and still lost some health!")
            defender.damage(round(attacker.weapon['damage'] * .5, None), True)

        #No block, deals full damage
        else:
            defender.damage(attacker.weapon['damage'], True)

        #Second hit from dagger
        if attacker.weapon['name'] == 'dagger' and randint(0,4) > 0:
            print(f'{attacker.name} hit twice!')
            defender.damage(attacker.weapon['damage'], True)
    return

#Takes 2 players and determines which one has a positive health
# value and updates their wins accordingly
def determineWinner(player1, player2):
    if player1.isDead():
        winner = player2
    else:
        winner = player1
    print("The winner is...... ", end="", flush=True)
    doSleep(1.5)
    print(f"{winner.name}!")
    doSleep(1)
    logging.debug(f"Winner: {winner.name}")
    winner.wins += 1

def gameEnd(player1):
    if player1.wins > 1:
        print(f"Congrats, {player1.name}, on the {player1.wins} wins!")
    elif player1.wins == 1:
        print(f"Congrats on the win, {player1.name}!")
    print("\nThank you for playing.")
    logging.info("Player exited game")
    exit()