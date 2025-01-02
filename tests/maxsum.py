#!/bin/python3

import math
import os
import random
import re
import sys

# TO create the DP I will use the SRTBOT Approach
# Subproblem:  MaxSum(i) = maximum sum of non-adjacent elements in A[i:] - O(n)
# Relation: MaxSum(i) = max{ A[i] + MaxSum(i+2) if i+2 < len(A) else 0, # chosen i
#                           MaxSum(i+1) if i + 1 < len(A), # did not choose i
#                           0} # if all are negative
# topology order i: len(a) -> 0
# base case: MaxSum(len(a)) = 0
# original Problem: MaxSum(0)
# Time complexity: O(n)

# Complete the maxSubsetSum function below.
def recursiveMaxSubsetSum(arr):
    # 
    memo = {}
    def maxSum(i):
        if i in memo:
            return memo[i]
        
        if i >= len(arr):
            memo[i] = 0
        else:
            max_if_use_i = arr[i] + (maxSum(i+2) if (i + 2) < len(arr) else 0)
            max_if_not_use_i = maxSum(i+1)
            memo[i] = max(max_if_use_i, max_if_not_use_i, 0)
        
        return memo[i]

    return maxSum(0)


def maxSubsetSum(arr):
    memo = {}
    for i in range(len(arr)+1, -1, -1):
        if i in memo:
            return memo[i]
        
        if i >= len(arr):
            memo[i] = 0
        else:
            max_if_use_i = arr[i] + (memo[i+2] if (i + 2) < len(arr) else 0)
            max_if_not_use_i = memo[i+1]
            memo[i] = max(max_if_use_i, max_if_not_use_i, 0)

    return memo[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

