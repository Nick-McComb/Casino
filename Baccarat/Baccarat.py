
'''
This is based The Venetian Casino in Las Vegas
Rules for baccarat can be found on https://www.venetianlasvegas.com/resort/casino/table-games/how-to-play-baccarat.html
This is going to be used to simulate the game along with test the Martingale strategy
'''

import random

def baccarat(selection = "player", num_decks = 6):
    deck = [1,2,3,4,5,6,7,8,9,0,0,0,0] * 4
    discard = []
    print(deck)
    random.shuffle(deck)
    print(deck)

    player = []
    banker = []
    winner = None
    player_value = 0
    banker_value = 0

    if len(deck) == 0:
        print("shuffle")
#initial flip    
    player.append(deck.pop())
    print("player flipped a", player[0])
    banker.append(deck.pop())
    print("banker flipped a", banker[0])
    player.append(deck.pop())
    print("player flipped a", player[1])
    banker.append(deck.pop())
    print("banker flipped a", banker[1])
    
    print('\n')

    banker_value = sum(banker)
    player_value = sum(player)

    banker_value = banker_value % 10
    player_value = player_value % 10

    print("bankers value is",banker_value)
    print("players value is",player_value)

    print('\n')


#if banker has 9 and player has 8
    if banker_value == 9 and player_value < 9 or banker_value == 8 and player_value < 8:
        print("banker has",banker_value, "player has",player_value, "BANKER WINS!" )
        winner = "banker"
#if player has 9 and banker has 8
    elif player_value == 9 and banker_value < 9 or player_value == 8 and banker_value < 8:
        print("banker has",banker_value, "player has",player_value, "PLAYER WINS!" )
        winner = "player"
#if player hand is less than 6
    elif player_value < 6:
        player.append(deck.pop())
        print("player flipped a", player[2])
        player_value = sum(player)
        player_value = player_value % 10
        print("players value is",player_value)
    #once the player draws a card this 3rd card determines what the banker does
        #banker always draws if banker value is between 0-2
        if banker_value < 3:
            banker.append(deck.pop())
            print("banker flipped a", banker[2])
            banker_value = sum(banker)
            banker_value = banker_value % 10
            print("bankers value is",banker_value)
        #banker draws on value of 3 if players 3rd card is not an 8
        elif banker_value == 3 and player[2] != 8:
            banker.append(deck.pop())
            print("banker flipped a", banker[2])
            banker_value = sum(banker)
            banker_value = banker_value % 10
            print("bankers value is",banker_value)
        #banker draws on value of 4 if players card is between 2-7
        elif banker_value == 4 and (player[2] > 1 and player[2] < 8):
            banker.append(deck.pop())
            print("banker flipped a", banker[2])
            banker_value = sum(banker)
            banker_value = banker_value % 10
            print("bankers value is",banker_value)
        #banker draws on value of 5 if players card is between 4-7
        elif banker_value == 5 and (player[2] > 3 and player[2] < 8):
            banker.append(deck.pop())
            print("banker flipped a", banker[2])
            banker_value = sum(banker)
            banker_value = banker_value % 10
            print("bankers value is",banker_value)
        #banker draws on value of 6 if players card is between 6-7
        elif banker_value == 6 and (player[2] > 5 and player[2] < 8):
            banker.append(deck.pop())
            print("banker flipped a", banker[2])
            banker_value = sum(banker)
            banker_value = banker_value % 10
            print("bankers value is",banker_value)
#if banker hand is less than 6 and player does not have 3rd card
    elif banker_value < 6:
        banker.append(deck.pop())
        print("banker flipped a", banker[2])
        banker_value = sum(banker)
        banker_value = banker_value % 10
        print("bankers value is",banker_value)

    print('\n')
    print("bankers value is",banker_value)
    print("players value is",player_value)
    
    if banker_value == player_value:
        winner = "push"
    if banker_value > player_value:
        winner = "banker"
    else: winner = "player"

    if winner == "push":
        print("YOU PUSHED")
        return None
    if winner == selection:
        print("YOU WIN!!!")
        return True
    else: 
        print("YOU LOSE!!")
        return False

print(baccarat("banker"))

    

