from AbstractCard import AbstractCard
from collections.abc import Iterable
import random

class Deck:
    """Class to represent a deck of cards.  As with most decks,
    this one is mutable."""

    def _invariant(self) -> bool:
        """Class invariant."""
        # Everything in the deck is an AbstractCard.  If we pay attention to mypy,
        # that will never be false, but there's really nothing else to check.
        valid: bool = True
        for card in self._cards:
            if not isinstance(card, AbstractCard):
                valid = False # mypy thinks this is unreachable (which it should be)
        return valid

    def __init__(self, cards: Iterable[AbstractCard]):
        """Create a deck from an iterable collection of AbstractCards."""
        self._cards: list[AbstractCard] = list(cards)
        # Post:
        assert self._invariant()

    # Mutation Methods

    def deal(self) -> AbstractCard:
        """Deal the card off the top of the deck."""
        # Top of the deck is the *end* of the list.
        # Pre:
        assert len(self._cards) > 0
        # For checking postcondition
        oldTopCard: AbstractCard = self._cards[-1]
        oldlen: int = len(self._cards)

        card: AbstractCard = self._cards.pop() # Do the actual dealing
        # Post:
        assert oldTopCard == card and len(self._cards) == (oldlen - 1)
        return card

    #def dealFromBottom(self) -> AbstractCard:
    #    pass

    def pickACard(self) -> AbstractCard:
        """Pick a random card from the deck, remove it from the deck, and return it to the deck"""
        return self._cards.pop(random)

    def shuffle(self) -> None:
        """Randomly reorder the deck in place"""
        for i in len(self):
            self._cards[i] = self._cards.pop(random.randrange(i, len(self)))

    # Query Methods

    def __len__(self) -> int:
        """Number of cards currently in the deck."""
        return len(self._cards)

    def __contains__(self, card: AbstractCard) -> bool:
        """Returns true if card is in the deck."""
        return (card in self._cards)

    def __str__(self) -> str:
        """Represent the Deck as a string."""
        result = 'Deck of {0} cards, listed bottom to top:\n'.format(len(self))
        for card in self._cards:
            result += '\t' + str(card) + '\n'
        return result

    def addTop(self, card: AbstractCard) -> None:
        self._cards.append(card)

    def addBottom(self, card: AbstractCard) -> None:
        self._cards.insert(0, card)
