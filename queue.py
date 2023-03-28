from typing import Generic, TypeVar

T = TypeVar('T')

class Queue(Generic[T]):
    """Class to represent a queue.  The queue is implemented as
    a Python list, with the head of the queue at index 0 in the list
    and the tail of the queue at the end of the list."""

    def _invariant(self) -> bool:
        """Class invariant."""
        valid: bool = True
        for i in range(len(self._items)):
            valid = valid and (self._items[i] is not None)
        return valid
    
    def __init__(self):
        """Create an empty queue."""
        self._items: list[T] = []
        assert self._invariant()

    def empty(self) -> bool:
        """Check whether the queue is empty."""
        return (len(self._items) == 0)
    
    def enqueue(self, item: T) -> None:  # O(1)
        """Add an item to the tail of the queue."""
        self._items.append(item)
        assert self._invariant()

    def push(self, item: T) -> None: # O(1)
        """Add an item to the tail of the queue (alternate name for the operation)."""
        self.enqueue(item)

    def dequeue(self) -> T: # O(n).  Oops!
        """Remove and return the item at the head of the queue.
        The queue cannot be empty before doing this."""
        # Pre:
        assert not self.empty()
        item: T = self._items.pop(0)
        assert self._invariant()
        return item

    def pop(self) -> T: # O(n).  Oops!
        """Remove and return the item at the head of the queue.
        The queue cannot be empty before doing this.  pop() is an
        alternate name for dequeue()."""
        return self.dequeue()
