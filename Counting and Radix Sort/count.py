"""
Is possible, for small integers, to do O(n) sort with counting or radix sort
If you have an array with length n containing k keys, if k = n^O(1), we can sort at O(n).
"""


def key(elem):
    return elem

"""
Counting Sort
@params  array - One dimension array with integers.
@returns the array sorted
@complexity O(k+n) => O(n) if k = n^O(1)
            It puts the array elements aggruped in a 'frequency' list.
            Therefore, we just need to put the elements in normal order
            on output, using one simple for.
"""
def counting_sort(array):
    k = 10 #number of keys
    freq = []
    for x in range(k): #O(K)
        freq.append([])

    for elem in array: #O(N)
        freq[key(elem)].append(elem)
    
    output = []
    for values in freq:  # O(K+N)
        output.extend(values)
    
    return output


"""
Radix Sort
Sort big integers in base b using counting sort
@complexity O(n logn k) => O(nc) if k <= n^c
            It orders from the least significant digit to the most using
            counting sort. 
"""