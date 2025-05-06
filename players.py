enemyNames = ("Bob", "Leonidas", "Boss-man", "One-eyed Duck", "Calzoni", 
              "Nebula", "Cymbal Monkey", "AIDAN", "&$!'@$#", "Nemo",
              "Dev", "Crabcake", "a Slice of 'za", "Your future self",
              "Err-or!", "A chocolate chip", "The Doors", "ENEMY_NAME")

#Game constants
PLAYER_START_HEALTH = 25
PLAYER_MAX_HEALTH = int(PLAYER_START_HEALTH * 1.2)

#Enter new weapons below this line:

WEAPON_SWORD = {'name' : 'sword', 
                'damage' : 5, 
                'speed' : 7}
WEAPON_AXE = {'name' : 'axe', 
              'damage' : 7, 
              'speed' : 4}
WEAPONS = {'1' : WEAPON_SWORD, 
           '2' : WEAPON_AXE}

MOVES = {'1' : 'Attack', 
         '2' : 'Block',
         '3' : 'Potion'}

class Player:
    def  __init__(self, name, bot = False):
        if str(name).islower():
            name = str(name).title()
        self.name = str(name) 
        self.bot = bot
        self.weapon = {}
        self.health = PLAYER_START_HEALTH
        self.maxHealth = PLAYER_MAX_HEALTH 
        self.attacking = False
        self.blocking = False
        self.healing = False
        self.wins = 0

    #weaponSelect asks player to choose a weapon and stores 
    # the choice in the player dictionary. If the player
    # already knows their choice, they can supply that choice
    # at function call as a str.
    def weaponSelect(self, weaponSelection = '-1'):
        weaponSelection = str(weaponSelection)
        global WEAPONS

        #Default selection, requests choice from terminal
        if weaponSelection not in WEAPONS:
            print("Select a weapon:")
            for number, weapon in WEAPONS.items():
                print(f"{number}) {str(weapon['name']).title()} - {weapon['damage']} damage and {weapon['speed']} speed")
            weaponSelection = input().strip()

        while weaponSelection not in WEAPONS:
            print("Invalid input.")
            weaponSelection = input("Please enter the number corresponding to your weapon choice: ").strip()

        self.weapon = WEAPONS[weaponSelection]
        print(f"\n{self.name} chose the {self.weapon['name']}.")
        return

    #Checks if player is alive or dead.
    def isDead(self):
        return self.health <= 0
   
   #Sets the value of the 'blocking' key to True for the blocker
    def block(self):
        self.blocking = True
        return
   
   #Requests input from the player to determine their next move.
    #If the player already knows their choice, they can supply 
    # that choice at function call as a str.
    def moveSelect(self, choice = '0'):
        choice = str(choice)
        global MOVES

        #Default selection, requests choice from terminal
        if choice not in MOVES:
            print("Choose your next move:")
            for number, move in MOVES.items():
                print(f"{number}) {move}")
            choice = input().strip()
            print()

        while choice not in MOVES:
            print("Invalid input.")
            choice = input("Please enter the number corresponding to your move choice: ").strip()

        if str(choice) == '1':
            self.attacking = True
        elif str(choice) == '2':
            self.blocking = True
        elif str(choice) == '3':
            self.healing = True