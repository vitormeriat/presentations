from __future__ import print_function

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def insertion_sort(unsorted):    
    for i in range(0, len(unsorted)):
        j = i
        while j > 0 and unsorted[j-1] > unsorted[j]:
            swap(unsorted, j-1, j)
            j -= 1
    return unsorted

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