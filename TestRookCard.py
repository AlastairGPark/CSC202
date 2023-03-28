#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  TestRookCard.py: tests for RookCard
#  
#  Copyright 2023 Peter Brown <peter.brown@converse.edu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

import unittest
from AbstractCardExam1 import AbstractCard
from RookCard import RookCard
from PlayingCardExam1 import PlayingCard

class TestRookCard(unittest.TestCase):
    """Unit tests for the RookCard class."""

    def setUp(self) -> None:
        self.colorSuits: tuple[str, ...] = ('Black', 'Green', 'Red', 'Yellow')
        self.colorRanks: tuple[str,...] = tuple(map(str, range(1, 15)))
        rookSuitlist: list[str] = [x for x in RookCard.SUITS if x not in self.colorSuits]
        assert len(rookSuitlist) == 1
        
        rookRanklist: list[str] = [x for x in RookCard.RANK_NAMES[1:] if x not in self.colorRanks]
        assert len(rookRanklist) == 1
        
        self.rookRank: str = rookRanklist[0]
        self.rookSuit: str = rookSuitlist[0]
        self.bird = RookCard(self.rookRank, self.rookSuit)

    # Test whether constructor raises exceptions when asked to make 
    #    cards with invalid combinations of rank and suit
    def testConstructorRookNonBird(self) -> None:
        for rank in self.colorRanks:
            with self.subTest(rank=rank):
                with self.assertRaises(AssertionError):
                    RookCard(self.rookSuit, rank)

    def testConstructorColorBird(self) -> None:
        for suit in self.colorSuits:
            with self.subTest(suit=suit):
                with self.assertRaises(AssertionError):
                    RookCard(suit, self.rookRank)

    def testConstructorFlakyRank(self) -> None:
        with self.assertRaises(AssertionError):
            RookCard('0', 'Green')

    def testConstructorFlakySuit(self) -> None:
        with self.assertRaises(AssertionError):
            RookCard('5', 'Elderberries')

    # Test rankName()
    def testRankName(self) -> None:
        for rank in self.colorRanks:
            with self.subTest(rank=rank):
                self.assertEqual(RookCard(rank, 'red').rankName(), rank)
        self.assertEqual(self.bird.rankName(), self.rookRank)

    # Test suitName()
    def testSuitName(self) -> None:
        for suit in self.colorSuits:
            with self.subTest(suit=suit):
                self.assertEqual(RookCard('5', suit).suitName(), suit)
        self.assertEqual(self.bird.suitName(), self.rookSuit)
        
    # Test conversion to string
    def testStr(self) -> None:
        for rank in self.colorRanks:
            for suit in self.colorSuits:
                with self.subTest(case=suit+str(rank)):
                    self.assertEqual(str(RookCard(rank, suit)), \
                                     suit.capitalize() + ' ' + rank.capitalize())
        self.assertEqual(str(self.bird), 'Rook Bird')
    
    # Test comparisons between cards

    # Test whether the cards that *should* be equal actually *are* equal
    def testEqual(self) -> None:
        for rank1 in self.colorRanks:
            with self.subTest(rank1=rank1):
                for suit1 in self.colorSuits:
                    with self.subTest(suit1=suit1):
                        card1 = RookCard(rank1, suit1)
                        # Check NotImplemented.  It should fall back to object.__eq__()
                        self.assertFalse(card1 == 'some other value')

                        # Verify that unrelated cards aren't equal
                        try: # catch any thrown exceptions from in here
                            regRank:str = PlayingCard.RANK_NAMES[RookCard.RANK_NAMES.index(rank1)]
                            regSuit:str = PlayingCard.SUITS[RookCard.SUITS.index(suit1)]
                            regCard: PlayingCard = PlayingCard(regRank, regSuit)
                        except:
                            regCard = PlayingCard('5', 'Hearts')
                        self.assertFalse(card1 == regCard)

                        # Verify that none of the color cards are equal to the Rook Bird
                        self.assertFalse(card1 == self.bird)
                        self.assertFalse(self.bird == card1)
                        # Check equality with all the color cards
                        for rank2 in self.colorRanks:
                            with self.subTest(rank2=rank2):
                                for suit2 in self.colorSuits:
                                    with self.subTest(suit2=suit2):
                                        card2 = RookCard(rank2, suit2)
                                        self.assertFalse(card1 is card2) # Different objects
                                        self.assertEqual((card1 == card2), \
                                            (rank1 == rank2 and suit1 == suit2))

        self.assertEqual(self.bird, RookCard(self.rookRank, self.rookSuit))

    # Test for correct ordering
    def testLT(self) -> None:
        for rank1 in self.colorRanks:
            with self.subTest(rank1=rank1):
                for suit1 in self.colorSuits:
                    with self.subTest(suit1=suit1):
                        card1 = RookCard(rank1, suit1)
                        
                        # Everything's less than the Rook Bird
                        self.assertTrue(card1 < self.bird)
                        self.assertFalse(self.bird < card1)

                        # Check ordering with respect to all other cards
                        for rank2 in self.colorRanks:
                            with self.subTest(rank2=rank2):
                                for suit2 in self.colorSuits:
                                    with self.subTest(suit2=suit2):
                                        card2 = RookCard(rank2, suit2)
                                        if RookCard.RANK_NAMES.index(rank1) < RookCard.RANK_NAMES.index(rank2):
                                            self.assertTrue(card1 < card2)
                                        elif rank1 == rank2:
                                            self.assertEqual(card1 < card2, 
                                                             RookCard.SUITS.index(suit1) 
                                                             < RookCard.SUITS.index(suit2))
                                        else: # rank2 < rank1
                                            self.assertFalse(card1 < card2)                        
        self.assertFalse(self.bird < RookCard(self.rookRank, self.rookSuit))

    # Test makeDeck
    def testMakeDeck(self) -> None:
        cards: list[AbstractCard] = RookCard.makeDeck()
        self.assertEqual(len(cards), 57)
        for rank in self.colorRanks:
            with self.subTest(rank=rank):
                for suit in self.colorSuits:
                    with self.subTest(suit=suit):
                        c: RookCard = RookCard(rank, suit)
                        self.assertEqual(cards.count(c), 1)
        self.assertEqual(cards.count(self.bird), 1)
    
if __name__ == '__main__':
    unittest.main()
