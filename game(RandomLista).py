#import the module random

import random
from select import select

#save the player helth
playerLive = 100

#save the player mana

playerMana = 100

#defaut of enem life

enemyLife = 50

#defaut the number of enemies 

n = int(input("Chose the amount of enemies"))

#vector that sabe all the enemies

enemy = []

for i in range(n):
    enemy.append([i+1,enemyLife])

#while this variable is true we are playing the game
playing = True
while playing:
    # show on scree the life of the player 
    print("health: ", playerLive)
    print("Mana: ", playerMana)
    
    action = int(input("Choose to atack (1) or to cure (2)"))

    if action == 1:
        #choose a random enemy
        selectEnemy = random.choice(enemy) #random choice take a random item from the list
        #determine the damage
        damage = random.randint(1,20)
        print("You cause %i of damage on the enemy %i" %(damage, selectEnemy[0]))
        selectEnemy[1] -= damage # selectEnemy[n] and enemy[selectEenemy[n]] point to the same memory adress 
        if selectEnemy[1] <= 0:
            #say that the enemy is dead
            print("Enemy %i is dead" %selectEnemy[0])
            enemy.remove(selectEnemy)
        print("Enemies healt: ", enemy)
    
    if action == 2: 
        #cure youself, but only is the sp if greater then 10
        if playerMana >= 10: 
            health = random.randint(10,20)
            print("you receive %i of health" %health)
            playerLive += health
            playerMana -= 10 
        else: 
            #player can't cure herself
            print("you dont have enougth mana")
    
    #now the nemy atack enemy are stuped and they dont cure themself

    for i in enemy: # i can change range(n) to a list
        #choose the damage
        hit = bool(random.choice([1,1,1,0]))
        if hit: #i can use 1 or 0 as True or false
            #choose the damage
            damage = random.randint(1,20)
            print("The enemy %i couse you %i of damage" %(i[0], damage))
            playerLive -= damage
        else: 
            print("The enemy Miss")
    #increase the mana of the player in each turn        
    if playerMana < 100:
        playerLive += 3

    # but never more than one hundred
    if playerMana > 100:
        playerMana = 100
    
    #if the life of the player is lower than 0 the player lost

    if playerLive < 0:
        print("You lose") 
        playing = False 

    if len(enemy) == 0:
        print("You win")
        playing = False 






