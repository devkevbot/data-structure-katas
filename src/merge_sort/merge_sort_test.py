from merge_sort import merge_sort
import unittest


class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        arr = [13, -47, 1002, 69, 4, -1000]
        merge_sort(arr, 0, len(arr))
        self.assertListEqual(arr, [-1000, -47, 4, 13, 69, 1002])

        arr = [5, 4, 3, 2, 1]
        merge_sort(arr, 0, len(arr))
        self.assertListEqual(arr, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
