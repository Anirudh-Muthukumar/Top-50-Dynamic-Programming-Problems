'''
Longest Alternating subsequence problem is to find a longest subsequence of a given sequence
such that elements are in alternating order.

Time complexity : O(n^2)
Space complexity: O(n)

'''

lookup = {}

def LAS(A, start, end, flag):
    
    key = str(start) + '|' + str(flag)

    if key not in lookup:
        res = 0
        for i in range(start, end+1):
            
            # flag is set - A[i-1] < A[i]
            if flag and A[i-1]<A[i]:
                res = max(res, 1 + LAS(A, i+1, end, not flag))
            
            # flag is not set - A[i-1] > A[i]
            elif not flag and A[i-1]>A[i]:
                res = max(res, 1 + LAS(A, i+1, end, not flag))

            # exclude current element and don't toggle the flag
            else:
                res = max(res, LAS(A, i+1, end, flag)) 
        
        lookup[key] = res
    
    return lookup[key]


def longestAlternatingSequence(A):
    n = len(A)
    return 1 + max(LAS(A, 1, n-1, True), LAS(A, 1, n-1, False))

if __name__ == '__main__':
    arr = [8, 9, 6, 4, 5, 7, 3, 2, 4]

    print("\nLAS = %d\n" % longestAlternatingSequence(arr))