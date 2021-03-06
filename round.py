import random

from deck import Deck
from score import ScoreHand, ScorePegging


class Round:
    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.crib = []
        self.cards_played = []

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
        if self.cut_card.number == 11:
            self.players[0].add_points(2)
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
                    print('    ', player.name, card, count)
                    self.cards_played.append(card)
                    self.check_for_pegging(player)
                if not card_played:
                    break

    def check_for_pegging(self, player):
        score = ScorePegging(self.cards_played)
        player.add_points(score.score())

    def score_hands(self):
        for player in self.players:
            player.score_hand(self.cut_card)

    def count_crib(self):
        score = ScoreHand(
            cards=self.crib,
            cut_card=self.cut_card,
            is_crib=True,
        )
        self.players[0].add_points(score.score_hand())

    def start(self):
        print('Starting round')

        print('  Dealing cards')
        for player in self.players:
            self.deck.deal_to_player(player)

        for player in self.players:
            self.discard_to_crib(player)
        print(' ', self.players)

        self.get_cut_card()
        self.play_cards()
        self.score_hands()
        self.count_crib()
