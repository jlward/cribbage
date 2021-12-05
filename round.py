import random

from deck import Deck
from score import Score


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
                    print(player, card, count)
                    self.cards_played.append(card)
                    self.check_for_pegging(player)
                if not card_played:
                    break

    def print_players(self):
        for player in self.players:
            print(player)

    def check_for_magic_numbers(self):
        count = sum(card.value for card in self.cards_played)
        if count == 15:
            return True
        if count == 31:
            return True
        return False

    def check_for_pair_points(self):
        last_card = self.cards_played[-1]
        num_pairs = 1
        for card in self.cards_played[-2::-1]:
            if card == last_card:
                num_pairs += 1
            else:
                break
        return num_pairs * (num_pairs - 1)

    def _check_for_straight(self, cards):
        current = cards[0].value
        for card in cards[1:]:
            if current + 1 != card.value:
                return False
            current = card.value
        return True

    def check_for_straight_points(self):
        if len(self.cards_played) < 3:
            return 0
        last_cards = []
        longest_straight = 0
        for card in self.cards_played[::-1]:
            last_cards.append(card)
            if len(last_cards) < 3:
                continue
            last_cards.sort()
            if not self._check_for_straight(last_cards):
                break
            longest_straight = len(last_cards)
        return longest_straight

    def check_for_pegging(self, player):
        if self.check_for_magic_numbers():
            player.add_points(2)
        pair_points = self.check_for_pair_points()
        if pair_points:
            player.add_points(pair_points)
        straight_points = self.check_for_straight_points()
        if straight_points:
            player.add_points(straight_points)

    def score_hands(self):
        for player in self.players:
            player.score_hand(self.cut_card)

    def count_crib(self):
        score = Score(
            cards=self.crib,
            cut_card=self.cut_card,
            is_crib=True,
        )
        self.players[0].add_points(score.score_hand())

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
