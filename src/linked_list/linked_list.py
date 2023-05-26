from typing import Optional


class Node:
    def __init__(self, val, prev=None, next=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class LinkedList:
    """
    A Linked List is a data structure consisting of nodes which are
    linked together. Each node contains a value.
    """

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.len = 0

    def __len__(self) -> int:
        return self.len

    def __str__(self) -> str:
        curr = self.head
        out = []
        while curr:
            out.append(str(curr.val))
            curr = curr.next
        return "<->".join(out)

    def append(self, val: int) -> None:
        """
        Adds the val to the end of the list.

        Time: O(1)
        Space: O(1)
        """
        n = Node(val)

        if len(self) == 0:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n

        self.len += 1

    def prepend(self, val: int) -> None:
        """
        Adds the value to the start of the list.

        Time: O(1)
        Space: O(1)
        """
        n = Node(val)

        if len(self) == 0:
            self.head = n
            self.tail = n
        else:
            self.head.prev = n
            n.next = self.head
            self.head = n

        self.len += 1

    def get_at(self, pos: int) -> Optional[int]:
        """
        Return the value of the node at position `pos` in the list

        Time: O(n)
        Space: O(1)
        """
        if pos < 0 or pos > len(self):
            return None

        curr = self.head
        while pos > 0:
            curr = curr.next
            pos -= 1

        return curr.val

    def remove_at(self, pos: int) -> None:
        """
        Removes the node at position `pos` in the list

        Time: O(n)
        Space: O(1)
        """
        if pos < 0 or pos > len(self):
            return None

        curr = self.head
        while pos > 0:
            curr = curr.next
            pos -= 1

        if curr is self.head:
            if len(self) == 1:
                self.head = None
                self.tail = None
            else:
                self.head.next.prev = None
                self.head = self.head.next
            self.len -= 1
        elif curr is self.tail:
            if len(self) == 1:
                self.head = None
                self.tail = None
            else:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            self.len -= 1

        return curr.val

    def head_val(self) -> Optional[int]:
        """
        Returns the value of the head of the list

        Time: O(1)
        Space: O(1)
        """
        if self.head:
            return self.head.val
        return None

    def tail_val(self) -> Optional[int]:
        """
        Returns the value of the tail of the list

        Time: O(1)
        Space: O(1)
        """
        if self.tail:
            return self.tail.val
        return None
