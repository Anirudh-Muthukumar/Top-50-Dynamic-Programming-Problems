'''
Given an array A, maximize value of the expression A[s] - A[r] + A[q] - A[p] such that
p, q, r and s are indices of A and satisfy the constraint p<q<r<s

Time complexity : O(n)
Space complexity: O(n)
'''

def maximizeValue(A):
    # Maintain four lookup tables as follows:
    # L1 to store results of A[s]
    # L2 to store results of A[s] - A[r]
    # L3 to store results of A[s] - A[r] + A[q]
    # L4 to store results of A[s] - A[r] + A[q] - A[p]

    n = len(A)

    L1 = [-float('inf')] * (n+1)
    L2 = [-float('inf')] * (n)
    L3 = [-float('inf')] * (n-1)
    L4 = [-float('inf')] * (n-2)

    # Maximum value of A[s]
    for i in range(n-1, -1, -1):
        L1[i] = max(L1[i+1], A[i])

    # Maximum value of A[s] - A[r]
    for i in range(n-2, -1, -1):
        L2[i] = max(L2[i+1], L1[i+1] - A[i])
    
    # Maximum value of A[s] - A[r] + A[q]
    for i in range(n-3, -1, -1):
        L3[i] = max(L3[i+1], L2[i+1] + A[i])
    
    # Maximum value of A[s] - A[r] + A[q] - A[p]
    for i in range(n-4, -1, -1):
        L4[i] = max(L4[i+1], L3[i+1] - A[i])

    # maximum value is present in L4[0]
    return L4[0]

if __name__ == '__main__':
    arr = [3, 9, 10, 1, 30, 40]
    print("\nMaximum value = %d\n" %maximizeValue(arr))