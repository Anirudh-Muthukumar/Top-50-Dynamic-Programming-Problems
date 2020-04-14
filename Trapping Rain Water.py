'''
Given n non-negative integers representing an elevation map where the width of 
each bar is 1, compute how much water it is able to trap after raining.  

Time complexity : O(n)
Space complexity: O(1)
'''

def trap(A):
    n = len(A)
    if n==0:
        return 0
    
    left_max = [None] * n
    right_max = [None] * n
    left_max[0] = A[0]
    right_max[-1] = A[-1]
    
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], A[i])
    
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], A[i])

    water = 0
    
    for i in range(n):
        water += min(left_max[i], right_max[i]) - A[i]
    
    return water


A = [0,1,0,2,1,0,1,3,2,1,2,1]
print("Water trapped = ", trap(A))