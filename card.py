face_map = {
    1: 'A',
    11: 'J',
    12: 'Q',
    13: 'K',
}


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    @property
    def face(self):
        return face_map.get(self.number, self.number)

    def __str__(self):
        return f'{self.face}{self.suit}'

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.number == other.number

    @property
    def value(self):
        if self.number > 10:
            return 10
        return self.number
