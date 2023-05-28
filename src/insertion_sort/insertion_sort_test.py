from insertion_sort import insertion_sort
import unittest


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        arr = [13, -47, 1002, 69, 4, -1000]
        insertion_sort(arr)
        self.assertListEqual(arr, [-1000, -47, 4, 13, 69, 1002])

        arr = [5, 4, 3, 2, 1]
        insertion_sort(arr)
        self.assertListEqual(arr, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
