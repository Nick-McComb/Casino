
'''In the future add a loop for 100x then track the avg hands before loss, avg hands won, avg money won, and avg overall profit'''

import random
from Baccarat import baccarat
from Baccarat import deal

def martinagale(money = 1600, base_bet =25, num_decks = 8, selection = "player"):
    #deck = [1,2,3,4,5,6,7,8,9,0,0,0,0] * 4
    #deck = deck * num_decks
    discard = []
    hands = 0
    profit = 0
    winner = True
    loses = 0
    bet = base_bet
    original_money = money
    while winner:
        deck = deal()
        while len(deck) > 10:
            print("\n")
            print(selection)
            print("THIS IS THE BET", bet)
            print(deck)
            results = baccarat(deck, discard, selection, bet)
            print(results)
            hands +=1
            money -= bet 
            print("HEREEEE",money)
            
    
            if results[0]:
                profit += base_bet
                money = original_money
                bet = base_bet
                loses = 0
                selection = "player"

            elif results[0] == None:
                money += bet 

            else:
                loses +=1
                #money -= bet   
                bet *=2 
                if money < bet:
                    winner = False
                    break
                if loses in [1, 4, 5]:
                    selection = "banker"
                elif loses in [2, 3, 6]:
                    selection = "player"
            print("END HAND", money, "PROF", profit)

            
    
    return money, hands, profit
#print(deal())

print(martinagale(1600, 25))


