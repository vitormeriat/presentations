from __future__ import print_function

def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)

def heap_sort(array):
    """
    Simple implementation of the heap sort algorithm in Python
    :param array: some mutable ordered array with heterogeneous comparable items inside
    :return: the same array ordered by ascending

    Examples:
    >>> heap_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> heap_sort([])
    []

    >>> heap_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, i, n)
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, 0, i)
    return array

if __name__ == '__main__':
    import sys
    print("Heap Sort\n============================================\n")

    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by a comma:\n')
    unsorted = [int(item) for item in user_input.split(',')]
    print(heap_sort(unsorted))
