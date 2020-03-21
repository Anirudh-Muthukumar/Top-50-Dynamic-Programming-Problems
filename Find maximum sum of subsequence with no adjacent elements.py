'''
Given an array of integers determine the subsequence with maximum sum that has no adjacent
elements from the array.     

Time complexity : O(n)
Space complexity: O(n)

'''

def findMaximumSum(A, n, lookup):

    if n<0:
        return 0 
    
    key = str(n) 

    if key not in lookup:

        # include current element, recur from n-2 
        include = A[n] + findMaximumSum(A, n-2, lookup)

        # exclude current element, recur from n-1
        exclude = findMaximumSum(A, n-1, lookup)

        lookup[key] = max(include, exclude)
    
    return lookup[key]



if __name__ == '__main__':
    A = [1, 2, 9, 4, 5, 0, 4, 11, 6]
    n = len(A) 
    print("\nMaximum sum subsequence without adjacent elements = %d\n" % findMaximumSum(A, n-1, {}))