from unittest import TestCase

from card import Card
from score import Score


class PointsTestCase(TestCase):
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
        score = Score(cards, cut_card)
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
        score = Score(cards, cut_card, is_crib=True)
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
        score = Score(cards, cut_card)
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
        score = Score(cards, cut_card)
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
        score = Score(cards, cut_card)
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
        score = Score(cards, cut_card)
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
        score = Score(cards, cut_card)
        self.assertEqual(score.score_hand(), 10)
