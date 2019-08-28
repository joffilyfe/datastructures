"""Binary search algorithm

This is the most classic search algorithm. It can be used to search data in a
binary search tree or in a simple array container those must be ordered.

Its complexity is O(log n).
"""

def binary_search(array, value):
    """The interactive way to implement"""

    min = 0
    max = len(array) - 1

    while min <= max:
        mid = (min + max) // 2

        if value == array[mid]:
            return mid
        elif value < array[mid]:
            max = mid - 1
        elif value > array[mid]:
            min = mid + 1
    return - 1


def binary_search_with_recursion(array, value, size):
    """One type of recursion way to implement."""

    mid = size // 2

    if size < 0:
        return -1

    if value == array[mid]:
        return mid
    elif value < array[mid]:
        return binary_search_with_recursion(array[0:mid], value, mid - 1)
    elif value > array[mid]:
        return binary_search_with_recursion(array[mid+1:], value, mid - 1)

def binary_search_without_slicing(array, value, min, max):
    """Recurssive implemention without slicing the array. This implementation
    is less expensive for memory than `binary_search_with_recursion`."""

    if min > max:
        return -1

    mid = (min + max) // 2

    if value == array[mid]:
        return mid
    elif value < array[mid]:
        return binary_search_without_slicing(array, value, min=min, max=mid-1)
    elif value > array[mid]:
        return binary_search_without_slicing(array, value, min=mid+1, max=max)


if __name__ == "__main__":
    import random

    value = 20
    array = list(range(1, 10))

    index = binary_search_with_recursion(array, value, len(array) - 1)
    print(f"Value {value} found (?) at index {index}")