'''
Given a MxN matrix where each cell can have value of 0, 1, -1 where -1 denotes unsafe cell, 
collect maximum number of 1s starting from first cell and by visiting only safe cells (0 or 1). 
We are allowed to go left or down if the row is odd otherwise right or down from current cell.

Time complexity : O(mn)
Space complexity: O(mn)
'''

def collectMaximumOnes(A):
    
    # data structure to store the how many 1s is collected ending
    # at each cell 
    m, n = len(A), len(A[0])

    T = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        T[i][n] = A[i-1][n-1]
    
    res = 0

    for i in range(1, m+1):
        # for odd rows left/down
        if i%2!=0:
            for j in range(1, n+1):
                if A[i-1][j-1]==-1:
                    T[i][j] = 0
                else:
                    T[i][j] = A[i-1][j-1] + max(T[i][j-1], T[i-1][j])
                    res = max(res, T[i][j])

        # for even rows right/down 
        else:
            # need value of right cell to update current cell
            for j in range(n-1, 0, -1):
                if A[i-1][j-1]==-1:
                    T[i][j] = 0 
                else:
                    T[i][j] = A[i-1][j-1] + max(T[i][j+1], T[i-1][j])
                    res = max(res, T[i][j])
         

    return res

if __name__ == '__main__':
    arr = [
            [1, 1, -1, 1, 1],
            [1, 0, 0, -1, 1],
            [1, 1, 1, 1, -1],
            [-1, -1, 1, 1, 1],
            [1, 1, -1, -1, -1]
        ]
    
    print("\nMaximum 1s = %d\n" % collectMaximumOnes(arr))