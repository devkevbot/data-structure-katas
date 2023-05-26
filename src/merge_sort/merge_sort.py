def merge_sort(arr: list[int], start: int, end: int):
    """
    Performs a recursive in-place merge sort (ascending order) on the input array

    Let n be the number of elements in the input array.
    Time: O(nlogn)
    Space: O(n)
    """

    if end - start <= 0:
        return

    mid = (start + end) // 2

    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)

    merge_subarrays(arr, start, mid, end)


def merge_subarrays(arr: list[int], start: int, mid: int, end: int):
    left_pos = 0
    right_pos = 0
    write_pos = start

    left_arr = arr[start : mid + 1]
    right_arr = arr[mid + 1 : end + 1]

    while left_pos < len(left_arr) and right_pos < len(right_arr):
        if left_arr[left_pos] <= right_arr[right_pos]:
            arr[write_pos] = left_arr[left_pos]
            left_pos += 1
        else:
            arr[write_pos] = right_arr[right_pos]
            right_pos += 1
        write_pos += 1

    while left_pos < len(left_arr):
        arr[write_pos] = left_arr[left_pos]
        left_pos += 1
        write_pos += 1

    while right_pos < len(right_arr):
        arr[write_pos] = right_arr[right_pos]
        right_pos += 1
        write_pos += 1
