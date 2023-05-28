from queue import Queue
import unittest


class TestQueue(unittest.TestCase):
    def test_queue_creation(self):
        q = Queue()
        self.assertEqual(len(q), 0)

    def test_queue_insertion(self):
        q = Queue()

        q.enqueue(42)
        self.assertEqual(len(q), 1)
        self.assertEqual(q.data[0], 42)

        q.enqueue(69)
        self.assertEqual(len(q), 2)
        self.assertEqual(q.data[1], 69)

    def test_queue_removal(self):
        q = Queue()
        q.enqueue(42)
        front = q.dequeue()

        self.assertEqual(len(q), 0)
        self.assertEqual(front, 42)

        front = q.dequeue()
        self.assertIsNone(front)

    def test_queue_peek_front(self):
        q = Queue()
        front = q.peek_front()

        self.assertEqual(len(q), 0)
        self.assertIsNone(front)

        q.enqueue(42)
        front = q.peek_front()
        self.assertEqual(len(q), 1)
        self.assertEqual(front, 42)

        q.enqueue(69)
        front = q.peek_front()
        self.assertEqual(len(q), 2)
        self.assertEqual(front, 42)


if __name__ == "__main__":
    unittest.main()
