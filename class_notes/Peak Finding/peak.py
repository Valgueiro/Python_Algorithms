from math import floor
array = [6,7,4,3,2,1,4,5]

"""
1D peak
@params  arr - One dimension array
@returns Number representing a peak (at position mid)
@complexity O(log n)
"""
def peak(arr):
    mid = floor(len(arr)/2)
    if mid > 0 and arr[mid] < arr[mid-1]:
        return peak(arr[:mid-1]) # peak on the left part
    elif mid+1 < len(arr) and arr[mid] < arr[mid+1]:
        return peak(arr[mid+1:]) # peak on the right part
    else: 
        return arr[mid] # i'm a peak


matrix = [[10, 8, 10, 10],
          [14, 13, 12, 11], 
          [15, 9, 11, 21], 
          [16, 17, 19, 20]]

def find_global_max_ind(arr):
    max_ind = 0
    for index, elemt in enumerate(arr):
        if arr[max_ind] < elemt:
            max_ind = index
    return max_ind
             

"""
2D peak
@params mat - Two dimension array
@returns Number representing a peak (at position (mid_col, i))
@complexity O(n*log n)
"""
def peak_matrix(mat):
    mid_col = floor(len(mat)/2)
    i = find_global_max_ind(mat[mid_col])
    if mid_col > 0 and mat[mid_col][i] < mat[mid_col-1][i]:
        return peak_matrix(mat[:mid_col-1])
    elif mid_col+1 < len(mat) and mat[mid_col][i] < mat[mid_col+1][i]:
        return peak_matrix(mat[mid_col+1:])
    else:
        return mat[mid_col][i]