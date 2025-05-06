#Player class for Shrub Arena
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
                'damage' : 2, 
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
         '3' : 'Health Potion',
         '4' : 'Inflict Poision'}

class Player:
    def  __init__(self, name = '', bot = False):
        global totalPlayers
        totalPlayers += 1  
        self.bot = bot
        self.wins = 0
        self.replay = '3'

        #Defines self.name
        self.namePlayer(name)
        #Defines self.health, self.maxHealth, self.poisoned, and self.poisonedTurns
        self.resetPlayerStats()
        #Defines self.weapon
        self.weaponSelect()
        #Defines self.attacking, self.blocking, self.healing, and self.poisoning
        self.resetPlayerFlags()

        if not bot:
            print(f"Welcome, {self.name}!")
        logging.debug(f"{self.name} has been created.")

    #Assigns a name to player. If player is a bot, a random name is chosen
    def namePlayer(self, name = ''):
        if str(name).islower():
            name = str(name).title() 
        if self.bot:
            self.name = enemyNames[randint(0, len(enemyNames) - 1)]
        elif name == '':
            self.name = input(f"\nEnter your name, player {totalPlayers}: ").strip()
            sleep(0.5)
        else:
            self.name = str(name)
            if self.name == 'PLAYER1-BOT':
                self.bot = True
                self.namePlayer()
        
        if self.name in playerNames:
            print(f"Name already taken. Please choose another name.")
            self.namePlayer()
            sleep(0.5)
        playerNames.append(self.name)

    #Resets player stats for new game
    def resetPlayerStats(self):
        self.health = PLAYER_START_HEALTH
        self.maxHealth = PLAYER_MAX_HEALTH 
        self.poisoned = False
        self.poisonedTurns = 0
        logging.debug(f"{self.name} has had stats reset.")

    #Resets player stats for new game
    def resetPlayerFlags(self):
        self.attacking = False
        self.blocking = False
        self.healing = False
        self.poisoning = False
        logging.debug(f"{self.name} has had flags reset.")

    #Asks player to choose a weapon and stores the choice in self.weapon. 
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

    #Requests input from the player to determine their next move.
    def moveSelect(self):
        global MOVES

        #Requests choice from terminal if not bot
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

        #Set flags
        match choice:
            case '1':
                self.attacking = True
            case '2':
                self.blocking = True
            case '3':
                self.healing = True
            case '4':
                self.poisoning = True

        logging.debug(f"{self.name} chose {MOVES[choice]}")
    
    #Asks user if they would like to replay and modifies self.replay.
    def replayChoice(self):
        logging.debug("Requesting replay choice")
        
        print("Would you like to:")
        for number, choice in REPLAYCHOICES.items():
                print(f"{number}) {choice}")
        self.replay = str(input().strip())
        while self.replay not in REPLAYCHOICES:
            print("Invalid input.")
            self.replay = str(input("Please enter the number corresponding to your choice: ").strip())
 
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

    #Checks if player is poisoned and deals damage if so
    def poisonDamage(self):
        if self.poisoned:
            print(f"{self.name} is poisoned!")
            self.damage()
            self.poisonedTurns -= 1
            if self.poisonedTurns == 0:
                self.poisoned = False
                print(f"{self.name} is no longer poisoned!")
                logging.debug(f"{self.name} is no longer poisoned!")
            if self.health <= 0:
                self.health = 1

    #Verifies that player has legal health value.
    def checkHealth(self):
        if self.health > self.maxHealth:
            self.health = self.maxHealth
        if self.health < 0:
            self.health = 0
        logging.debug(f"Checked {self.name} for legal health values.")

    #Returns players alive state in boolean value
    def isDead(self):
        logging.debug(f"Checked if {self.name} is dead.")
        return self.health <= 0
   
   #Checks if player is drinking a potion and heals if so
    def isDrinkingPotion(self):
        if self.healing:
            self.heal(randint(1,6))
    
    #Checks if a player is applying poison and applies if so
    def isPoisoning(self, defender):
        if self.poisoning and randint(1,10) < 10 and not defender.blocking:
            print(f"{self.name} poisoned {defender.name}!")
            logging.debug(f"{self.name} poisoned {defender.name}")
            defender.poisoned = True
            defender.poisonedTurns = 2

    