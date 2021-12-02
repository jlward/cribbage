class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        return f'{self.number} {self.suit}'

    def __repr__(self):
        return str(self)
