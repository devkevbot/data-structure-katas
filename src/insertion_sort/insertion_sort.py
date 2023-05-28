def insertion_sort(arr: list[int]) -> None:
    """
    An in-place insertion sort

    Let n be the number of elements
    Time: O(n^2)
    Space: O(1)
    """

    for i in range(1, len(arr)):
        j = i - 1

        while j >= 0 and arr[j + 1] < arr[j]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
