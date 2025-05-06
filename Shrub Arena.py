'''

INF360 - Programming in Python

Midterm

The goal of the game is to defeat your opponent in combat.
    To do this, you will both select a weapon and fight each other.
    While fighting, you may choose to either attack your opponent 
        or ready your shield to block. 

I, Justin Beshirs , affirm that the work submitted for this assignment is entirely my own. 
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, 
or the use of unauthorized materials. This includes, but is not limited to, the use of resources such as Chegg, 
MyCourseHero, StackOverflow, ChatGPT, or other AI assistants, except where explicitly permitted by the instructor. 
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence 
to academic standards. I understand that failing to comply with this integrity statement may result in consequences, 
including disciplinary actions as determined by my course instructor and outlined in institutional policies. 
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''
import logging
logging.basicConfig(filename='ShrubArena.log', 
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
from time import sleep
from random import randint
from sys import exit

try:
    import functions as fn
except:
    logging.critical("Missing function.py")
    print("Missing functions.py")
    exit()

try:
    import players as pl
except:
    logging.critical("Missing players.py")
    print("Missing players.py")
    exit()

#Game variables
playGame = True


#Exits on unpredicted errors
try:
    #Intro
    fn.clearScreen()
    print("Welcome to the Shrub Arena!")
    print("___________________________")
    playerName = str(input("What should we call you? : "))
    if playerName == "":
        playerName = "Player"
    fn.printManual()
    sleep(0.3)

    #Main Game Loop
    logging.debug("Starting main game loop")
    while playGame:
        
        #Define players here
        logging.debug("Creating players")
        player1 = pl.Player(playerName)
        player2 = pl.Player(pl.enemyNames[randint(0, len(pl.enemyNames) - 1)], True)
        print(f"Hello, {player1.name}! Your enemy is {player2.name}.\n")

        #Weapon selections
        logging.debug("Selecting weapons")
        player1.weaponSelect()
        player2.weaponSelect(str(randint(1,len(pl.WEAPONS))))
        sleep(1)

        #Play until a players health <= 0
        print(f"All players are starting with {pl.PLAYER_START_HEALTH} health.")
        print("*-" * 10 + "*")
        while not player1.isDead() and not player2.isDead():
            player1Move = player1.moveSelect()
            player2Move = player2.moveSelect(str(randint(1,2)))

            fn.attack(player1, player1Move, player2, player2Move)

        #Determine winner
        fn.determineWinner(player1, player2)
        logging.debug("Winner determined\n" \
                f"Player 1: {player1.name} - {player1.health} health\n" \
                f"Player 2: {player2.name} - {player2.health} health\n")
        #Display wins and ask to replay
        print(f"\nYour total wins: {player1.wins}")
        replay = fn.replayChoice()

        if replay == 'n':
            playGame = False
        else:
            fn.clearScreen()
            print(f"Welcome Back to the Shrub Arena, {player1.name}!")
            print("___________________________")
            sleep(1)

    #End game
    if player1.wins > 1:
        print(f"Congrats, {player1.name}, on the {player1.wins} wins!")
    elif player1.wins == 1:
        print(f"Congrats on the win, {player1.name}!")
    print("\nThank you for playing.")
    exit()
except KeyboardInterrupt:
    if player1.wins > 1:
        print(f"Congrats, {player1.name}, on the {player1.wins} wins!")
    elif player1.wins == 1:
        print(f"Congrats on the win, {player1.name}!")
    print("\nThank you for playing.")
    exit()
except Exception as e:
    print(f"Unexpected error: {e}.\nExiting game.")
    exit()