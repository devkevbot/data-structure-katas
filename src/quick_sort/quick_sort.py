def quick_sort(arr: list[int], start: int, end: int):
    """
    Performs a recursive in-place quick sort (ascending order) on the input array

    Let n be the number of elements in the input array.
    Time: O(n^2)
    Space: O(logn)
    """

    if end - start <= 0:
        return

    pivot = arr[end]
    swap_pos = start

    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[swap_pos] = arr[swap_pos], arr[i]
            swap_pos += 1

    arr[end], arr[swap_pos] = arr[swap_pos], arr[end]

    quick_sort(arr, start, swap_pos - 1)
    quick_sort(arr, swap_pos + 1, end)
