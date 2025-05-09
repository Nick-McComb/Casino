
'''
This is based The Venetian Casino in Las Vegas
Rules for baccarat can be found on https://www.venetianlasvegas.com/resort/casino/table-games/how-to-play-baccarat.html
This is going to be used to simulate the game along with test the Martingale strategy
'''

import random

#set up initial deck shuffle and card burn
def deal(num_decks = 8):
    deck = [1,2,3,4,5,6,7,8,9,10,10,10,10] * 4
    deck = deck * num_decks
    #shuffle
    random.shuffle(deck)
    random.shuffle(deck)
    random.shuffle(deck)
    #cut the deck at random spot
    cut = random.randint(1,len(deck)-1)
    first_half = deck[:cut]
    second_half = deck[cut:]
    deck = second_half + first_half
    #remove first card then remove as many cards as the first card
    value = deck.pop()
    for i in range(value):
        value = deck.pop()
    return deck

#determines the winner of the game and return bet
def determine_winner(player_val, banker_val, selection, bet):
    if player_val == banker_val:
        return None, "push", bet
    winner = "player" if player_val > banker_val else "banker"
    won = selection == winner
    payout = bet * 2 if won else 0
    return won, winner, payout

#determines if banker should draw after player has already drawn
def should_banker_draw(banker_val, player_third):
    #once the player draws a card this 3rd card determines what the banker does
    #banker always draws if banker value is between 0-2
    if banker_val < 3:
        return True
    #banker draws on value of 3 if players 3rd card is not an 8
    if banker_val == 3:
        return player_third != 8
    #banker draws on value of 4 if players card is between 2-7
    if banker_val == 4:
        return 2 <= player_third <= 7
    #banker draws on value of 5 if players card is between 4-7
    if banker_val == 5:
        return 4 <= player_third <= 7
    #banker draws on value of 6 if players card is between 6-7
    if banker_val == 6:
        return 6 <= player_third <= 7
    return False

def draw_card(deck, hand, who):
    card = deck.pop()
    hand.append(card)
    print(f"{who} flipped a {card}")


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
    draw_card(deck, player, "player")
    draw_card(deck, banker, "banker")
    draw_card(deck, player, "player")
    draw_card(deck, banker, "banker")

    print('\n')

    banker_value = sum(banker)
    player_value = sum(player)

    banker_value = banker_value % 10
    player_value = player_value % 10

    print("players value is",player_value)
    print("bankers value is",banker_value)
    print('\n')


#if banker or player has 8 or 9 and the other does not
    if max(player_value, banker_value) >= 8:
        pass
#if player hand is less than 6
    elif player_value < 6:
        draw_card(deck, player, "player")
    #once the player draws a card this 3rd card determines what the banker does
        if should_banker_draw(banker_value, player[2]):
            draw_card(deck,banker,"banker")
#if banker hand is less than 6 and player does not have 3rd card
    elif banker_value < 6:
        draw_card(deck,banker,"banker")
        

    banker_value = sum(banker)
    banker_value = banker_value % 10
    player_value = sum(player)
    player_value = player_value % 10
    #print("bankers value is",banker_value)
    print('\n')
    print("players value is",player_value)
    print("bankers value is",banker_value)
    
    return determine_winner(player_value, banker_value, selection, bet)




#print(baccarat("banker"))
#deck = [1,2,3,4,5,6,7,8,9,0,0,0,0] * 4
#deck = deck * 8
#print(deck)
#print(len(deck))
#discard = []
#print(baccarat(deck,discard,"banker", 25))
#print(len(deck))

    

