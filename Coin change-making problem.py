'''
Given a set of denominations of unlimited supply, return the minimum possible coins 
to get to the given target.

Time complexity : O(n * target)
Space complexity: O(n)
'''

def coinChange(denominations, target):

    n = len(denominations)

    # array to store minimum # of coins to get to total of i 
    T = [float('inf')] * (target+1)

    T[0] = 0

    for total in range(1, target+1):
        res = float('inf')
        for denomination in denominations:
            if denomination <= total:
                # ways to reach using a particular denomination
                res = T[total-denomination]

                # update minimum coins needed if using current 
                # coin resulted in a solution
                T[total] = min(T[total], res+1)

    return T[target]


if __name__ == '__main__':
    denominations = [1, 3, 5, 7]
    target = 15
    print("\nMinimum # of coins = %d\n" % coinChange(denominations, target))