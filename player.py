from score import Score


class ComputerPlayer:
    def __init__(self, name):
        self.hand = []
        self.hand_copy = []
        self.name = name
        self.score = 0

    def __str__(self):
        return f'{self.name} {self.hand} {self.score}'

    @property
    def hand_count(self):
        return len(self.hand)

    def add_to_hand(self, card):
        self.hand.append(card)
        self.hand_copy.append(card)

    def discard_to_crib(self):
        cards = [
            self.hand.pop(0),
            self.hand.pop(0),
        ]
        for card in cards:
            self.hand_copy.remove(card)
        return cards

    def play_card(self, current_count):
        self.hand.sort(reverse=True)
        for card in self.hand:
            if card.value + current_count <= 31:
                self.hand.remove(card)
                return card

    def score_hand(self, cut_card):
        print(self)
        score = Score(
            cards=self.hand_copy,
            cut_card=cut_card,
        )
        points = score.score_hand()
        self.score += points
        return points
