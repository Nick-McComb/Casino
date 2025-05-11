
'''In the future add a loop for 100x then track the avg hands before loss, avg hands won, avg money won, and avg overall profit'''

import random
from Baccarat import Baccarat
from Player import Player
#from Baccarat import deal

#test
#this is a test function to test the martingale strategy in baccarat
def martinagale(money = 1600, base_bet =25, num_decks = 8, selection = "player"):
    #deck = [1,2,3,4,5,6,7,8,9,0,0,0,0] * 4
    #deck = deck * num_decks
    hands = 0
    loses = 0
    profit = 0
    winner = True
    original_money = money
    bet = base_bet

    game = Baccarat(num_decks)
    Nick = Player("Nick", money)
    game.add_player(Nick)

    while winner:
    
        print(f"\nSelection: {selection}")
        print(f"Current Bet: {bet}")
        
        try:
            Nick.place_bet(bet, selection)
        except ValueError:
            print("Not enough cash to place bet.")
            break
        
        result = game.deal()
        
        hands += 1
        winner = result[0]
        money -= bet
        

        if winner == selection:
            profit += base_bet
            money = original_money
            bet = base_bet
            loses = 0
            selection = "player"

        elif winner == "push":
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
        

        print(f"End of Hand {hands} | Cash: {money} | Profit: {profit}")

            
    
    return hands, profit
#print(deal())


hands_avg = 0
profit_avg = 0
for i in range(100):
    
    attempt = martinagale(400, 25)
    hands_avg += attempt[0]
    profit_avg += attempt[1]

hands_avg /= 100
profit_avg /= 100
print(hands_avg, profit_avg)

#144.6 1605.0
#156.24 1752.75
#134.82 1493.0