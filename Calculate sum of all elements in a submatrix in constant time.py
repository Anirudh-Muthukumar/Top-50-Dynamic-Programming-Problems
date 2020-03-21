'''
Given a matrix MxN and 'm' queries, find the sum of all the elements in the submatrix 
(p, q) and (r,s) in constant time.

Time complexity : O(m + n^2)
Space complexity: O(n^2)
'''

def submatrixSum(A, p, q, r, s):
    m, n = len(A), len(A[0])

    # compute the sum matrix
    # sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + A[i][j]
    Sum = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            Sum[i][j] = Sum[i-1][j] + Sum[i][j-1] - Sum[i-1][j-1] + A[i-1][j-1] 

    p, q, r, s = p+1, q+1, r+1, s+1 # query is 0-indexed

    # ans = sum[r][s] - sum[r][q-1] - sum[p-1][s] + sum[p-1][q-1]
    return Sum[r][s] - Sum[r][q-1] - Sum[p-1][s]  + Sum[p-1][q-1]

if __name__ == '__main__':
    A = [ 
            [0, 2, 5, 4, 1],
            [4, 8, 2, 3, 7],
            [6, 3, 4, 6, 2],
            [7, 3, 1, 8, 3],
            [1, 5, 7, 9, 4]
    ]

    p, q = 1, 1
    r, s = 3, 3

    print("\nSubmatrix Sum = %d \n" % submatrixSum(A, p, q, r, s))