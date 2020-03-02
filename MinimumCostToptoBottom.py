# Minimum cost path to reach bottom cell from top cell

def solve(maze):
    N, M = len(maze), len(maze[0])
    T = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            T[i][j] = maze[i][j]

            # only one way to reach any cell in first row -> through adjacent left cell
            if i==0 and j>0:
                T[0][j] += T[0][j-1]
            
            # only way to reach any cell in first column -> through adjacent upper cell
            elif i>0 and j==0:
                T[i][0] += T[i-1][0]
            
            else:
                T[i][j] += min(T[i-1][j], T[i][j-1])
            
    print("Minimum cost: ", T[N-1][M-1])


if __name__ == '__main__':

    maze = [ [4,7,8,6,4],
             [6,7,3,9,2],
             [3,8,1,2,4],
             [7,1,7,3,7],
             [2,9,8,9,3]
            ]
    
    solve(maze)