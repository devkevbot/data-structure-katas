from typing import Optional


class Stack:
    """
    A Stack is a last-in, first-out data structure.
    """

    def __init__(self) -> None:
        self.data = []

    def __len__(self) -> int:
        return len(self.data)

    def __str__(self) -> str:
        to_strs = lambda n: str(n)
        return "\n".join(list(map(to_strs, reversed(self.data))))

    def push(self, val: int) -> None:
        """
        Pushes val to the top of stack.

        Time: Amortized O(1)
        Space: O(1)
        """
        self.data.append(val)

    def pop(self) -> Optional[int]:
        """
        Pops the top element from the stack.
        Returns None if the stack is empty.

        Time: O(1)
        Space: O(1)
        """
        if len(self) > 0:
            return self.data.pop()
        return None

    def peek(self) -> Optional[int]:
        """
        Return thes top element of the stack without popping it.
        Returns None if the stack is empty.

        Time: O(1)
        Space: O(1)
        """
        if len(self) > 0:
            return self.data[-1]
        return None
