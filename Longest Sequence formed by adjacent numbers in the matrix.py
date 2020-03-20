'''
Longest sequence formed by adjacent numbers in the matrix problem is to find longest sequence
of adjacent cells such that their values are +1 the previous cell. 

Time Complexity : O(mn)
Space Complexity: O(mn)

'''

def findLongestPath(A, i, j, lookup):
    m, n = len(A), len(A[0])
    
    key = str(i) + '|' + str(j)

    if key not in lookup:
        
        path = []

        # recur to top cell if it is 1 more than current cell
        if i>0 and A[i-1][j]-A[i][j]==1:
            path = findLongestPath(A, i-1, j, lookup)

        # recur to bottom cell if it is 1 more than current cell
        if i+1<m and A[i+1][j]-A[i][j]==1:
            path = findLongestPath(A, i+1, j, lookup)

        # recur to right cell if it is 1 more than current cell
        if j+1<n and A[i][j+1]-A[i][j]==1:
            path = findLongestPath(A, i, j+1, lookup)

        # recur to left cell if it is 1 more than current cell
        if j>0 and A[i][j-1]-A[i][j]==1:
            path = findLongestPath(A, i, j-1, lookup)

        lookup[key] = [A[i][j]] + path
    
    return lookup[key]

if __name__ == '__main__':
    matrix = [ 
                [10, 13, 14, 21, 23],
                [11,  9, 22,  2,  3],
                [12,  8,  1,  5,  4],
                [15, 24,  7,  6, 20],
                [16, 17, 18, 19, 25]
            ]
    m, n = len(matrix), len(matrix[0])

    # data structure to result of subproblems
    lookup = {}

    longestPath = []

    # compute the longest path starting from each cell 
    for i in range(m):
        for j in range(n):
            currentPath = findLongestPath(matrix, i, j, lookup)
            
            if len(currentPath) > len(longestPath):
                longestPath = currentPath
    
    print("Longest path = ", longestPath)