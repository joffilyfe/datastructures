"""Bubble is an algorithm used to sort values in one list container.

The algorithm works swaping a set of two values if the criterion match,
for example:
    Given this array [3, 2, 5, 9, 6] we need it sorted from the lower
    to greater.

    In the first interation we found 3 lower than 2 then we swap them.
    Next we look of 5 is lower than 9 and it is true so we does not swap them.
    Next  look if 9 is lower than 6 and its false then we swap them. We got
    [2, 3, 5, 6, 9] in the first interaction.

Its complexity is O(n^2) in the worst case.
"""

def bubble_sort(array):
    """Bubble sort algorithm"""
    max = len(array)

    while True:
        has_changes = False
        max = max - 1

        for index in range(0, max):
            if array[index] > array[index + 1]:
                aux = array[index]
                array[index] = array[index + 1]
                array[index + 1] = aux
                # array[index], array[index + 1] = array[index + 1], array[index] # this is a python way
                has_changes = True

        if not has_changes:
            return array


if __name__ == "__main__":
    import random

    array = list(reversed(range(1, 100)))
    array.append(0)

    print(bubble_sort(array))