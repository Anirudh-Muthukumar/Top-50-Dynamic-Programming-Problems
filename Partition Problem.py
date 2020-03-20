'''
Parition problem is to determine whether the given array can be paritioned
into two subsets with equal sum

(Special case of knapsack problem) - find a collection of items with given value

Time complexity : O(nW)
Space complexity: O(nW)
'''

def subsetSum(A, n, sum, lookup):
    
    # subset found
    if sum==0: 
        return True
    
    # no items left or sum is negative
    if n<0 or sum<0:
        return False
    
    # dynamic input for the subproblem
    key = str(n) + '|' + str(sum)
    
    if key not in lookup:
        # include current element
        include = subsetSum(A, n-1, sum-A[n], lookup)

        # exclude current element
        exclude = subsetSum(A, n-1, sum, lookup)

        lookup[key] = include or exclude 
    
    return lookup[key]

def partitionProblem(arr):
    Sum = sum(arr)
    n = len(arr)
    return Sum%2==0 and subsetSum(arr, n-1, Sum//2, {})

if __name__ == '__main__':

    arr = [3,1,1,2,2,1]
    print("\nCan Partition Array ? - %s\n" % partitionProblem(arr))