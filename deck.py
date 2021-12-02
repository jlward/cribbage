import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        for number in range(1, 14):
            for suit in '♣♦♥♠':
                self.cards.append(Card(
                    number=number,
                    suit=suit,
                ))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_to_player(self, player):
        print(player)
        for _ in range(6):
            card = self.cards.pop(0)
            player.add_to_hand(card)
            print(card)
