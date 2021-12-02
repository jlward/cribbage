class ComputerPlayer:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def __str__(self):
        return f'{self.name} {self.hand}'

    @property
    def hand_count(self):
        return len(self.hand)

    def add_to_hand(self, card):
        self.hand.append(card)

    def discard_to_crib(self):
        cards = [
            self.hand.pop(0),
            self.hand.pop(0),
        ]
        return cards

    def play_card(self, current_count):
        self.hand.sort(reverse=True)
        for card in self.hand:
            if card.value + current_count <= 31:
                self.hand.remove(card)
                return card
