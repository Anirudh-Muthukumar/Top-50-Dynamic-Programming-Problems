'''
Given a rod of length n and list of prices for each length, cut the rod into smaller rods
such that product of the prices is maximized. 

Time complexity : O(n^2)
Space complexity: O(n)

'''

def maximumProduct(n):
    # array to store the results of length i 
    T = [i for i in range(n+1)]

    for i in range(1, n+1):
        # each rod of length i can be cut into (1, i-1), (2, i-2), ... ,(i, 0)
        for j in range(1, i+1):
            T[i] = max(T[i], j * T[i-j])
    
    return T[n]


if __name__ == '__main__':
    # price of each length is same as length
    n = 15 

    print("\nMaximum product = %d\n" %maximumProduct(n))