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
        who goes first. If opponent two is a bot, this draw favors the player.

4) Blocking
    When you block an attack, 1 of 3 things can happen.
    1)You have a slight chance to block all damage
    2)You have an increased chance to block half of the damage (rounded to the nearest whole number)
    3)You have a chance to parry the attack, dealing a 1-3 damage to the attacker and healing 2-4 health
        *Your health cannot go above 1.2 times your starting health
                """
        clearScreen()
        print(manual) 
        logging.debug("Manual printed")      
        sleep(2)

    printBuffer() 
    return



#Determines who is attacking or blocking
# and outputs each players health after
# attack sequence
def move(player1, player2):
    logging.debug("Starting attack sequence")
    #Players chose health potions
    if player1.healing:
        player1.heal(randint(1,6))
    if player2.healing:
        player2.heal(randint(1,6))

    #Both platers attack
    if player1.attacking and player2.attacking:
        print(f"{player1.name} and {player2.name} attacked each other!")

        #Both players have same speed and player2 is a bot
        if player1.weapon['speed'] == player2.weapon['speed'] and \
            player2.bot == True:
            if randint(0,9) < 6:
                attack(player1, player2)
                attack(player2, player1)
            else:
                attack(player2, player1)
                attack(player1, player2)

        #Both players have same speed
        elif player1.weapon['speed'] == player2.weapon['speed']:
            if randint(0,9) < 5:
                attack(player1, player2)
                attack(player2, player1)
            else:
                attack(player2, player1)
                attack(player1, player2)
        
        #Player1 has a faster speed
        elif player1.weapon['speed'] > player2.weapon['speed']:
            attack(player1, player2)
            attack(player2, player1)

        #Player2 has a faster speed
        else:
            attack(player2, player1)
            attack(player1, player2)

    #Player1 attacks, player2 blocks/heals
    elif player1.attacking and not player2.attacking:
        print(f"{player1.name} attacked {player2.name}!")
        attack(player1, player2)

    #Only enemy attacks
    elif player2.attacking and not player1.attacking:
        print(f"{player2.name} attacked {player1.name}!")
        attack(player2, player1)

    #Both block
    else:
        print(f"Neither {player1.name} or {player2.name} attacked.\n") 

    sleep(0.5)
    if not player1.isDead() and not player2.isDead():
        print(f"\n{player1.name}'s health is: {player1.health}")
        print(f"{player2.name}'s health is: {player2.health}")
    printBuffer() 
    sleep(1.2)

    #Reset move flags
    player1.attacking = False
    player2.attacking = False
    player1.blocking = False
    player2.blocking = False
    player1.healing = False
    player2.healing = False
    return

#Deals damage to defender based on attackers weapon.
# if defended is blocking, unsets the block flag and ends
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
            defender.damage(round(attacker.weapon['damage'] * .5, None))

        #No block, deals full damage
        else:
            defender.damage(attacker.weapon['damage'])
    return

#Takes 2 players and determines which one has a positive health
# value and updates their wins accordingly
def determineWinner(player1, player2):
    if player1.isDead():
        winner = player2
    else:
        winner = player1
    print("The winner is...... ", end="", flush=True)
    sleep(1.5)
    print(f"{winner.name}!")
    sleep(1)
    logging.debug(f"Winner: {winner.name}")
    winner.wins += 1
