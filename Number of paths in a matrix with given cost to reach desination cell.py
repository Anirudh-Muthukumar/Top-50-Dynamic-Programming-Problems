'''
Find the total number of paths from top cell to bottom cell with given cost.

Time complexity : O(m * n * cost)
Space complexity: O(mn)

'''

def numberOfPaths(A, m, n, cost, lookup):

    # base case: 
    if cost<0:
        return 0

    # first cell 
    if m==0 and n==0:
        if A[m][n]==cost:
            return 1
        else:
            return 0
    
    # dynamic input 
    key = str(m) + '|' + str(n) + '|' + str(cost)

    if key not in lookup:
        if m==0:
            lookup[key] =  numberOfPaths(A, 0, n-1, cost - A[m][n], lookup)
        
        elif n==0:
            lookup[key] =  numberOfPaths(A, m-1, 0, cost - A[m][n], lookup)

        else:
            lookup[key] =  numberOfPaths(A, m-1, n, cost - A[m][n], lookup) + numberOfPaths(A, m, n-1, cost - A[m][n], lookup)
        
    return lookup[key]

if __name__ == '__main__':

    grid =  [ 
             [4, 7, 1, 6],
             [5, 7, 3, 9],
             [3, 2, 1, 2],
             [7, 1, 6, 3]
            ]

    cost = 25 
    m, n = len(grid), len(grid[0])

    print("\nNumber of paths = %d\n" %numberOfPaths(grid, m-1, n-1, cost, {}))
    