from typing import Generic, TypeVar

T = TypeVar('T')

class CircQ(Generic[T]):
    """Class to represent a circular queue.  The queue is implemented as
    a Python list, but the head does not stay put; it moves through the
    list as items are removed.  The tail also moves through the list as
    items are added.  If the queue gets full, it will grow like a normal
    Python list, but this has to be done manually."""

    def _invariant(self) -> bool:
        """Class invariant."""
        valid: bool = True
        # for i in range(len(self._items)):
        #     valid = valid and (self._items[i] is not None)
        return valid
    
    def __init__(self):
        """Create an empty queue."""
        self._size = 2 # Initial size
        self._items: list[T|None] = [None, None]
        self._head: int = 0
        self._tail: int = 0
        assert self._invariant()

    def empty(self) -> bool:
        """Check whether the queue is empty."""
        return (self._head == self._tail and (self._items[self._tail] is None))
    
    def enqueue(self, item: T) -> None:  # O(1) amortized
        """Add an item to the tail of the queue."""
        if self._items[self._tail] is not None: # Queue is full
            self.resize()

        self._items[self._tail] = item
        self._tail += 1
        if self._tail == self._size:
            self._tail = 0
        assert self._invariant()

    def push(self, item: T) -> None: # O(1) amortized
        """Add an item to the tail of the queue (alternate name for the operation)."""
        self.enqueue(item)

    def dequeue(self) -> T: # O(1)
        """Remove and return the item at the head of the queue.
        The queue cannot be empty before doing this."""
        # Pre:
        assert not self.empty()
        item: T = self._items[self._head]
        self._items[self._head] = None
        self._head += 1
        if self._head == self._size:
            self._head = 0
        assert self._invariant()
        return item

    def pop(self) -> T: # O(1)
        """Remove and return the item at the head of the queue.
        The queue cannot be empty before doing this.  pop() is an
        alternate name for dequeue()."""
        return self.dequeue()
    

    def resize(self) -> None:
        """Doubles the size of the queue."""
        newItems: list[T] = []
        # Reserve the correct number of slots
        for i in range(2 * self._size):
            newItems.append(None)
        # Copy across
        i: int = 0
        while self._items[self._head] is not None:
            newItems[i] = self._items[self._head]
            self._items[self._head] = None # Mark the slot as having been copied
            i += 1
            self._head += 1
            if self._head == self._size:
                self._head = 0
        # Set _items to newItems, set _head and _tail
        self._items = newItems
        self._head = 0
        self._tail = i
        self._size = 2 * self._size