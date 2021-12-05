from unittest import TestCase

from card import Card


class CardTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.card = Card(number=1, suit='a')

    def test_str_is_same_as_repr(self):
        self.assertEqual(str(self.card), repr(self.card))

    def test_face_handles_numbers(self):
        self.assertEqual(self.card.face, 'A')

    def test_value_handles_face_cards(self):
        self.card.number = 15
        self.assertEqual(self.card.value, 10)
        self.card.number = 7
        self.assertEqual(self.card.value, 7)

    def test_card_can_be_check_for_less_than(self):
        card = Card(number=2, suit='a')
        assert card > self.card

    def test_card_equality(self):
        self.assertEqual(self.card, Card(number=1, suit='b'))
