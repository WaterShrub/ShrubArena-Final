import logging
logging.basicConfig(filename='ShrubArena.log', 
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
from random import randint
from time import sleep
from getpass import getpass

#Game constants/variables
PLAYER_START_HEALTH = 25
PLAYER_MAX_HEALTH = int(PLAYER_START_HEALTH * 1.2)

enemyNames = ("Bob", "Leonidas", "Boss-man", "One-eyed Duck", "Calzoni", 
              "Nebula", "Cymbal Monkey", "AIDAN", "&$!'@$#", "Nemo",
              "Dev", "Crabcake", "a Slice of 'za", "Your future self",
              "Err-or!", "A chocolate chip", "The Doors", "ENEMY_NAME")
playerNames = []
totalPlayers = 0

REPLAYCHOICES = {'1' : 'Play again vs same enemy', 
                '2' : 'Play again vs new enemy',
                '3' : 'Exit'}

#Enter new weapons below this line:

WEAPON_DAGGER = {'name' : 'dagger',
                'damage' : 3, 
                'speed' : 10}
WEAPON_SWORD = {'name' : 'sword', 
                'damage' : 5, 
                'speed' : 7}
WEAPON_AXE = {'name' : 'axe', 
              'damage' : 7, 
              'speed' : 4}
WEAPON_GREATAXE = {'name' : 'great axe',
                  'damage' : 10, 
                  'speed' : 2}
WEAPONS = {'1' : WEAPON_SWORD, 
           '2' : WEAPON_AXE,
           '3' : WEAPON_DAGGER,
           '4' : WEAPON_GREATAXE}

MOVES = {'1' : 'Attack', 
         '2' : 'Block',
         '3' : 'Health Potion'}

class Player:
    def  __init__(self, name = '', bot = False):
        global totalPlayers
        totalPlayers += 1  

        if str(name).islower():
            name = str(name).title() 
        if name == '':
            self.name = input(f"\nEnter your name, player {totalPlayers}: ").strip()
            sleep(0.5)
        else:
            self.name = str(name)
        if self.name in playerNames:
            print(f"Name already taken. Please choose another name.")
            self.name = input(f"\nEnter your name, player {totalPlayers}: ").strip()
            sleep(0.5)
        playerNames.append(self.name)

        self.bot = bot
        #self.weapon = self.weaponSelect()
        self.health = PLAYER_START_HEALTH
        self.maxHealth = PLAYER_MAX_HEALTH 
        self.wins = 0
        self.replay = '3'
        #Move flags
        self.attacking = False
        self.blocking = False
        self.healing = False

        self.weaponSelect()

        if not bot:
            print(f"Welcome, {self.name}!")
        logging.debug(f"{self.name} has been created.")

    #weaponSelect asks player to choose a weapon and stores 
    # the choice in the player dictionary. If the player
    # already knows their choice, they can supply that choice
    # at function call as a str.
    def weaponSelect(self):
        global WEAPONS

        #Default selection, requests choice from terminal
        if not self.bot:
            print(f"\n{self.name}, select your weapon: \n"\
                  "**Choices hidden for privacy.")
            for number, weapon in WEAPONS.items():
                print(f"{number}) {str(weapon['name']).title()} - {weapon['damage']} damage and {weapon['speed']} speed")
            weaponSelection = getpass("").strip()
        else:
            weaponSelection = str(randint(1,len(WEAPONS)))
        while weaponSelection not in WEAPONS:
            print("Invalid input.")
            weaponSelection = getpass("Please enter the number corresponding to your weapon choice: ").strip()
        sleep(0.5)

        logging.debug(f"{self.name} chose the {WEAPONS[weaponSelection]['name']}")
        self.weapon = WEAPONS[weaponSelection]
        return 

    #Checks if player is alive or dead.
    def isDead(self):
        logging.debug(f"Checked if {self.name} is dead.")
        return self.health <= 0
   
   #Requests input from the player to determine their next move.
    #If the player already knows their choice, they can supply 
    # that choice at function call as a str.
    def moveSelect(self):
        global MOVES

        #Default selection, requests choice from terminal
        if not self.bot:
            print(f"{self.name}, choose your next move:\n"\
                  "**Choices hidden for privacy.")
            for number, move in MOVES.items():
                print(f"{number}) {move}")
            choice = str(getpass("").strip())
            print()
        else:
            choice = str(randint(1,len(MOVES)))

        while choice not in MOVES:
            print("Invalid input.")
            choice = getpass("Please enter the number corresponding to your move choice: ").strip()

        if str(choice) == '1':
            self.attacking = True
        elif str(choice) == '2':
            self.blocking = True
        elif str(choice) == '3':
            self.healing = True

        logging.debug(f"{self.name} chose {MOVES[choice]}")
        return
    
    #Verifies that player has legal health value.
    def checkHealth(self):
        if self.health > self.maxHealth:
            self.health = self.maxHealth
        if self.health < 0:
            self.health = 0
        logging.debug(f"Checked {self.name} for legal health values.")
        return
    
    #Heals player based on supplied amount. Defaults a random value between 2 and 4.
    def heal(self, amount = randint(2,4)):
        self.health += amount
        print(f"{self.name} healed for {amount} health!")
        logging.debug(f"{self.name} healed for {amount} health!")
        self.checkHealth()

    #Damages player based on supplied amount. Defaults a random value between 1 and 3.
    def damage(self, amount = randint(1,3)):
        self.health -= amount
        print(f"{self.name} took {amount} damage!")
        logging.debug(f"{self.name} took {amount} damage!")
        self.checkHealth()

    #Asks user if they would like to replay.
    #Returns int choice
    def replayChoice(self):
        logging.debug("Requesting replay choice")
        
        print("Would you like to:")
        for number, choice in REPLAYCHOICES.items():
                print(f"{number}) {choice}")
        self.replay = str(input().strip())
        while self.replay not in REPLAYCHOICES:
            print("Invalid input.")
            self.replay = str(input("Please enter the number corresponding to your choice: ").strip())
