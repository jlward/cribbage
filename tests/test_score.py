from unittest import TestCase

from card import Card
from score import ScoreHand, ScorePegging


class ScoreHandTestCase(TestCase):
    def test_flush_not_crib(self):
        cards = [
            Card(number=1, suit='a'),
            Card(number=2, suit='a'),
            Card(number=3, suit='a'),
            Card(number=4, suit='a'),
        ]

        cut_card = Card(
            number=5,
            suit='a',
        )
        score = ScoreHand(cards, cut_card)
        self.assertEqual(score.check_for_flush(), 5)
        cut_card.suit = 'b'
        self.assertEqual(score.check_for_flush(), 4)
        cards[0].suit = 'b'
        cut_card.suit = 'a'
        self.assertEqual(score.check_for_flush(), 0)

    def test_flush_crib(self):
        cards = [
            Card(number=1, suit='a'),
            Card(number=2, suit='a'),
            Card(number=3, suit='a'),
            Card(number=4, suit='a'),
        ]

        cut_card = Card(
            number=5,
            suit='a',
        )
        score = ScoreHand(cards, cut_card, is_crib=True)
        self.assertEqual(score.check_for_flush(), 5)
        cut_card.suit = 'b'
        self.assertEqual(score.check_for_flush(), 0)
        cards[0].suit = 'b'
        cut_card.suit = 'a'
        self.assertEqual(score.check_for_flush(), 0)

    def test_check_for_straight(self):
        cards = [
            Card(number=1, suit='a'),
            Card(number=2, suit='a'),
            Card(number=3, suit='a'),
            Card(number=4, suit='a'),
        ]

        cut_card = Card(
            number=5,
            suit='a',
        )
        score = ScoreHand(cards, cut_card)
        self.assertEqual(score.check_for_straight(), 5)
        cards[2].number = 9
        self.assertEqual(score.check_for_straight(), 0)
        cards[2].number = 3
        cards[3].number = 5
        self.assertEqual(score.check_for_straight(), 3)
        cards[3].number = 3
        self.assertEqual(score.check_for_straight(), 6)

    def test_check_for_pairs(self):
        cards = [
            Card(number=1, suit='a'),
            Card(number=2, suit='a'),
            Card(number=3, suit='a'),
            Card(number=4, suit='a'),
        ]

        cut_card = Card(
            number=5,
            suit='a',
        )
        score = ScoreHand(cards, cut_card)
        self.assertEqual(score.check_for_pairs(), 0)
        cut_card.number = 1
        self.assertEqual(score.check_for_pairs(), 2)
        cards[1].number = 1
        self.assertEqual(score.check_for_pairs(), 6)
        cards[3].number = 3
        self.assertEqual(score.check_for_pairs(), 8)

    def test_check_for_15s(self):
        cards = [
            Card(number=1, suit='a'),
            Card(number=1, suit='a'),
            Card(number=3, suit='a'),
            Card(number=4, suit='a'),
        ]

        cut_card = Card(
            number=5,
            suit='a',
        )
        score = ScoreHand(cards, cut_card)
        self.assertEqual(score.check_for_15s(), 0)
        cards[1].number = 2
        self.assertEqual(score.check_for_15s(), 2)
        for card in cards:
            card.number = 5
        cut_card.number = 12
        self.assertEqual(score.check_for_15s(), 16)

    def test_check_for_nobs(self):
        cards = [
            Card(number=1, suit='a'),
            Card(number=1, suit='a'),
            Card(number=3, suit='a'),
            Card(number=4, suit='a'),
        ]

        cut_card = Card(
            number=5,
            suit='a',
        )
        score = ScoreHand(cards, cut_card)
        self.assertEqual(score.check_for_nobs(), 0)
        cards[0].number = 11
        self.assertEqual(score.check_for_nobs(), 1)
        cut_card.suit = 'b'
        self.assertEqual(score.check_for_nobs(), 0)

    def test_score_hand(self):
        cards = [
            Card(number=1, suit='a'),
            Card(number=1, suit='a'),
            Card(number=3, suit='a'),
            Card(number=4, suit='a'),
        ]

        cut_card = Card(
            number=5,
            suit='a',
        )
        score = ScoreHand(cards, cut_card)
        self.assertEqual(score.score_hand(), 10)


class ScorePeggingTestCase(TestCase):
    def test_magic_numbers_15(self):
        cards = [
            Card(number=10, suit='a'),
            Card(number=5, suit='a'),
        ]
        score = ScorePegging(cards)
        self.assertEqual(score.check_for_magic_numbers(), True)
        cards[0].number = 12
        self.assertEqual(score.check_for_magic_numbers(), True)
        cards[0].number = 4
        self.assertEqual(score.check_for_magic_numbers(), False)

    def test_magic_numbers_31(self):
        cards = [
            Card(number=10, suit='a'),
            Card(number=11, suit='a'),
            Card(number=12, suit='a'),
            Card(number=1, suit='a'),
        ]
        score = ScorePegging(cards)
        self.assertEqual(score.check_for_magic_numbers(), True)
        cards[0].number = 8
        self.assertEqual(score.check_for_magic_numbers(), False)

    def test_check_for_pair_points(self):
        cards = [
            Card(number=10, suit='a'),
            Card(number=11, suit='a'),
            Card(number=12, suit='a'),
            Card(number=1, suit='a'),
        ]
        score = ScorePegging(cards)
        self.assertEqual(score.check_for_pair_points(), 0)
        cards[3].number = 12
        self.assertEqual(score.check_for_pair_points(), 2)
        cards[1].number = 12
        self.assertEqual(score.check_for_pair_points(), 6)
        cards[0].number = 12
        self.assertEqual(score.check_for_pair_points(), 12)

    def test_check_for_straight_random_outside(self):
        cards = [
            Card(number=10, suit='a'),
            Card(number=12, suit='a'),
        ]
        score = ScorePegging(cards)
        self.assertEqual(score.check_for_straight_points(), 0)
        cards.append(
            Card(number=11, suit='a'),
        )
        self.assertEqual(score.check_for_straight_points(), 3)
        cards.append(
            Card(number=9, suit='a'),
        )
        self.assertEqual(score.check_for_straight_points(), 4)
        cards[1].number = 2
        self.assertEqual(score.check_for_straight_points(), 0)

    def test_check_for_straight_inside_with_other_straights(self):
        cards = [
            Card(number=1, suit='a'),
            Card(number=2, suit='a'),
            Card(number=3, suit='a'),
            Card(number=5, suit='a'),
            Card(number=6, suit='a'),
            Card(number=7, suit='a'),
        ]
        score = ScorePegging(cards)
        self.assertEqual(score.check_for_straight_points(), 3)
        cards.append(
            Card(number=4, suit='a'),
        )
        self.assertEqual(score.check_for_straight_points(), 7)

    def test_score_magic_numbers(self):
        cards = [
            (10, 0),
            (5, 2),
            (10, 0),
            (6, 2),
        ]
        stack = []
        for number, expected_points in cards:
            stack.append(Card(number=number, suit='a'))
            score = ScorePegging(stack)
            self.assertEqual(score.score(), expected_points)

    def test_score_pairs(self):
        cards = [
            (10, 0),
            (10, 2),
            (10, 6),
        ]
        stack = []
        for number, expected_points in cards:
            stack.append(Card(number=number, suit='a'))
            score = ScorePegging(stack)
            self.assertEqual(score.score(), expected_points)

    def test_score_striaghts(self):
        cards = [
            (1, 0),
            (2, 0),
            (3, 3),
            (5, 0),
            (6, 0),
            (4, 6),
        ]
        stack = []
        for number, expected_points in cards:
            stack.append(Card(number=number, suit='a'))
            score = ScorePegging(stack)
            self.assertEqual(score.score(), expected_points)
