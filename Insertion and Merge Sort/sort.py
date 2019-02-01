from math import floor, inf
a = [7, 2, 5, 5, 9.6]


"""
Insertion Sort
@params  array - One dimension array
@returns the array sorted
@complexity O(n^2) with O(n^2) swaps and comparisons
            OBS: It could be done with binary search to find the right place,
            changing the complexity of comparisons to O(n log n)
"""
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j-1] > array[j]:
                aux = array[j-1]
                array[j-1] = array[j]
                array[j] = aux

    return array


"""
Merge Step
@params  left - One dimension array
         right - One dimension array
@returns the array merged in order
        OBS: It's used on Merge Sort steps
"""
def merge(left, right):
    output = []
    left_cursor = 0
    right_cursor = 0
    while left_cursor < len(left) or right_cursor < len(right):
        left_value = inf
        if left_cursor < len(left): 
            left_value = left[left_cursor]

        right_value = inf
        if right_cursor < len(right): 
            right_value = right[right_cursor]
        
        if left_value < right_value:
            output.append(left_value)
            left_cursor+=1
        else:
            output.append(right_value)
            right_cursor+=1
    return output

"""
Merge Sort
@params  array - One dimension array
@returns the array sorted
@complexity O(n log n) 
"""
def merge_sort(array):
    if len(array) > 2:
        mid = floor(len(array)/2)
        return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))
    elif len(array) == 2:
        return merge([array[0]], [array[1]])
    else:
        return array

print(merge_sort(a))
