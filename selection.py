from __future__ import print_function

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def selectionsort(array):
    for i in range(0, len(array)):
        Ismallest = i
        for j in range(i + 1, len(array)):
            if array[j] < array[Ismallest]:
                Ismallest = j
        swap(array, i, Ismallest)


if __name__ == "__main__":    
    import sys    
    print("Quick Sort\n============================================\n")
    
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by a comma:\n')
    unsorted = [int(item) for item in user_input.split(',')]
    selectionsort(unsorted)
    print(unsorted)