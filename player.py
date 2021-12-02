class ComputerPlayer:
    def __init__(self):
        self.hand = []

    def add_to_hand(self, card):
        self.hand.append(card)

    def discard_to_crib(self):
        cards = [
            self.hand.pop(0),
            self.hand.pop(0),
        ]
        return cards
