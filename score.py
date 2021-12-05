import itertools
from collections import Counter

from more_itertools import consecutive_groups


class ScoreHand:
    def __init__(self, cards, cut_card, is_crib=False):
        self.cards = cards
        self.cut_card = cut_card
        self.is_crib = is_crib

    def check_for_straight(self):
        cards = self.cards + [self.cut_card]
        numbers = set(card.number for card in cards)
        numbers = sorted(list(numbers))
        biggest_run = max(
            [list(group) for group in consecutive_groups(numbers)],
            key=len,
        )
        len_biggest_run = len(biggest_run)
        if len_biggest_run < 3:
            return 0
        counts = Counter(card.number for card in cards)
        pair_counts = 0
        for number, count in counts.items():
            if number not in biggest_run:
                continue
            if count < 2:
                continue
            pair_counts += count
        if pair_counts == 0:
            return len_biggest_run
        return len_biggest_run * pair_counts

    def check_for_pairs(self):
        cards = self.cards + [self.cut_card]
        points = 0
        counts = Counter(card.number for card in cards)
        for value in counts.values():
            points += value * (value - 1)
        return points

    def check_for_15s(self):
        cards = self.cards + [self.cut_card]
        fifteens = [
            seq
            for i in range(1, len(cards) + 1)
            for seq in itertools.combinations(cards, i)
            if sum(card.value for card in seq) == 15
        ]
        return len(fifteens) * 2

    def check_for_flush(self):
        if self.is_crib:
            suits = set([card.suit for card in self.cards + [self.cut_card]])
            if len(suits) == 1:
                return 5
            return 0
        suits = [card.suit for card in self.cards]
        points = 0
        if len(set(suits)) != 1:
            return points
        points = 4
        if self.cut_card.suit == self.cards[0].suit:
            points += 1
        return points

    def check_for_nobs(self):
        jacks = [card for card in self.cards if card.number == 11]
        for jack in jacks:
            if jack.suit == self.cut_card.suit:
                return 1
        return 0

    def score_hand(self):
        print(self.cards, self.cut_card)
        points = 0
        points_from_run = self.check_for_straight()
        print('points_from_run', points_from_run)
        points += points_from_run

        points_from_pairs = self.check_for_pairs()
        print('points_from_pairs', points_from_pairs)
        points += points_from_pairs

        points_from_15s = self.check_for_15s()
        print('points_from_15s', points_from_15s)
        points += points_from_15s

        points_from_flush = self.check_for_flush()
        print('points_from_flush', points_from_flush)
        points += points_from_flush

        points_from_nobs = self.check_for_nobs()
        print('points_from_nobs', points_from_nobs)
        points += points_from_nobs

        return points


class ScorePegging:
    def __init__(self, cards_played):
        self.cards_played = cards_played

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

    def score(self):
        points = 0
        if self.check_for_magic_numbers():
            points += 2
        pair_points = self.check_for_pair_points()
        if pair_points:
            points += pair_points
        straight_points = self.check_for_straight_points()
        if straight_points:
            points += straight_points
        return points
