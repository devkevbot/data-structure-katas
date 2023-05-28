from typing import Optional


class Queue:
    """
    A Queue backed by an array.
    """

    def __init__(self) -> None:
        self.data = []

    def __len__(self) -> int:
        return len(self.data)

    def enqueue(self, val: int) -> None:
        """
        Inserts a value at the end of the queue.

        Time: Amortized O(1)
        Space: O(1)
        """
        self.data.append(val)

    def dequeue(self) -> Optional[int]:
        """
        Removes the value at the front of the queue.

        Let n be the length of the queue.
        Time: O(n)
        Space: O(n)
        """
        if len(self) == 0:
            return None
        return self.data.pop(0)

    def peek_front(self) -> Optional[int]:
        """
        Peeks the value at the front of the queue.

        Time: O(1)
        Space: O(1)
        """
        if len(self) == 0:
            return None
        return self.data[0]
