from more_itertools import consecutive_groups
from collections import Counter


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
        biggest_run = max([
            list(group)
            for group in consecutive_groups(numbers)
        ], key=len)
        len_biggest_run = len(biggest_run)
        if len_biggest_run > 2:
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
        return 0

    def check_for_pairs(self, cards):
        points = 0
        counts = Counter(card.number for card in cards)
        for value in counts.values():
            points += value * (value - 1)
        return points

    def check_for_15s(self, cards):
        return 0

    def check_for_flush(self, cards):
        return 0

    def check_for_nobs(self, cards, cut_card):
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
        points += points_from_15s

        points_from_flush = self.check_for_flush(self.hand_copy + [cut_card])
        points += points_from_flush

        points_from_nobs = self.check_for_nobs(self.hand_copy, cut_card)
        points += points_from_nobs

        self.score += points
        return points
