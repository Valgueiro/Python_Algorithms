
"""
SRTBOT approach for recursive algorithm design & (with memoization)
    - Subproblem: definition
        - for Sequence S, try perfixes (S[:i] o(n)), suffixes (S[i:] o(n)), substrings (S[i:j] o(n^2))
        - for nonnegative integer K, try integers in [0,K]
        - add subprobs & constraints to "remmember state"

    - Relate: subproblem solutions recursively
        - identify question about subproblem solution that, if you knew answer, reduces to "smaller" subproblems
        - locally brute-force all answers to question
        - can think of correctly guessing answer
    
    - Topological order: on subprobs (DAG) A -> b = b needs A

    - Base case of relation

    - Original problem: solve via subproblem(s)

    - Time Analysis <= num of subproblems * time per subproblem + work to solve original
"""

# Fibonnaci
# SRTBOT
# Subproblem: F(n) = Fi , 1<=n<=n
# Relate: F(n) = f(n-1) + f(n-2)
# Topo: 1 -> n
# base: F(0) = 0; f(1) =  1
# Original: F(n)
# Time: O(n) with memoization

@cache
def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    
    return self.fib(n-1) + self.fib(n-2)

# LCS
# Subproblem: lcs(i, j) = size of longest prefix between t1[i:] and t2[j:]
# Relation: lcs(i,j) = if t1[i] == t2[j]: return 1 + lcs(i + 1, j+1) 
# else: max(lcs(i+1, j), lcs(i, j+1))
# Topological order: i: 0 -> |t1| j: 0 -> |t2|
# Base case: i == |t1| - 1 or j == |t2| - 2 return 0.
# Original prob: lcs(0, 0)
# Time: O(|t1| * |t2|)

def longestCommonSubsequence(text1: str, text2: str) -> int:
    res = []
    @cache
    def lcs(i, j):
        if i == len(text1) or j == len(text2):
            return 0

        if text1[i] == text2[j]:
            res.append(text1[i])
            return 1 + lcs(i+1, j+1)

        return max(lcs(i+1, j), lcs(i, j+1))
    out =  lcs(0, 0)
    print(res)

    return out


# LIS

# Subprob: lis() = size of lis on A[i:] when A[i] was chosen
# Relation: 1 + max{A[j] for j in range(i, len(A) if A[j] > A[i])}
# Topo: i: 0-> j
# Base: lis(len(s)) = 0
# Original prob: max{lis(j) for j in range(len(s))}
# Time: O(n) * O(n) * O(1) -> O(n^2)

def lengthOfLIS(nums: List[int]) -> int:
    @cache
    def lis(i):
        if i == len(nums):
            return 0
        return 1 + max([lis(j) for j in range(i, len(nums)) if nums[j]> nums[i]] + [0])

    return max(lis(j) for j in range(len(nums))) 


# Max subset of non-adjacent members. Sometimes recursive doesnt fit.
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
