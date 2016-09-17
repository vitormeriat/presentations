from __future__ import print_function

def _mergesort(array, start, end):
    mid = (start + end)/2
    if start < end:
        _mergesort(array, start, mid)
        _mergesort(array, mid+1, end)
    elif start == end: return

    L = start; R = mid+1
    tmp_array = []
    while ( L <= mid and R <= end):
        if (array[L] < array[R]):
            tmp_array.append(array[L])
            L += 1
        else:
            tmp_array.append(array[R])
            R += 1

    if L <= mid:
        tmp_array += array[L:]
    else:
        tmp_array += array[R:]

    i = 0;
    while (start <= end):
        array[start] = tmp_array[i]
        start += 1; i += 1;

def mergesort(array):
    _mergesort(array, 0, len(array)-1)

if __name__ == "__main__":
    import sys    
    print("Merge Sort\n============================================\n")
    
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by a comma:\n')
    unsorted = [int(item) for item in user_input.split(',')]
    mergesort(unsorted)
    print(unsorted)
