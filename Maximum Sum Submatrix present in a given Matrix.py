'''
Find the maximum sum submatrix of present in the given matrix. 

Time complexity : O(n^4)
Space complexity: O(n^2)

'''

def findMaximumSumSubmatrix(A):

    m, n = len(A), len(A[0])

    # compute the sum matrix
    S = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + A[i-1][j-1] 

    maximumSum = -float('inf')
    max_p, max_q, max_r, max_s = -1, -1, -1, -1

    for p in range(1, m+1):
        for r in range(p, m+1):
            for q in range(1, n+1):
                for s in range(q, n+1):
                    currentSum = S[r][s] - S[r][q-1] - S[p-1][s] + S[p-1][q-1]
                    if currentSum > maximumSum:
                        maximumSum = currentSum
                        max_p, max_q, max_r, max_s = p, q, r, s 

    print("\nMaximum Sum = %d\n" % maximumSum)
    print("(%d, %d) to (%d, %d)\n" % (max_p-1, max_q-1, max_r-1, max_s-1))


if __name__ == '__main__':
    A = [
            [-5, -6, 3, 1, 0],
            [9, 7, 8, 3, 7],
            [-6, -2, -1, 2, -4],
            [-7, 5, 5, 2, -6],
            [3, 2, 9, -5, 1]
    ]

    findMaximumSumSubmatrix(A)