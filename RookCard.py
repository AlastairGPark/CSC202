#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  RookCard.py
#  
#  Copyright 2021 phbrown <peter.brown@converse.edu>
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
#
import functools
from AbstractCardExam1 import AbstractCard

@functools.total_ordering
class RookCard(AbstractCard):
    """ Class to represent a Rook card."""
    colorSuits: tuple[str,...] = ('Black', 'Green', 'Red', 'Yellow')
    rookSuit: tuple[str] = ('Rook' ,) # Comma at the end tells Python this is a tuple
    SUITS: tuple[str,...] = colorSuits + rookSuit

    colorRanks: tuple[str, ...] = ('', '1', '2', '3', '4', 
                                     '5', '6', '7', '8', '9', 
                                     '10', '11', '12', '13', '14')
    rookRank: tuple[str, ...] = ('Bird', )
    RANK_NAMES: tuple[str, ...] = colorRanks + rookRank
    _TOP_COLOR_RANK: int = len(colorRanks) - 1
    _TOP_RANK: int = len(RANK_NAMES) - 1
    # _COLOR_RANKS: tuple[int, ...] = tuple(range(_TOP_COLOR_RANK + 1))
    # _BIRD_RANKS: tuple[int, ...] = tuple(range(_TOP_COLOR_RANK + 1, _TOP_RANK + 1))
    _BOTTOM_RANK: int = 1

    def _invariant(self) -> bool:
        """Class invariant."""
        # This UnoCard is a valid color card
        colorOK: bool = ((self._BOTTOM_RANK <= self._rank <= self._TOP_COLOR_RANK)
            and (self._suit < len(self.colorSuits)))

        # This UnoCard is a valid wild card
        birdOK: bool = ((self._TOP_COLOR_RANK < self._rank <= self._TOP_RANK))
           # and (len(self.colorSuits) <= self._suit < len(self.SUITS)))

        return ((colorOK and (not birdOK)) or (birdOK and (not colorOK)))

    def __init__(self, rank: str, suit: str):
        """Constructor"""
        # Pre:
        assert ((suit.capitalize() in self.colorSuits and 
                    rank.capitalize() in self.colorRanks) or 
                (suit.capitalize() in self.rookSuit and
                    rank.capitalize() in self.rookRank))
        super().__init__(rank, suit)

    @classmethod
    def makeDeck(cls) -> list[AbstractCard]:
        deck: list[AbstractCard] = []
        for suit in RookCard.SUITS:
            if suit in RookCard.colorSuits:
                for rank in RookCard.colorRanks[1:]:
                    deck.append(RookCard(rank, suit))
            else:
                for rank in RookCard.rookRank:
                    for i in range(1):
                        deck.append(RookCard(rank, suit))

        assert len(deck) == 57
        return deck