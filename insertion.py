from __future__ import print_function

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def insertion_sort(array):   
    """
    Simple implementation of the insertion sort algorithm in Python

    :param array: some mutable ordered array with heterogeneous comparable items inside 
    :return: the same array ordered by ascending

    Examples:
    >>> insertion_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> insertion_sort([])
    []

    >>> insertion_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    for i in range(0, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            swap(array, j-1, j)
            j -= 1
    return array

if __name__ == "__main__":
    import sys    
    print("Insertion Sort\n============================================\n")
    
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by a comma:\n')
    unsorted = [int(item) for item in user_input.split(',')]
    print(insertion_sort(unsorted))