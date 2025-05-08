'''

INF360 - Programming in Python

Final

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

#Exits on unpredicted errors
try:
    #Intro
    fn.clearScreen()
    print("Welcome to the Shrub Arena!")
    print("___________________________")
    fn.printManual()
    fn.doSleep(0.3)

    #Initialize player 1
    logging.debug("Creating player 1")
    player1 = pl.Player()
    fn.doSleep(0.2)

    #Starts game with new second player
    logging.debug("Starting game with new player")
    playGame = True
    while playGame:
        #initiallize player2
        if not player1.bot:
                player2Choice = input(
                                "\nWould you like to play againtst:\n" \
                                "1) A computer\n" \
                                "2) Another human\n").strip()
                while str(player2Choice) != '1' and str(player2Choice) != '2':
                    player2Choice = input("Invalid choice. \nPlease enter the number corresponding to your choice: ")
                fn.doSleep(0.5)

        else:
            logging.debug("Battle will be bots only")
            player2Choice = '1'

        logging.debug("Creating player 2")
        if player2Choice == '1':
            player2 = pl.Player(bot = True)
            print(f"{player1.name}, your enemy is {player2.name}.\n")
        else :
            player2 = pl.Player()
            fn.doSleep(0.2)

        #Main Game Loop
        logging.debug("Starting main game loop")
        playGameCurrentPlayers = True
        while playGameCurrentPlayers:
            playGameCurrentPlayers = True
            print(f"\n{player1.name} chose the {player1.weapon['name']}.")
            print(f"{player2.name} chose the {player2.weapon['name']}.")
            fn.doSleep(1)

            #Play until a players health <= 0
            print(f"\nAll players are starting with {pl.PLAYER_START_HEALTH} health.")
            print("*-" * 10 + "*")
            while not player1.isDead() and not player2.isDead():
                player1Move = player1.moveSelect()
                player2Move = player2.moveSelect()
                fn.move(player1, player2)

            #Determine winner
            logging.debug("Determining winner")
            fn.determineWinner(player1, player2)
            logging.debug("Winner determined")

            #Display wins and ask to replay
            print(f"\n{player1.name}'s total wins: {player1.wins}")
            print(f"{player2.name}'s total wins: {player2.wins}")
            fn.printBuffer()
            player1.replayChoice()

            if player1.replay == '3':
                playGameCurrentPlayers = False
                playGame = False
            else:
                if player1.replay == '2':
                    logging.debug("Replaying with new player")
                    playGameCurrentPlayers = False
                else:
                    logging.debug("Replaying with same players")
                fn.clearScreen()
                print(f"Welcome Back to the Shrub Arena, {player1.name}!")
                print("___________________________")
                fn.doSleep(1)

                #Reset player variables
                player1.resetPlayerStats()
                if player1.replay == '1':
                    player2.resetPlayerStats()
                else:
                    pl.totalPlayers -= 1

    #End game
    fn.gameEnd(player1)
except KeyboardInterrupt:
    print()
    try:
        fn.gameEnd(player1)
    except NameError:
        print("Game interrupted before player was created.")
        logging.info("Game interrupted before player was created.")
        exit()
except Exception as e:
    print()
    print(f"Unexpected error: {e}.\nExiting game.")
    logging.critical(f"Unexpected error: {e}.\nExiting game.")
    exit()