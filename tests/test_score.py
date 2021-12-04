from unittest import TestCase

from card import Card
from score import Score


class PointsTestCase(TestCase):
    def test_flush(self):
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
