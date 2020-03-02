
def largestSquareMatrix(grid):
    N, M = len(grid), len(grid[0])
    T = [[0 for _ in range(M)] for _ in range(N)]

    maxlen = 0

    for i in range(N):
        for j in range(M):
            T[i][j] = grid[i][j]

            if i>0 and j>0 and grid[i][j]==1:
                T[i][j] = min(T[i-1][j-1], min(T[i-1][j], T[i][j-1])) + 1
            # print(T[i][j], end = ' ')
            if maxlen < T[i][j]:
                maxlen = T[i][j]
        # print()
    
    print("Side = ", maxlen)

if __name__ == '__main__':
    matrix = [  [0,0,1,0,1,1],
                [0,1,1,1,0,0],
                [0,0,1,1,1,1],
                [1,1,1,1,1,1],
                [1,1,1,1,1,1],
                [1,1,1,1,1,1],
                [1,0,1,1,1,1],
                [1,1,1,0,1,1]
            ]
    
    largestSquareMatrix(matrix)