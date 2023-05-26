from quick_sort import quick_sort
import unittest


class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        arr = [13, -47, 1002, 69, 4, -1000]
        quick_sort(arr, 0, len(arr) - 1)
        self.assertListEqual(arr, [-1000, -47, 4, 13, 69, 1002])

        arr = [5, 4, 3, 2, 1]
        quick_sort(arr, 0, len(arr) - 1)
        self.assertListEqual(arr, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
