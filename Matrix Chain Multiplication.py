'''
Matrix Chain Multiplication is an optimization problem to find the most efficient way to 
multiply given sequences of matrices.  

Time Complexity : O(n^3)
Space Complexity: O(1)

'''

def matrixChainMultiplication(dims, i, j, lookup):

    # base case: one matrix
    if j<=i+1:
        return 0  
    
    minCost = float('inf') 

    # check if subproblem is already solved
    if lookup[i][j]==0:

        # Find cost of all possible combinations
        # (M[i+1])                x (M[i+2] * M[i+3] * ... * M[j])
        # (M[i+1] * M[i+2])       x (M[i+3] * ... * M[j])
        # (M[i+1] * ... * M[j-1]) x ( M[j])

        for k in range(i+1, j):

            # cost of (M[i+1] * ... * M[k])
            cost = matrixChainMultiplication(dims, i, k, lookup)

            # cost of (M[k+1] * ... * M[j])
            cost += matrixChainMultiplication(dims, k, j, lookup)

            # cost to multiple [i * k] x [k * j]
            cost += dims[i] * dims[k] * dims[j]

            minCost = min(minCost, cost)
        
        lookup[i][j] = minCost
    
    # minCost to multiply i+1 to j
    return lookup[i][j]

if __name__ == '__main__':
    
    # dimension of matrix i is [i] x [i-1]
    dims = [10, 30, 5, 60]
    n = len(dims)

    # data structure to store results of subproblem
    lookup = [[0 for _ in range(n+1)] for _ in range(n+1)]

    print("\nMinimum cost = %d\n" % matrixChainMultiplication(dims, 0, n-1, lookup))