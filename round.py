import random
from deck import Deck


class Round:
    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.crib = []

    def discard_to_crib(self, player):
        self.crib.extend(player.discard_to_crib())

    @property
    def players_have_cards(self):
        for player in self.players:
            if player.hand_count:
                return True
        return False

    def get_cut_card(self):
        self.cut_card = random.choice(self.deck.cards)
        self.deck.cards.remove(self.cut_card)

    def play_cards(self):
        while self.players_have_cards:
            count = 0
            while count <= 31:
                card_played = False
                for player in self.players:
                    card = player.play_card(current_count=count)
                    if card is None:
                        continue
                    count += card.value
                    card_played = True
                    print(player, card, count)
                if not card_played:
                    break

    def print_players(self):
        for player in self.players:
            print(player)

    def score_hands(self):
        for player in self.players:
            player.score_hand(self.cut_card)

    def count_crib(self):
        pass

    def start(self):
        print('Starting round')

        print('Dealing cards')
        for player in self.players:
            self.deck.deal_to_player(player)

        for player in self.players:
            self.discard_to_crib(player)

        self.get_cut_card()
        self.play_cards()
        self.score_hands()
        self.print_players()
        self.count_crib()
        self.print_players()
