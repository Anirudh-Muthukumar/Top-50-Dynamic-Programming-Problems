'''
Longest bitonic subsequence (LBS) problem is to find a subsequence of given sequence 
such that elements of the subsequence are first sorted in increasing order and
then sorted in decreasing order. 

# Time complexity: O(n^2)
# Space complexity: O(n) - to find LBS
# Space complexity: O(n^2) - to find all LBS

'''

def LBS(A): 
    # Maintain to arrays to store LIS and LDS 
    # LIS - Longest Increasing subsequence ending at index i 
    # LDS - Longest Decreasing subsequence starting at index i

    n = len(A)
    LIS = [0] * n 
    LDS = [0] * n

    LIS[0] = 1 

    for i in range(1, n):
        for j in range(n):
            if A[j]<A[i] and LIS[j] > LIS[i]:
                LIS[i] = LIS[j]

        # every element is a subsequence on its own
        LIS[i] += 1 
    
    LDS[0] = 1 
    # reverse the array and find LIS to get LDS
    B = A[::-1]

    for i in range(1, n):
        for j in range(n):
            if B[j]<B[i] and LDS[j] > LDS[i]:
                LDS[i] = LDS[j]

        # every element is a subsequence on its own
        LDS[i] += 1 

    # reverse the result back to get LDS
    LDS = LDS[::-1]

    maxlen = 0
    for i in range(n):
        maxlen = max(maxlen, LIS[i]+LDS[i]-1)
    
    return maxlen

def printLBS(A):
    n = len(A)
    LIS = [[] for _ in range(n)]
    LDS = [[] for _ in range(n)]
    
    LIS[0].append(A[0])
    
    for i in range(1, n):
        for j in range(n):
            if A[j] < A[i] and len(LIS[j]) > len(LIS[i]):
                LIS[i] = LIS[j][:]

        LIS[i].append(A[i])
    
    B = A[::-1]
    LDS[0].append(B[0])
    
    for i in range(1, n):
        for j in range(n):
            if B[j] < B[i] and len(LDS[j]) > len(LDS[i]):
                LDS[i] = LDS[j][:]
        
        LDS[i].append(B[i])
    
    LDS = LDS[::-1]
    LDS = [lds[::-1] for lds in LDS]


    lbs = 0
    for i in range(n):
        lbs = max(lbs, len(LIS[i]) + len(LDS[i]) - 1)
    
    print("LBS of %s: " % A, end = ' ')

    for i in range(n):
        if (len(LIS[i]) + len(LDS[i]) - 1)==lbs:
            print("%s\n" % (LIS[i] + LDS[i][1:]))
            break
    
    
if __name__ == '__main__':

    arr = [4, 2, 5, 9, 7, 6, 10, 3, 1]

    print("\nLength of LBS = ", LBS(arr))

    printLBS(arr)