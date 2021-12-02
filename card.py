class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        return f'{self.number} {self.suit}'

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.value < other.value

    @property
    def value(self):
        if self.number > 10:
            return 10
        return self.number
