from __future__ import print_function

def _mergesort(unsorted, start, end):
    mid = (start + end)/2
    if start < end:
        _mergesort(unsorted, start, mid)
        _mergesort(unsorted, mid+1, end)
    elif start == end: return

    L = start; R = mid+1
    tmp_array = []
    while ( L <= mid and R <= end):
        if (unsorted[L] < unsorted[R]):
            tmp_array.append(unsorted[L])
            L += 1
        else:
            tmp_array.append(unsorted[R])
            R += 1

    if L <= mid:
        tmp_array += unsorted[L:]
    else:
        tmp_array += unsorted[R:]

    i = 0;
    while (start <= end):
        unsorted[start] = tmp_array[i]
        start += 1; i += 1;
    return unsorted

def merge_sort(array):
    """
    Simple implementation of the merge sort algorithm in Python

    :param array: some mutable ordered array with heterogeneous comparable items inside
    :return: the same array ordered by ascending

    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> merge_sort([])
    []

    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    return _mergesort(array, 0, len(array)-1)

if __name__ == "__main__":
    import sys    
    print("Merge Sort\n============================================\n")
    
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by a comma:\n')
    unsorted = [int(item) for item in user_input.split(',')]
    print(merge_sort(unsorted))
