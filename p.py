#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
n=int(input("enter no. of times you want to play this game"))
i=1
while (i<=n) :
    def Winner(player1,player2):
        if player1 == player2:
            return None
        elif player1== 's':
            if player2 == 'w':
                return False
            elif player2 == 'g':
                return True
        elif player1 == 'w':
            if player2 == 'g':
                return False
            elif player2 == 's':
                return True
        elif player1 == 'g':
            if player2 == 's':
                return False
            elif player2  == 'w':
                return True

    player1=input("Player1's Turn: Snake(s) Water(w) or Gun(g)?")
    

    player2 = input("Player2's turn: Snake(s) Water(w) or Gun(g)?")
    Final_result = Winner(player1,player2)

    print(f"Player1 chose {player1}")
    print(f"Player2 chose {player2}")

    if Final_result==None:
        print("The game is a Tie!")
    
    elif Final_result:
        print("Player2 Won!")
    else:
        print("Player2 Lost!")
i+=1

