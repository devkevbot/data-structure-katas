def binary_search_boolean(arr: list[int], target: int) -> bool:
    """
    Returns whether or not the array contains target.

    Let n be the length of the input array.
    Time: O(logn)
    Space: O(1)
    """
    if len(arr) == 0:
        return False

    L = 0
    R = len(arr) - 1

    while L <= R:
        # In other languages, this addition may integer overflow
        M = (L + R) // 2

        if arr[M] == target:
            return True

        if target < arr[M]:
            R = M - 1
        elif target > arr[M]:
            L = M + 1

    return False


def binary_search_index(arr: list[int], target: int) -> int:
    """
    Returns the index of the target value in the array if it exists and -1 otherwise.

    Let n be the length of the input array.
    Time: O(logn)
    Space: O(1)
    """
    if len(arr) == 0:
        return -1

    L = 0
    R = len(arr) - 1

    while L <= R:
        # In other languages, this addition may integer overflow
        M = (L + R) // 2

        if arr[M] == target:
            return M

        if target < arr[M]:
            R = M - 1
        elif target > arr[M]:
            L = M + 1

    return -1
