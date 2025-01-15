
'''
This is based The Venetian Casino in Las Vegas
Rules for baccarat can be found on https://www.venetianlasvegas.com/resort/casino/table-games/how-to-play-baccarat.html
This is going to be used to simulate the game along with test the Martingale strategy
'''

import random

#set up initial deck shuffle and card burn
def deal(num_decks = 8):
    deck = [1,2,3,4,5,6,7,8,9,0,0,0,0] * 4
    deck = deck * num_decks
    random.shuffle(deck)
    random.shuffle(deck)
    random.shuffle(deck)
    value = deck.pop()
    if value == 0:
        value = 10
    for i in range(value):
        value = deck.pop()
    return deck

def baccarat(deck:list, discard:list, selection = "player", bet = 25):
    #print(deck)
    #random.shuffle(deck)
    #print(deck)

    player = []
    banker = []
    winner = None
    player_value = 0
    banker_value = 0

    if len(deck) == 0:
        print("shuffle")
#initial flop    
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

    print("players value is",player_value)
    print("bankers value is",banker_value)
    print('\n')


#if banker or player has 8 or 9 and the other does not
    if banker_value in [8, 9] or player_value in [8, 9]:
        winner = "banker" if banker_value > player_value else "player"
#if player hand is less than 6
    elif player_value < 6:
        player.append(deck.pop())
        print("player flipped a", player[2])
    #once the player draws a card this 3rd card determines what the banker does
        #banker always draws if banker value is between 0-2
        if banker_value < 3:
            banker.append(deck.pop())
            print("banker flipped a", banker[2])
        #banker draws on value of 3 if players 3rd card is not an 8
        elif banker_value == 3 and player[2] != 8:
            banker.append(deck.pop())
            print("banker flipped a", banker[2])
        #banker draws on value of 4 if players card is between 2-7
        elif banker_value == 4 and (player[2] > 1 and player[2] < 8):
            banker.append(deck.pop())
            print("banker flipped a", banker[2])
        #banker draws on value of 5 if players card is between 4-7
        elif banker_value == 5 and (player[2] > 3 and player[2] < 8):
            banker.append(deck.pop())
            print("banker flipped a", banker[2])
        #banker draws on value of 6 if players card is between 6-7
        elif banker_value == 6 and (player[2] > 5 and player[2] < 8):
            banker.append(deck.pop())
            print("banker flipped a", banker[2])
#if banker hand is less than 6 and player does not have 3rd card
    elif banker_value < 6:
        banker.append(deck.pop())
        print("banker flipped a", banker[2])
        

    banker_value = sum(banker)
    banker_value = banker_value % 10
    player_value = sum(player)
    player_value = player_value % 10
    #print("bankers value is",banker_value)
    print('\n')
    print("players value is",player_value)
    print("bankers value is",banker_value)
    
    if banker_value == player_value:
        winner = "push"
    elif banker_value > player_value:
        winner = "banker"
    else: winner = "player"

    if winner == "push":
        print("YOU PUSHED")
        return None, winner, bet
    elif winner == selection:
        print("YOU WIN!!!")
        return True, winner, bet*2
    else: 
        print("YOU LOSE!!")
        return False, winner, 0


#print(baccarat("banker"))
#deck = [1,2,3,4,5,6,7,8,9,0,0,0,0] * 4
#deck = deck * 8
#print(deck)
#print(len(deck))
#discard = []
#print(baccarat(deck,discard,"banker", 25))
#print(len(deck))

    

