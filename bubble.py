from __future__ import print_function

def bubble_sort(array):
    """
    Simple implementation of bubble sort algorithm in Python

    :param array: some mutable ordered array with heterogeneous comparable items inside
    :return: the same array ordered by ascending

    Examples:
    >>> bubble_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> bubble_sort([])
    []

    >>> bubble_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    length = len(array)
    for i in range(length-1, -1, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

if __name__ == '__main__':
    import sys
    print("Bubble Sort\n============================================\n")
    
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by a comma:\n')
    unsorted = [int(item) for item in user_input.split(',')]
    print(bubble_sort(unsorted))
