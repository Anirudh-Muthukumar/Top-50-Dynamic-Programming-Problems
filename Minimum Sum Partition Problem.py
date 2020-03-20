'''
Minimum Sum Partition problem is to partition the given array into two subsets 
such that absolute difference between sum of the two subsets is minimum. 

(Special case of partition problem)

Time complexity : O(nW)
Space complexity: O(nW)

'''

def minimumSumPartition(A, n, sum1, sum2, lookup):

    # no more elements left
    if n==0:
        return abs(sum1 - sum2)
    
    # dynamic input of the subproblem 
    key = str(n) + '|' + str(sum1) + '|' + str(sum2) 

    if key not in lookup:

        # include current item to set 1
        set1 = minimumSumPartition(A, n-1, sum1 + A[n], sum2, lookup)

        # include current item to set 2
        set2 = minimumSumPartition(A, n-1, sum1, sum2 + A[n], lookup)
        
        # choose the one which minimizes sum
        lookup[key] = min(set1, set2)
    
    return lookup[key]

if __name__ == '__main__':
    arr = [10, 20, 15, 5, 25]
    n = len(arr)
    print("\nMinimum difference = %d\n" % minimumSumPartition(arr, n-1, 0, 0, {}))