from __future__ import print_function

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def partition(array, start, end):
    pivot = array[end]
    L = start
    R = end
    while L < R:
        while array[L] < pivot:
            L += 1
        while array[R] > pivot:
            R -= 1
        swap(array, L, R)
        
        if (array[L] == array[R]):
            L += 1
    return R

def _quick_sort(array, start, end):
    if start < end:
        split = partition(array, start, end)
        _quick_sort(array, start, split - 1)
        _quick_sort(array, split + 1, end)
    return array

def quick_sort(array):
    return _quick_sort(array, 0, len(array) - 1)


if __name__ == "__main__":
    import sys    
    print("Quick Sort\n============================================\n")
    
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by a comma:\n')
    unsorted = [int(item) for item in user_input.split(',')]    
    print(quick_sort(unsorted))