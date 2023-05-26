import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_linked_list_creation(self):
        l = LinkedList()

        self.assertIsNone(l.head)
        self.assertIsNone(l.tail)
        self.assertEqual(0, len(l), "Expected length to be 0")

    def test_linked_list_append(self):
        l = LinkedList()
        l.append(42)

        self.assertIsNotNone(l.head, "Expected head to exist")
        self.assertIsNotNone(l.tail, "Expected tail to exist")
        self.assertEqual(l.head, l.tail, "Expected head and tail to be the same")
        self.assertEqual(1, len(l), "Expected length to be 1")

        l.append(69)
        self.assertEqual(l.head.val, 42)
        self.assertEqual(l.tail.val, 69)
        self.assertEqual(2, len(l), "Expected length to be 2")

    def test_linked_list_prepend(self):
        l = LinkedList()
        l.prepend(42)

        self.assertIsNotNone(l.head, "Expected head to exist")
        self.assertIsNotNone(l.tail, "Expected tail to exist")
        self.assertEqual(l.head, l.tail, "Expected head and tail to be the same")
        self.assertEqual(1, len(l), "Expected length to be 1")

        l.prepend(69)
        self.assertEqual(69, l.head.val, "Expected head to be 69")
        self.assertEqual(42, l.tail.val, "Expected tail to be 42")
        self.assertEqual(2, len(l), "Expected length to be 2")

    def test_linked_list_get_at(self):
        l = LinkedList()
        l.append(42)
        l.append(69)
        l.append(420)

        self.assertEqual(3, len(l), "Expected length to be 3")

        self.assertEqual(42, l.get_at(0), "Expected element 0 to be 42")
        self.assertEqual(69, l.get_at(1), "Expected element 1 to be 69")
        self.assertEqual(420, l.get_at(2), "Expected element 2 to be 420")

        self.assertIsNone(l.get_at(-1), "Expected too small index to result in None")
        self.assertIsNone(l.get_at(999), "Expected too large index to result in None")

    def test_linked_list_remove_at(self):
        l = LinkedList()
        l.append(42)
        l.append(69)
        l.append(420)

        self.assertEqual(3, len(l), "Expected length to be 3")

        self.assertEqual(42, l.remove_at(0), "Expected removed element to be 42")
        self.assertEqual(69, l.remove_at(0), "Expected removed element to be 69")
        self.assertEqual(420, l.remove_at(0), "Expected removed element to be 420")
        self.assertEqual(0, len(l), "Expected length to be 0")

        self.assertIsNone(l.remove_at(-1), "Expected too small index to result in None")
        self.assertIsNone(
            l.remove_at(999), "Expected too large index to result in None"
        )


if __name__ == "__main__":
    unittest.main()
