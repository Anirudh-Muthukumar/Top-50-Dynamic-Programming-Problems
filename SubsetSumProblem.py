# Check if there is any non-empty subset with given sum 
# Special case of knapsack problem

def subsetSum(arr, sum):
    n = len(arr)
    T = [[None for _ in range(sum+1)] for _ in range(n+1)]
    
    # if sum is zero
    for i in range(n+1):
        T[i][0] = True

    # if sum is non-zero
    for j in range(1, sum+1):
        T[0][j] = False

    for i in range(1, n+1):
        for j in range(1, sum+1):
            # if sum is negative, dont include ith element
            if arr[i-1] > j:
                T[i][j] = T[i-1][j]
            else: # include or exclude ith element
                T[i][j] = T[i-1][j] or T[i-1][j-arr[i-1]]
    
    return T[n][sum]

nums = [7,3,2,5,8]
target = 18

print("Subset Sum : ", subsetSum(nums, target))