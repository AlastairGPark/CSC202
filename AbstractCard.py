import abc
from typing import cast

class AbstractCard(abc.ABC):
    """Abstract base class for cards that are represented by rank and suit.
    Rank and suit are represented internally as integers, but externally as strings.
    The class keeps the names of ranks and classes in tuples of strings."""

    # Subclasses should override at least SUITS, RANK_NAMES, and _TOP_RANK
    SUITS: tuple[str, ...] = tuple()
    RANK_NAMES: tuple[str, ...] = tuple()
    _BOTTOM_RANK: int = 0
    _TOP_RANK: int = len(RANK_NAMES) - 1
    _RANKS: tuple[int, ...] = tuple(range(_BOTTOM_RANK, _TOP_RANK+1))

    def _invariant(self) -> bool:
        """Class invariant."""
        return (0 <= self._suit < len(self.SUITS)) and \
            (self._BOTTOM_RANK <= self._rank <= self._TOP_RANK)

    def __init__(self, rank: str, suit: str):
        """Create an AbstractCard of a given suit and rank."""
        # Pre:
        assert suit.capitalize() in self.SUITS and \
            rank.capitalize() in self.RANK_NAMES
        self._suit: int = self.SUITS.index(suit.capitalize())
        self._rank: int = self.RANK_NAMES.index(rank.capitalize())
        # Post:
        assert self._invariant()

    def suitName(self) -> str:
        """Given a PlayingCard, return the name of its suit."""
        return self.SUITS[self._suit]

    def rankName(self) -> str:
        """Given a PlayingCard, return its rank as a string."""
        return self.RANK_NAMES[self._rank]

    def __lt__(self, other: 'AbstractCard') -> bool:
        """Return True if self < other. Implements a war-style ordering where
        ranks are compared first and suits are compared only if ranks are equal.
        This relationship is only defined if the types of self and other are hierarchically
        related; that is either the types are the same or there's an ancestor-descendant
        relationship between them."""
        #Pre:
        assert self._invariant and other._invariant

        #If no ancestor-descendant relationship, return NotImplemented
        if (not (isinstance(self, other.__class__))) \
            and (not (isinstance(other, self.__class__))):
            return NotImplemented
        #Compare Ranks
        elif self._rank < other._rank:
            return True
        elif other._rank < self._rank:
            return False
        #self._rank == other._rank
        else: 
            return self._suit < other._suit

    def __eq__(self, other: object) -> bool:
        """Return True iff the PlayingCards have the same rank and suit."""
        # Pre:
        assert self._invariant()

        if not isinstance(other, AbstractCard):
            return NotImplemented
        else:
            return (self.rankName() == other.rankName()) and \
                (self.suitName() == other.suitName())

    def __str__(self) -> str:
        """Return a string representation of this AbstractCard."""
        return (self.suitName() + ' ' + self.rankName()).strip()

    # Subclasses need to override
    @classmethod
    @abc.abstractmethod
    def makeDeck(cls) -> list['AbstractCard']:
        """Makes an entire deck of this kind of card, and returns it as a list."""
