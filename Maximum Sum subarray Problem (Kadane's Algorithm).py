'''
Given an array, find the subarray with maximum sum using Kadane's Algorithm

Time complexity : O(n)
Space complexity: O(1)

''' 

def maximumSumSubarray(A):

    max_so_far = A[0]
    max_ending_here = A[0]

    for i in range(1, len(A)):
        max_ending_here = max_ending_here + A[i]

        max_ending_here = max(max_ending_here, 0)

        max_so_far = max(max_ending_here, max_so_far)

    return max_so_far

if __name__ == '__main__':

    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    n = len(A)
    
    print("\nMaximum sum subarray = %d\n" %maximumSumSubarray(A))