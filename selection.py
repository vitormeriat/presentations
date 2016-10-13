from __future__ import print_function

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def selection_sort(array):
    """
    Simple implementation of the selection sort algorithm in Python
    :param array: Some mutable ordered array with heterogeneous comparable items inside
    :return: The same array ordered by ascending    

    Examples:
    >>> selection_sort([0, 5, 3, 2, 2, -8])
    [-8, 0, 2, 2, 3, 5]

    >>> selection_sort([])
    []

    >>> selection_sort([-2, -5, -45, 99])
    [-45, -5, -2, 99]
    """

    for i in range(0, len(array)):
        Ismallest = i
        for j in range(i + 1, len(array)):
            if array[j] < array[Ismallest]:
                Ismallest = j
        swap(array, i, Ismallest)
    return array


if __name__ == "__main__":    
    import sys    
    import time
    import cProfile
    print("Quick Sort\n============================================\n")
    
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by a comma:\n')    
    unsorted = [int(item) for item in user_input.split(',')]    
    print(selection_sort(unsorted))
    