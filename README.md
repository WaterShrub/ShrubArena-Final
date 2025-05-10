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
