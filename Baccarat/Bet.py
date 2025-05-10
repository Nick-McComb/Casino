

class Bet:
    def __init__(self, amount, selection):
        self._amount = amount
        self._selection = selection  # "player" or "banker"

    def __repr__(self):
        return f"Bet(amount={self._amount}, selection='{self._selection}')"

    def get_selection(self):
        return self._selection

    def get_amount(self):
        return self._amount
