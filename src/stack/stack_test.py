from stack import Stack
import unittest


class TestStack(unittest.TestCase):
    def test_stack_creation(self):
        s = Stack()
        self.assertEqual(0, len(s), "Expected length to be 0")

    def test_stack_push(self):
        s = Stack()
        s.push(42)
        s.push(69)

        self.assertEqual(2, len(s), "Expected length to be 2")
        self.assertEqual(69, s.peek(), "Expected peeked element to be 69")

    def test_stack_pop(self):
        s = Stack()
        s.push(42)
        s.push(69)

        self.assertEqual(69, s.pop(), "Expected popped element to be 69")
        self.assertEqual(1, len(s), "Expected length to be 1")

        self.assertEqual(42, s.pop(), "Expected popped element to be 42")
        self.assertEqual(0, len(s), "Expected length to be 0")

        self.assertIsNone(s.pop(), "Expected popped element to be None")


if __name__ == "__main__":
    unittest.main()
