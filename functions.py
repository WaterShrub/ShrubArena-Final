import logging
logging.basicConfig(filename='ShrubArena.log', 
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
from time import sleep
from random import randint

#Determines who is attacking or blocking
# and outputs each players health after
# attack sequence
def attack(player1, player2):
    logging.debug("Starting attack sequence")

    if player1.bot:
        
    if player1.attacking
    sleep(0.5)
    print(f"{player1.name}'s health is: {player1.health}\n")
    print(f"{player2.name}'s health is: {player2.health}\n")
    printBuffer() 
    sleep(1.2)
    return



#Clears the terminal of text
def clearScreen():
    print("\n" * 60)
    return

#Deals damage to defender based on attackers weapon.
# if defended is blocking, unsets the block flag and ends
def damage(attacker, defender):
    blockChance = randint(1,5)
    logging.debug(f"Block chance: {blockChance}")

    #40% chance for block to parry
    if defender.blocking and blockChance >= 4:
        defender.blocking = False
        defender.health += randint(2,4)
        attacker.health -= randint(1,3)

        if defender.health > defender.maxHealth:
            defender.health = defender.maxHealth 
        if attacker.health < 0:
            attacker.health = 0
    
        print(f"{defender.name} parried the attack! Careful, {attacker.name}!\n")
    
    #20% chance for block to block full damage
    elif defender.blocking and blockChance >=2:
        defender.blocking = False
        print(f"{defender.name} fully blocked the attack!\n")
        if defender.health < 0:
            defender.health = 0

    #40% chance for block to block partial damage
    elif defender.blocking:
        defender.blocking = False
        defender.health -= round(attacker.weapon['damage'] * .5, None)
        print(f"{defender.name} partially blocked the attack and still lost some health!\n")
        if defender.health < 0:
            defender.health = 0

    #No block, deals full damage
    else:
        defender.health -= attacker.weapon['damage']
        if defender.health < 0:
            defender.health = 0
    return

#Takes 2 players and determines which one has a positive health
# value and updates their wins accordingly
def determineWinner(player1, player2):
    if player1.isDead():
        winner = player2
    else:
        winner = player1
    print(f"The winner is {winner.name}!")
    logging.debug(f"Winner: {winner.name}")
    winner.wins += 1

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
    You have two choices for weaponry: a trusty sword or a mighty axe.
    The sword deals a moderate amount of damage (5) but is fast.
    The axe deals a substansial amount of damage (7) but takes more time to swing. 

3) Attacking
    When attacking, your weapon speed decides who goes first. 
    If a weapon is faster than the opponents, they will always attack first.
    If both opponents have the same weapon speed, a random draw determines 
        who goes first. If one opponent is a bot, this draw favors the player.

4) Blocking
    When you block an attack, 1 of 3 things can happen.
    1)You have a slight chance to block all damage
    2)You have an increased chance to block half of the damage (rounded to the nearest whole number)
    3)You have a chance to parry the attack, dealing a 1-3 damage to the attacker and healing 2-4 health
        *Your health cannot go above 1.2 times your starting health
                """
        clearScreen()
        print(manual)       
        sleep(2)

    printBuffer() 
    return

#Prints text buffer.
def printBuffer():
    print("*-" * 16 + "*") 
    return

#Asks user if they would like to replay.
# Returns 'y' or 'n'.
def replayChoice():
    choice = input("Would you like to play again? y/n: ").lower().strip()

    while choice != 'y' and choice != 'n':
        print("Invalid input.")
        choice = input("Would you like to play again? y/n: ").lower().strip()
    
    return choice
