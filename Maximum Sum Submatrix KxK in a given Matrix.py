'''
Find the maximum sum submatrix of present in the given matrix. 

Time complexity : O(mn)
Space complexity: O(mn)

'''

def findMaximumSumSubmatrix(A, k):

    m, n = len(A), len(A[0])

    # compute the sum matrix
    S = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + A[i-1][j-1] 

    maximumSum = -float('inf')
    max_p, max_q, max_r, max_s = -1, -1, -1, -1

    for r in range(k, m+1):
        for s in range(k, n+1):
            currentSum = S[r][s] - S[r][s-k] - S[r-k][s] + S[r-k][s-k]
            print(r, s, currentSum)
            if currentSum > maximumSum:
                max_p, max_q, max_r, max_s = r-k, s-k, r, s 
                maximumSum = currentSum

    print("\nMatrix : ")
    for i in range(max_p+1, max_r+1):
        for j in range(max_q+1, max_s+1):
            print(A[i-1][j-1], end = ' ')
        print()

    print("\nMaximum Sum = %d\n" % maximumSum)
    # print("(%d, %d) to (%d, %d)\n" % (max_p, max_q-1, max_r-1, max_s-1))


if __name__ == '__main__':
    A = [
            [3, -4, 6, -5, 1],
            [1, -2, 8, -4, -2],
            [3, -8, 9, 3, 1],
            [-7, 3, 4, 2, 7],
            [-3, 7, -5, 7, -6]
    ]

    K = 3

    findMaximumSumSubmatrix(A, K)