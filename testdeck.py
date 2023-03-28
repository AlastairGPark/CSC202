# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from AbstractCard import AbstractCard
from deck import Deck
from PlayingCard import PlayingCard
from UnoCard import UnoCard

class TestDeck(unittest.TestCase):
    # setup is run before every actual test
    def setUp(self) -> None:
        self.emptydeck = Deck([])
    # All methods whose names start with "test"
    # will be treated as tests
    def testLen(self) -> None:
        self.assertEqual(len(Deck([])), 0)
        deck: Deck = Deck(PlayingCard.makeDeck())
        self.assertEqual(len(deck), 52)
        deck = Deck(UnoCard.makeDeck())
        self.assertEqual(len(deck), 108) # Or it would be if UnoDeck.makeDeck() had been implemented
    
    def testContains(self) -> None:
        card: PlayingCard = PlayingCard('King', 'Spades')
        self.assertFalse(card in Deck([]))
        self.assertTrue(card in Deck(PlayingCard.makeDeck()))
        # Exclude the king of spades from the deck
        self.assertFalse(card in Deck(PlayingCard.makeDeck()[:-1]))

    def testDeal(self) -> None:
        card: PlayingCard = PlayingCard('King', 'Spades')
        deck: Deck = Deck(PlayingCard.makeDeck())
        self.assertTrue(len(deck) == 52 and card in deck)
        self.assertEqual(deck.deal(), card)
        self.assertEqual(len(deck), 51)
        self.assertFalse(card in deck)

    # Polymorphism!
    def testStr(self) -> None:
        # Deck contains *both* PlayingCards and UnoCards
        cards: list[AbstractCard] = PlayingCard.makeDeck() + UnoCard.makeDeck()
        deck: Deck = Deck(cards)
        self.assertEqual(len(deck), 160)

        # Each card converts itself to a string correctly, depending on its type
        print(str(deck))
        for i in range(159, -1, -1): # Backwards through the deck
            card: AbstractCard = deck.deal()
            # Polymorphic, again
            self.assertEqual(str(card), str(cards[i]))

    def testaddTop(self) -> None:
        card: PlayingCard = PlayingCard('Ace', 'Spades')
        deck: Deck = Deck(UnoCard.makeDeck())
        self.assertTrue(len(deck) == 108)
        self.assertFalse(card in deck)
        deck.addTop(card)
        self.assertTrue(len(deck) == 109 and card in deck)
        self.assertEqual(deck.deal(), card)
        self.assertTrue(len(deck) == 108)
        self.assertFalse(card in deck)


    def testaddBottom(self) -> None:
        card: PlayingCard = PlayingCard('Ace', 'Spades')
        deck: Deck = Deck(UnoCard.makeDeck())
        self.assertEqual(len(deck), 108)
        self.assertTrue(card not in deck)
        deck.addBottom(card)
        self.assertEqual(len(deck), 109)
        self.assertTrue(card in deck)
        for i in range(108):
            deck.deal()
        self.assertTrue(len(deck) == 1)
        self.assertTrue(card in deck)
        self.assertEqual(deck.deal(), card)

    def testPickCard(self) -> None:
        self.assertEqual(len(self.normalDeck), 52)
        card: AbstractCard = self.normalDeck.pickACard()
        self.assertEqual(len(self.normalDeck), 51)
        self.assertFalse(card in self.normalDeck)
        print('n', card)
        self.assertEqual(card, PlayingCard('7', 'Hearts'))
        


if __name__ == '__main__':
    unittest.main()