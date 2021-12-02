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

    def play_card(self, current_count):
        self.hand.sort(reverse=True)
        for card in self.hand:
            if card.value + current_count <= 31:
                self.hand.remove(card)
                return card
