def attack(player1, player1Move, player2, player2Move):
    logging.debug("Starting attack sequence")
    player1Move = str(player1Move)
    player2Move = str(player2Move)

    #Both attack
    if player1Move == 'Attack' and player2Move == 'Attack':
        print(f"{player1.name} and {player2.name} attacked each other!")
        
        #Both attackers have same speed and a player is CPU
        if player1.weapon['speed'] == player2.weapon['speed'] and \
            (player1.bot == True ^ player2.bot == True):
            if randint(0,9) < 6:
                damage(player1, player2)
                if not player2.isDead():
                    damage(player2, player1)
            else:
                damage(player2, player1)
                if not player1.isDead():
                    damage(player1, player2)

        #Both attackers have same speed
        if player1.weapon['speed'] == player2.weapon['speed']:
            if randint(0,9) < 5:
                damage(player1, player2)
                if not player2.isDead():
                    damage(player2, player1)
            else:
                damage(player2, player1)
                if not player1.isDead():
                    damage(player1, player2)

        #Player has a faster speed
        elif player1.weapon['speed'] > player2.weapon['speed']:
            damage(player1, player2)
            if not player2.isDead():
                damage(player2, player1)

        #Enemy has a faster speed
        else:
            damage(player2, player1)
            if not player1.isDead():
                damage(player1, player2)

    #Only player attacks
    elif player1Move == 'Attack' and player2Move == 'Block':
        print(f"{player1.name} attacked and {player2.name} blocked:")
        player2.block()
        damage(player1, player2)       

    #Only enemy attacks
    elif player2Move == 'Attack' and player1Move == 'Block':
        print(f"{player2.name} attacked and {player1.name} blocked:")
        player1.block()
        damage(player2, player1)

    #Both block
    else:
        print(f"{player1.name} and {player2.name} both blocked.\n")

    sleep(0.5)
    print(f"{player1.name}'s health is: {player1.health}\n")
    print(f"{player2.name}'s health is: {player2.health}\n")
    printBuffer() 
    sleep(1.2)
    return
