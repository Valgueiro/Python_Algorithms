from math import floor
array = [6,7,4,3,2,1,4,5]

#1D peak
def peak(arr):
    mid = floor(len(arr)/2)
    if mid > 0 and arr[mid] < arr[mid-1]:
        return peak(arr[:mid]) # peak on the left part
    elif mid+1 < len(arr) and arr[mid] < arr[mid+1]:
        return peak(arr[mid:]) # peak on the right part
    else: 
        return arr[mid] # i'm at a peak

