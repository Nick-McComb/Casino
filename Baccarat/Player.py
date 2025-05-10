
from Bet import Bet

class Player:

    def __init__(self, name, cash):
        self.name = name
        self._cash = cash
        self._bet = None
    
    def __repr__(self):
        return f"Player(name='{self.name}', cash={self._cash}, bet={self._bet})"

    def place_bet(self, amount, selection):
        #checks for valid amount
        if amount > self._cash:
            raise ValueError("Bet amount cannot exceed available cash")
        #checks for valid selection
        if selection not in ("player", "banker"):
            raise ValueError("Invalid selection. Choose 'player' or 'banker'.")
        self._bet = Bet(amount, selection)
        self._cash -= amount  # Subtract the bet amount from the player's cash

    def get_bet(self):
        return self._bet

    def get_cash(self):
        return self._cash

    def clear_bet(self):
        self._bet = None

    def receive_payout(self, payout):
        self._cash += payout


    
    


  

    
    
    
