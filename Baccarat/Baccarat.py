
'''
This is based The Venetian Casino in Las Vegas
Rules for baccarat can be found on https://www.venetianlasvegas.com/resort/casino/table-games/how-to-play-baccarat.html
This is going to be used to simulate the game along with test the Martingale strategy
'''

import random
from Player import Player

class Baccarat:
    """
    Baccarat class, starts game of baccarat
    initialized with a deck of cards, unshuffled
    """
    def __init__(self, num_decks = 8):
        self._num_decks = num_decks
        self._deck = self._initialize_deck()
        self._shuffle()
        self._players = [] #list of players
        self._winner = None
        

    #initializes the deck
    def _initialize_deck(self):
        return [1,2,3,4,5,6,7,8,9,10,10,10,10] * 4 * self._num_decks

    #set up initial deck shuffle and card burn
    def _shuffle(self):
        #shuffle
        random.shuffle(self._deck)
        random.shuffle(self._deck)
        random.shuffle(self._deck)
        #cut the deck at random spot
        cut = random.randint(1,len(self._deck)-1)
        #deck equals second half plus first half of the deck (cut the deck)
        self._deck = self._deck[cut:] + self._deck[:cut] 
        #remove first card then remove as many cards as the first card
        value = self._deck.pop()
        for i in range(value):
            value = self._deck.pop()

    #determines the winner of the game and return bet
    def _determine_winner(self, player_val, banker_val):
        if player_val == banker_val:
            self._winner = "push"
            return
        self._winner = "player" if player_val > banker_val else "banker"
            # won = player.get_selection() == self._winner
            # payout = player.get_bet() * 2 if won else 0

    def _make_payout(self):
        for player in self._players:
            bet = player.get_bet()
            if bet.get_selection() == self._winner:
                if self._winner == "banker":
                    # Typical baccarat banker bet pays 0.95:1
                    payout = int(bet.get_amount() * 1.95)
                else:
                    payout = bet.get_amount() * 2
                player.receive_payout(payout)
                print(f"{player.name} won {payout}")
            elif self._winner == "push":
                player.receive_payout(bet.get_amount())  # Return original bet
                print(f"{player.name} pushed and got their bet back.")
            else:
                print(f"{player.name} lost.")
            
            player.clear_bet()


    #determines if banker should draw after player has already drawn
    def _should_banker_draw(self, banker_val, player_third):
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

    def _draw_card(self, hand, who):
        card = self._deck.pop()
        hand.append(card)
        print(f"{who} flipped a {card}")


    def add_player(self, player):
        self._players.append(player)

    def deal(self):
        #print(deck)
        #random.shuffle(deck)
        #print(deck)
        
        player = []
        banker = []
        winner = None
        player_value = 0
        banker_value = 0

        if len(self._deck) < 10:
            self._deck = self._initialize_deck()
            self._shuffle()
    #initial flop    
        self._draw_card(player, "player")
        self._draw_card(banker, "banker")
        self._draw_card(player, "player")
        self._draw_card(banker, "banker")

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
            self._determine_winner(player_value, banker_value)
            self._make_payout()
            return self._winner, player, banker
    #if player hand is less than 6
        elif player_value < 6:
            self._draw_card(player, "player")
        #once the player draws a card this 3rd card determines what the banker does
            if self._should_banker_draw(banker_value, player[2]):
                self._draw_card(banker,"banker")
    #if banker hand is less than 6 and player does not have 3rd card
        elif banker_value < 6:
            self._draw_card(banker,"banker")
            

        banker_value = sum(banker)
        banker_value = banker_value % 10
        player_value = sum(player)
        player_value = player_value % 10
        #print("bankers value is",banker_value)
        print('\n')
        print("players value is",player_value)
        print("bankers value is",banker_value)
        
        self._determine_winner(player_value, banker_value)
        self._make_payout()
        
        return self._winner, player, banker # returns winner, players cards, bankers cards




#print(baccarat("banker"))
#deck = [1,2,3,4,5,6,7,8,9,0,0,0,0] * 4
#deck = deck * 8
#print(deck)
#print(len(deck))
#discard = []
#print(baccarat(deck,discard,"banker", 25))
#print(len(deck))

    

