import itertools
from collections import Counter

from more_itertools import consecutive_groups


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

    def check_for_straight(self, cards):
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

    def check_for_pairs(self, cards):
        points = 0
        counts = Counter(card.number for card in cards)
        for value in counts.values():
            points += value * (value - 1)
        return points

    def check_for_15s(self, cards):
        fifteens = [
            seq
            for i in range(1, len(cards) + 1)
            for seq in itertools.combinations(cards, i)
            if sum(card.value for card in seq) == 15
        ]
        return len(fifteens) * 2

    def check_for_flush(self, cards, cut_card):
        suits = [card.suit for card in cards]
        points = 0
        if len(set(suits)) != 1:
            return points
        points = 4
        if cut_card.suit == cards[0].suit:
            points += 1
        return points

    def check_for_nobs(self, cards, cut_card):
        jacks = [card for card in cards if card.number == 11]
        for jack in jacks:
            if jack.suit == cut_card.suit:
                return 1
        return 0

    def score_hand(self, cut_card):
        points = 0

        print(self.hand_copy, cut_card)
        points_from_run = self.check_for_straight(self.hand_copy + [cut_card])
        print('points_from_run', points_from_run)
        points += points_from_run

        points_from_pairs = self.check_for_pairs(self.hand_copy + [cut_card])
        print('points_from_pairs', points_from_pairs)
        points += points_from_pairs

        points_from_15s = self.check_for_15s(self.hand_copy + [cut_card])
        print('points_from_15s', points_from_15s)
        points += points_from_15s

        points_from_flush = self.check_for_flush(self.hand_copy, cut_card)
        print('points_from_flush', points_from_flush)
        points += points_from_flush

        points_from_nobs = self.check_for_nobs(self.hand_copy, cut_card)
        print('points_from_nobs', points_from_nobs)
        points += points_from_nobs

        self.score += points
        return points
