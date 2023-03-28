from typing import cast, Generic, Optional, TypeVar

T = TypeVar('T')

class LList(Generic[T]):
    """Implement a linked list of items of type T.  The implementation here
    uses the following definition of a list:
    A list is:
        1.  An empty list, OR
        2.  A node followed by a list.
    To handle the first case, this list uses a sentinel node at the end of each
    list--that is, a node with the data and next both equal to None."""

    def _invariant(self) -> bool:
        """Class invariant."""
        valid: bool = True
        # Either this is a sentinel node...
        if self._next is None:
            valid = (self._data is None)
        else: # Or it's not a sentinel node
            valid = (isinstance(self._next, LList))
        return valid

    def __init__(self):
        """Create an empty list (i.e., a sentinel node)."""
        self._data: Optional[T] = None
        self._next: Optional[LList[T]] = None
        # Postcondition
        assert self._invariant()

    #### QUERY METHODS

    def is_empty(self) -> bool:
        """Return True iff this list is empty.  This method could as
        accurately be named is_sentinel(), because it returns True
        iff the current list is just a sentinal node."""
        # Pre:
        assert self._invariant()
        return self._next is None
    
    def __str__(self) -> str:
        """Represent this list as a string."""
        # Pre:
        assert self._invariant()
        result: str = ''
        if self.is_empty():
            result = '∅'
        else:
            result = '❬' + str(self._data) + '❭➞' + str(self._next)
        return result
    
    def size(self) -> int:
        """Return the number of items on the list."""
        # Pre:
        assert self._invariant()
        size: int = 0 # Already correct for empty list
        if not self.is_empty(): # Different if it's *not* the empty list
            size = 1 + self._next.size() # type: ignore
        return size

    # In Python terms, size() is __len__()
    def __len__(self) -> int:
        return self.size()
    
    def search(self, value: T) -> bool:
        """Search the list for VALUE.  Return True if it's present
        and False if it's not."""
        found: bool = False # Already correct for empty list
        if not self.is_empty(): # Different if *not* the empty list
            if self._data == value: # Found it!
                found = True
            else:
                found = self._next.search(value) # type: ignore
        return found

    # Again, translating to normal Python terms
    def __contains__(self, value: T) -> bool:
        return self.search(value)

    #### MUTATOR METHODS

    def add(self, item: T) -> None:
        """Adds ITEM to the front of the list."""
        # Pre:
        assert self._invariant()
        newNode: LList[T] = LList[T]() # type: ignore
        # Order is important!
        # *First*, copy self into newNode
        newNode._data = self._data
        newNode._next = self._next
        # *Then*, make self hold item
        self._data = item
        self._next = newNode
        # Post:
        assert self._invariant() and (self._data == item) and (self._next is newNode)

    def pop(self, pos: int = -1) -> Optional[T]:
        """Remove and return the item on the list at position POS.
        POS defaults to -1 (the last item).  This method handles
        negative indices in the usual Python way.  Assumes the list
        is not empty."""
        # Pre:
        assert self._invariant() and not self.is_empty() and \
            (-self.size() <= pos < self.size())
        result: Optional[T] = None
        # Negative pos
        if pos < 0:
            pos += self.size()
        assert 0 <= pos < self.size() # pos is no longer negative
        if pos == 0: # Delete the first node
            result = self._data # Keep the data to return it
            self._data = cast(LList[T], self._next)._data # Link around the next node
            self._next = cast(LList[T], self._next)._next
        else: # This is not the node you are looking for
            result = self._next.pop(pos - 1) # type: ignore
        return result

    def index(self, item: T) -> None:
        #Pre:
        if self.is_empty:
            return ValueError

    def insert(self, pos, item: T) -> None:
        #Pre:
        self.size() <= pos <= self.size()
        #Post
        if pos < 0:
            pos += self.size()
        assert 0 <= pos < self.size() # pos is no longer negative
        if pos == 0: # Delete the first node
            result = self._data # Keep the data to return it
            self._data = cast(LList[T], self._next)._data # Link around the next node
            self._next = cast(LList[T], self._next)._next
        else: # This is not the node you are looking for
            result = self._next.pop(pos - 1) # type: ignore
        return result
        

    def append(self, item: T) -> None:
        """Adds ITEM to the front of the list."""
        # Pre:
        assert self._invariant()
        newNode: LList[T] = LList[T]() # type: ignore
        # Order is important!
        # *First*, copy self into newNode
        newNode._data = self._data
        newNode._next = self._next
        # *Then*, make self hold item
        self._data = item
        self._next = newNode
        # Post:
        assert self._invariant() and (self._data == item) and (self._next is newNode)

    def remove(self, pos) -> None:
        assert self._invariant() and not self.is_empty() and \
            (-self.size() <= pos < self.size())