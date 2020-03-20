'''
Given a rod of length n and list of prices of rod length i, find the optimal way 
to cut the rod into smaller rods such that profit is maximized. 

Time complexity : O(n^2)
Space complexity: O(n)
'''

def rodCut(price, n):
    # array to store the profit of length i 
    T = [0] * (n+1)

    for i in range(1, n+1):
        # a rod of length i can be cut into (1, i-1), (2, i-2), ... (i, 0)
        # cost(length=1) = T[i] or price[j-1] + T[i-j]
        for j in range(1, i+1):
            T[i] = max(T[i], price[j-1] + T[i-j])
    
    return T[n]


if __name__ == '__main__':
    price = [1,5,8,9,10,17,17,20]
    n = 4
    print("Maximum profit = ", rodCut(price, n))