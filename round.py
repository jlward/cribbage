from deck import Deck


class Round:
    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.crib = []

    def discard_to_crib(self, player):
        self.crib.extend(player.discard_to_crib())

    def start(self):
        print('Starting round')

        print('Dealing cards')
        for player in self.players:
            self.deck.deal_to_player(player)

        for player in self.players:
            self.discard_to_crib(player)
        print(self.crib)
