from binary_search import binary_search_boolean, binary_search_index
import unittest


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_boolean(self):
        arr = [1, 2, 3, 4, 5, 6]
        self.assertTrue(binary_search_boolean(arr, 1))
        self.assertTrue(binary_search_boolean(arr, 2))
        self.assertTrue(binary_search_boolean(arr, 3))
        self.assertTrue(binary_search_boolean(arr, 4))
        self.assertTrue(binary_search_boolean(arr, 5))
        self.assertTrue(binary_search_boolean(arr, 6))
        self.assertFalse(binary_search_boolean(arr, -10000))

    def test_binary_search_index(self):
        arr = [1, 2, 3, 4, 5, 6]
        self.assertEqual(binary_search_index(arr, 1), 0)
        self.assertEqual(binary_search_index(arr, 2), 1)
        self.assertEqual(binary_search_index(arr, 3), 2)
        self.assertEqual(binary_search_index(arr, 4), 3)
        self.assertEqual(binary_search_index(arr, 5), 4)
        self.assertEqual(binary_search_index(arr, 6), 5)
        self.assertEqual(binary_search_index(arr, -10000), -1)


if __name__ == "__main__":
    unittest.main()
