from unittest import TestCase

from deck import Deck
from player import ComputerPlayer


class DeckTestCase(TestCase):
    def test_deck(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deal_to_player(self):
        player = ComputerPlayer(name='Jason')
        deck = Deck()
        deck.deal_to_player(player)
        self.assertEqual(len(deck.cards), 52 - 6)
        self.assertEqual(len(player.hand), 6)
