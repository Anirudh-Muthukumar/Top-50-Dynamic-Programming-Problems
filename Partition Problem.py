# Partition the given array into two subarrays with equal sum
# Precondition : 
# (1) Sum of array elements should be even
# (2) Array can be divided into two subsets with equal sum

def subsetSum(arr, sum):
    n = len(arr)
    T = [[None for _ in range(sum+1)] for _ in range(n+1)]

    # if sum is not zero
    for j in range(1, sum+1):
        T[0][j] = False
    
    # if sum is zero
    for i in range(n+1):
        T[i][0] = True
    
    # for rest of the elements
    for i in range(1, n+1): # arr[i-1] indicates current array element
        for j in range(1, sum+1): # j indicates current sum 
            # sum goes to negative, don't include ith element
            if j - arr[i-1] < 0: 
                T[i][j] = T[i-1][j]
            else: # include and exclude ith element
                T[i][j] = T[i-1][j] or T[i-1][j-arr[i-1]]
    
    return T[n][sum]

def partition(arr):
    sum = 0
    for num in arr:
        sum += num
    
    return not sum&1 and subsetSum(arr, sum//2)
    


if __name__ == '__main__':

    arr = [3,1,1,2,2,1]
    print("Partition Array : ", partition(arr))