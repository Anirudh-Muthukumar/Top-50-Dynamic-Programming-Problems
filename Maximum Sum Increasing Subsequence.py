'''
Maximum Sum Increasing Subsequence (MSIS) problem is to find an increasing subsequence 
with maximum sum. 

Time complexity: O(n^2)
Space complexity: O(n) - to find MSIS 
Space complexity: O(n^2) - to print MSIS 

'''

def MSIS(A):
    n = len(A)
    # array to store MSIS of subsequence ending at index i
    sum = [0] * n 

    sum[0] = A[0] 

    for i in range(1, n):
        for j in range(n):
            if A[j] < A[i] and sum[j] > sum[i]:
                sum[i] = sum[j]
        sum[i] += A[i] 
    
    return max(sum) 

def printMSIS(A):
    n = len(A)
    Sum = [0] * n 
    MSIS = [[] for _ in range(n)]

    Sum[0] = A[0]
    MSIS[0].append(A[0])

    for i in range(1, n):
        for j in range(n):
            if A[j]<A[i] and Sum[j]>Sum[i]:
                MSIS[i] = MSIS[j][:]
                Sum[i] = Sum[j] 
        Sum[i] += A[i]
        MSIS[i].append(A[i])
    
    print("MSIS = ", end = ' ')
    for msis in MSIS:
        if sum(msis)==max(Sum):
            print(msis)

if __name__ == '__main__':
    arr = [8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11]
    
    print("MSIS of %s = %d"  %(arr, MSIS(arr)))

    printMSIS(arr)