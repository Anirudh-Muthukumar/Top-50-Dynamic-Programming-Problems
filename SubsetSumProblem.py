'''
Subset Sum problem is to find a subset from the given array such that it sums upto
given target. 

(Special case of knapsack problem) - find collection of item with given sum 

Time complexity: O(nW)
Space complexity: O(nW)
'''

def subsetSum(A, n, sum, lookup):
    # subset found
    if sum==0:
        return True 
    
    # if no elements left or sum becomes negative
    if n<0 or sum<0:
        return False  
    
    # dynamic input of the subproblem
    key = str(n) + '|' + str(sum)

    if key not in lookup:
        # include current item
        include = subsetSum(A, n-1, sum - A[n], lookup)

        # exclude current item
        exclude = subsetSum(A, n-1, sum, lookup)

        lookup[key] = include or exclude
    
    return lookup[key]

if __name__ == '__main__':
    nums = [7,3,2,5,8]
    target = 18
    n = len(nums)
    print("\nSubset Sum : %s\n" % subsetSum(nums, n-1, target, {}))